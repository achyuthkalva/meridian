#!/usr/bin/env python3
"""Check Meridian's mechanical safeguards without judging strategic quality.

This validator protects package structure, Level Guide naming, local links,
centralized research sources, evaluation fixtures, Markdown conventions, JSON,
and README SVG safety. Human review still decides whether evidence is credible
and whether a strategy or ecosystem view is useful.
"""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "meridian"
README = ROOT / "README.md"

EXPECTED_LEVELS = {
    "level-00-human-purpose.md": "# Level 0 — Human Purpose in Context",
    "level-01-current-experience.md": "# Level 1 — Current Experience",
    "level-02-problem-opportunity.md": "# Level 2 — Problem and Opportunity Space",
    "level-03-strategic-ux-outcome.md": "# Level 3 — Strategic UX Outcome",
    "level-04-experience-vision.md": "# Level 4 — Experience Vision",
    "level-05-experience-strategy.md": "# Level 5 — Experience Strategy",
    "level-06-product-strategy.md": "# Level 6 — Product Strategy",
    "level-07-experience-roadmap.md": "# Level 7 — Experience Roadmap and Priorities",
    "level-08-critical-experience.md": "# Level 8 — Critical Experience",
    "level-09-scenarios-journeys.md": "# Level 9 — Scenarios and Journeys",
    "level-10-solution-concepts.md": "# Level 10 — Solution Concepts",
    "level-11-capabilities-features.md": "# Level 11 — Enabling Capabilities and Features",
    "level-12-interaction-architecture.md": "# Level 12 — Interaction Architecture",
    "level-13-interface-prototyping.md": "# Level 13 — Interface Definition and Prototyping",
    "level-14-validation-implementation.md": "# Level 14 — Validation and Implementation Definition",
    "level-15-delivery-outcome-learning.md": "# Level 15 — Delivery, Live Experience, and Outcome Learning",
}

LINK_PATTERN = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
HTML_SOURCE_PATTERN = re.compile(r"(?:src|href)=[\"']([^\"']+)[\"']")
URL_PATTERN = re.compile(r"https?://[^\s)\]>'\"]+")
SOURCE_LINK_PATTERN = re.compile(r"\[source\]\(source-index\.md#([a-z0-9-]+)\)")
LEGACY_TERMS = (
    "Full Component Card",
    "Full component card",
    "full component card",
    "Module 3",
    "M3-",
    "Experience Portfolio and Priorities",
    "level-07-experience-portfolio",
    "Wiley",
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_required_files(errors: list[str]) -> None:
    required = [
        README,
        SKILL / "SKILL.md",
        SKILL / "agents" / "openai.yaml",
        SKILL / "references" / "level-map.md",
        SKILL / "references" / "experience-ecosystem.md",
        SKILL / "references" / "source-index.md",
        ROOT / "evals" / "suite.json",
        ROOT / "evals" / "evaluation-report.md",
        ROOT / "evals" / "cases.md",
    ]
    for path in required:
        if not path.is_file():
            fail(errors, f"Missing required file: {path.relative_to(ROOT)}")


def validate_skill_frontmatter(errors: list[str]) -> None:
    path = SKILL / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) > 500:
        fail(errors, f"SKILL.md has {len(lines)} lines; the limit is 500")
    if not lines or lines[0] != "---":
        fail(errors, "SKILL.md must begin with YAML frontmatter")
        return
    closing = next((index for index, line in enumerate(lines[1:], start=1) if line == "---"), None)
    if closing is None:
        fail(errors, "SKILL.md frontmatter is not closed")
        return

    fields: dict[str, tuple[str, list[str]]] = {}
    current: str | None = None
    for line_number, line in enumerate(lines[1:closing], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            if current is None:
                fail(errors, f"Unexpected indented frontmatter line {line_number}")
            else:
                fields[current][1].append(line.strip())
            continue
        match = re.fullmatch(r"([A-Za-z0-9_-]+):(?:\s*(.*))?", line)
        if not match:
            fail(errors, f"Malformed top-level frontmatter line {line_number}")
            current = None
            continue
        key, raw_value = match.group(1), match.group(2) or ""
        if key in fields:
            fail(errors, f"Duplicate frontmatter field: {key}")
        fields[key] = (raw_value, [])
        current = key

    allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    unknown = sorted(set(fields) - allowed)
    missing = sorted({"name", "description"} - set(fields))
    if unknown:
        fail(errors, f"Unsupported frontmatter fields: {unknown}")
    if missing:
        fail(errors, f"Missing required frontmatter fields: {missing}")

    def scalar(field: str) -> str:
        raw, continuation = fields.get(field, ("", []))
        raw = raw.strip()
        if raw in {"|", ">"}:
            joiner = "\n" if raw == "|" else " "
            value = joiner.join(continuation).strip()
        else:
            value = " ".join([raw, *continuation]).strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        return value

    name = scalar("name")
    description = scalar("description")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        fail(errors, "Skill name must use 1–64 lowercase letters, numbers, or single hyphens")
    if name != SKILL.name:
        fail(errors, f"Skill name must match its directory: expected {SKILL.name!r}")
    if not 1 <= len(description) <= 1024:
        fail(errors, "Skill description must contain 1–1024 characters")
    if "license" in fields and not scalar("license"):
        fail(errors, "The optional license field cannot be empty")
    if "compatibility" in fields and not 1 <= len(scalar("compatibility")) <= 500:
        fail(errors, "The optional compatibility field must contain 1–500 characters")
    if "allowed-tools" in fields and not scalar("allowed-tools"):
        fail(errors, "The optional allowed-tools field cannot be empty")
    if "metadata" in fields:
        raw, continuation = fields["metadata"]
        if not raw.strip() and not continuation:
            fail(errors, "The optional metadata field must contain a mapping")
        if raw.strip() and not (raw.strip().startswith("{") and raw.strip().endswith("}")):
            fail(errors, "Inline metadata must use a YAML mapping")
        for entry in continuation:
            if not re.fullmatch(r"[^:]+:\s*.+", entry):
                fail(errors, f"Malformed metadata entry: {entry!r}")

    if not any(line.strip() for line in lines[closing + 1 :]):
        fail(errors, "SKILL.md needs Markdown instructions after frontmatter")

    forbidden = [SKILL / "README.md", SKILL / "CHANGELOG.md"]
    for item in forbidden:
        if item.exists():
            fail(errors, f"Public documentation must remain outside the skill package: {item.relative_to(ROOT)}")


def validate_level_cards(errors: list[str]) -> None:
    references = SKILL / "references"
    actual = {path.name for path in references.glob("level-[0-9][0-9]-*.md")}
    expected = set(EXPECTED_LEVELS)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        fail(errors, f"Level-card set drifted; missing={missing}, extra={extra}")
    for filename, heading in EXPECTED_LEVELS.items():
        path = references / filename
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if heading not in text:
            fail(errors, f"Incorrect or missing heading in {path.relative_to(ROOT)}")
        for required_heading in ("## Card Path", "## Terminology", "### Terminology Status"):
            if required_heading not in text:
                fail(errors, f"Level Guide is missing {required_heading!r}: {path.relative_to(ROOT)}")


def validate_client_metadata(errors: list[str]) -> None:
    path = SKILL / "agents" / "openai.yaml"
    text = path.read_text(encoding="utf-8")
    required_patterns = {
        "interface block": r"^interface:\s*$",
        "display name": r'^\s+display_name:\s*["\']Meridian["\']\s*$',
        "short description": r"^\s+short_description:\s*.+$",
        "default prompt": r"^\s+default_prompt:\s*.+\$meridian.+$",
    }
    for label, pattern in required_patterns.items():
        if not re.search(pattern, text, re.MULTILINE):
            fail(errors, f"Client metadata is missing a valid {label}: {path.relative_to(ROOT)}")


def local_target(base: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().split()[0].strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:", "data:")):
        return None
    target = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not target:
        return None
    return (base / target).resolve()


def validate_local_links(errors: list[str]) -> None:
    markdown_files = [README, *sorted(SKILL.rglob("*.md")), *sorted((ROOT / "evals").rglob("*.md"))]
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        targets = LINK_PATTERN.findall(text) + HTML_SOURCE_PATTERN.findall(text)
        for raw_target in targets:
            target = local_target(path.parent, raw_target)
            if target is None:
                continue
            try:
                target.relative_to(ROOT)
            except ValueError:
                fail(errors, f"Link escapes repository in {path.relative_to(ROOT)}: {raw_target}")
                continue
            if not target.exists():
                fail(errors, f"Broken local link in {path.relative_to(ROOT)}: {raw_target}")


def markdown_files() -> list[Path]:
    return [README, *sorted(SKILL.rglob("*.md")), *sorted((ROOT / "evals").glob("*.md"))]


def validate_markdown_structure(errors: list[str]) -> None:
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        h1_count = len(re.findall(r"^# (?!#)", text, re.MULTILINE))
        if h1_count != 1:
            fail(errors, f"Markdown file needs exactly one H1: {path.relative_to(ROOT)}")
        if re.search(r"\|[^\n]*---:", text):
            fail(errors, f"Markdown table uses right-aligned columns: {path.relative_to(ROOT)}")
        for legacy in LEGACY_TERMS:
            if legacy in text:
                fail(errors, f"Legacy term {legacy!r} remains in {path.relative_to(ROOT)}")
        if re.search(r"Last [Uu]pdated", text):
            fail(errors, f"Last-updated metadata remains in {path.relative_to(ROOT)}")


def validate_source_architecture(errors: list[str]) -> None:
    references = SKILL / "references"
    index = references / "source-index.md"
    if not index.is_file():
        return
    index_text = index.read_text(encoding="utf-8")
    anchors = set(re.findall(r'<a id="([a-z0-9-]+)"></a>', index_text))
    urls = URL_PATTERN.findall(index_text)
    duplicates = sorted({url for url in urls if urls.count(url) > 1})
    if duplicates:
        fail(errors, f"Research Source Index repeats external URLs: {duplicates}")

    for path in sorted(references.glob("*.md")):
        if path == index:
            continue
        text = path.read_text(encoding="utf-8")
        if URL_PATTERN.search(text):
            fail(errors, f"External research URL must live only in source-index.md: {path.relative_to(ROOT)}")
        missing_anchors = sorted(set(SOURCE_LINK_PATTERN.findall(text)) - anchors)
        if missing_anchors:
            fail(errors, f"Unknown source-index anchor in {path.relative_to(ROOT)}: {missing_anchors}")
        if re.search(r"\[\^[^\]]+\]", text):
            fail(errors, f"Legacy footnote citation remains in {path.relative_to(ROOT)}")


def validate_evaluation_suite(errors: list[str]) -> None:
    path = ROOT / "evals" / "suite.json"
    if not path.is_file():
        return
    try:
        suite = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return
    expected_ids = [f"Test Case {number}" for number in range(1, 8)]
    actual_ids = [case.get("id") for case in suite.get("cases", [])]
    if actual_ids != expected_ids:
        fail(errors, f"Evaluation case IDs must be {expected_ids}; found {actual_ids}")
    for number in (1, 5, 7):
        fixture = ROOT / "evals" / "fixtures" / f"test-case-{number}"
        if not fixture.is_dir():
            fail(errors, f"Missing named fixture folder: {fixture.relative_to(ROOT)}")


def validate_json(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            fail(errors, f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")


def validate_svgs(errors: list[str]) -> None:
    assets = ROOT / "assets" / "readme"
    svg_files = sorted(assets.glob("*.svg"))
    expected = {
        "meridian-mark.svg",
        "meridian-hero.svg",
        "strategic-chain.svg",
        "evidence-controls.svg",
        "interaction-model.svg",
        "human-gates.svg",
        "progressive-disclosure.svg",
        "evaluation.svg",
    }
    if {path.name for path in svg_files} != expected:
        fail(errors, "README SVG asset set is incomplete or contains an unexpected file")
    for path in svg_files:
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError as exc:
            fail(errors, f"Invalid SVG XML in {path.relative_to(ROOT)}: {exc}")
            continue
        namespace = "{http://www.w3.org/2000/svg}"
        if root.tag != f"{namespace}svg":
            fail(errors, f"Invalid SVG root in {path.relative_to(ROOT)}")
        title = root.find(f"{namespace}title")
        desc = root.find(f"{namespace}desc")
        if title is None or desc is None:
            fail(errors, f"SVG needs title and desc accessibility text: {path.relative_to(ROOT)}")
        if root.get("role") != "img" or not root.get("aria-labelledby"):
            fail(errors, f"SVG needs role=img and aria-labelledby: {path.relative_to(ROOT)}")
        labelled_by = set((root.get("aria-labelledby") or "").split())
        available_ids = {element.get("id") for element in root.iter() if element.get("id")}
        if not labelled_by or not labelled_by.issubset(available_ids):
            fail(errors, f"SVG aria-labelledby must reference existing IDs: {path.relative_to(ROOT)}")
        if title is not None and not "".join(title.itertext()).strip():
            fail(errors, f"SVG title cannot be empty: {path.relative_to(ROOT)}")
        if desc is not None and not "".join(desc.itertext()).strip():
            fail(errors, f"SVG desc cannot be empty: {path.relative_to(ROOT)}")
        raw = path.read_text(encoding="utf-8")
        lowered = raw.lower()
        if (
            "<script" in lowered
            or "foreignobject" in lowered
            or "javascript:" in lowered
            or re.search(r"\bon[a-z]+\s*=", lowered)
            or re.search(r"(?:href|xlink:href)\s*=\s*[\"'](?:https?:|//)", lowered)
        ):
            fail(errors, f"SVG contains unsupported active or HTML content: {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    validate_required_files(errors)
    if not errors:
        validate_skill_frontmatter(errors)
        validate_level_cards(errors)
        validate_client_metadata(errors)
        validate_local_links(errors)
        validate_markdown_structure(errors)
        validate_source_architecture(errors)
        validate_evaluation_suite(errors)
        validate_json(errors)
        validate_svgs(errors)
    if errors:
        print("Meridian repository validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Meridian repository validation passed.")
    print("- Skill structure and frontmatter: baseline checks passed")
    print("- Level Guides: 16 of 16")
    print("- Local links: valid")
    print("- Research sources: centralized and anchor-checked")
    print("- Evaluation suite: 7 named test cases")
    print("- JSON: valid")
    print("- README SVGs: 8 of 8; XML, labels, and active-content checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

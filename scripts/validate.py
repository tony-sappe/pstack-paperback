#!/usr/bin/env python3
"""Check pstack's portable package, host catalogs, and local documentation links."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/pstack"


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key {key!r}")
            result[key] = value
        return result

    return json.loads(path.read_text(), object_pairs_hook=unique)


def check(condition, message, errors):
    if not condition:
        errors.append(message)


def validate():
    errors = []
    paths = {
        "portable": PLUGIN / "plugin.json",
        "codex": PLUGIN / ".codex-plugin/plugin.json",
        "grok": PLUGIN / ".grok-plugin/plugin.json",
        "codex_market": ROOT / ".agents/plugins/marketplace.json",
        "grok_market": ROOT / ".grok-plugin/marketplace.json",
    }
    try:
        docs = {name: read_json(path) for name, path in paths.items()}
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return [str(exc)]

    version = docs["portable"].get("version")
    check(docs["portable"].get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", "portable manifest schema mismatch", errors)
    for name in ("portable", "codex", "grok"):
        check(docs[name].get("name") == "pstack", f"{name} plugin name mismatch", errors)
        check(docs[name].get("version") == version, f"{name} plugin version mismatch", errors)
    check(docs["codex"].get("skills") == "./skills/", "Codex skills path mismatch", errors)
    check((PLUGIN / "skills").is_dir(), "missing package skills directory", errors)
    for name in ("codex_market", "grok_market"):
        entries = docs[name].get("plugins")
        check(isinstance(entries, list) and len(entries) == 1, f"{name} must contain one plugin", errors)
        if not isinstance(entries, list) or len(entries) != 1:
            continue
        entry = entries[0]
        source = entry.get("source", {})
        check(entry.get("name") == "pstack", f"{name} plugin entry name mismatch", errors)
        key = "source" if name == "codex_market" else "type"
        check(source.get(key) == "local", f"{name} must use a local source", errors)
        check(source.get("path") == "./plugins/pstack", f"{name} source path mismatch", errors)
        check((ROOT / source.get("path", "missing")).resolve() == PLUGIN.resolve(), f"{name} source does not resolve to package", errors)

    skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
    check(bool(skills), "no discoverable skills", errors)
    for removed in (
        ROOT / "automations/benny",
        PLUGIN / "cursor-only",
        *(PLUGIN / "skills" / name for name in ("setup-pstack", "automate-me", "make-bot-ui")),
        PLUGIN / "skills/poteto-mode/scripts",
        PLUGIN / "skills/poteto-mode/references/bugbot-triage.md",
        *(PLUGIN / "skills/poteto-mode/playbooks" / f"{name}.md" for name in ("autopilot-full", "autopilot-stack", "orchestrate", "multi-phase-plan", "shipping")),
    ):
        check(not removed.exists(), f"removed workflow remains: {removed.relative_to(ROOT)}", errors)
    for path in skills:
        contents = path.read_text()
        match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", contents, re.S)
        if not match:
            errors.append(f"{path.relative_to(ROOT)}: missing frontmatter")
            continue
        frontmatter = match.group(1)
        check(bool(re.search(rf"^name:\s*['\"]?{re.escape(path.parent.name)}['\"]?\s*$", frontmatter, re.M)), f"{path.relative_to(ROOT)}: name differs from directory", errors)
        check(bool(re.search(r"^description:\s*\S", frontmatter, re.M)), f"{path.relative_to(ROOT)}: missing description", errors)

    for path in sorted((PLUGIN / "agents").glob("*.md")):
        contents = path.read_text()
        match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", contents, re.S)
        check(bool(match), f"{path.relative_to(ROOT)}: missing agent frontmatter", errors)
        if match:
            check(bool(re.search(rf"^name:\s*{re.escape(path.stem)}\s*$", match.group(1), re.M)), f"{path.relative_to(ROOT)}: agent name differs from filename", errors)

    docs_to_check = [ROOT / "README.md", *ROOT.glob("docs/guide/*.md"), *PLUGIN.rglob("*.md")]
    legacy_pattern = re.compile(r"\.cursor/|cursor-team-kit|\bAskQuestion\b|/loop\b|/goal\b|\bBugbot\b|\bAutopilot-(?:full|stack)\b|playbooks/(?:orchestrate|multi-phase-plan|shipping)\.md|cursor-only/|automations/benny", re.I)
    link_pattern = re.compile(r"\]\(([^)]+)\)")
    for source in docs_to_check:
        contents = source.read_text()
        check(not legacy_pattern.search(contents), f"{source.relative_to(ROOT)}: removed host feature reference", errors)
        for raw in link_pattern.findall(contents):
            target = unquote(raw.split("#", 1)[0].strip("<>"))
            if not target or target == "url" or target.startswith(("http://", "https://", "mailto:", "codex://")):
                continue
            if not (source.parent / target).exists():
                errors.append(f"{source.relative_to(ROOT)}: missing link {target}")
    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        raise SystemExit(1)
    print("pstack package validation passed")

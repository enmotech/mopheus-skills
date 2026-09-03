#!/usr/bin/env python3
"""
install_claude_commands.py - Install Claude Code slash command aliases for Mopheus CLI.
Copies adapters/claude-code/commands/*.md into ~/.claude/commands/ or a specified target.
Works on Windows, Linux, and macOS.
"""

import argparse
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ADAPTER_COMMANDS_DIR = os.path.join(SCRIPT_DIR, "..", "adapters", "claude-code", "commands")


def main():
    parser = argparse.ArgumentParser(description="Install Mopheus Claude Code slash command aliases")
    parser.add_argument(
        "--target-dir",
        default=os.path.expanduser(os.path.join("~", ".claude", "commands")),
        help="Target directory for Claude Code commands (default: ~/.claude/commands)",
    )
    parser.add_argument("--local", action="store_true", help="Install into current directory .claude/commands")
    args = parser.parse_args()

    dest_dir = os.path.abspath(".claude/commands") if args.local else os.path.abspath(args.target_dir)
    os.makedirs(dest_dir, exist_ok=True)

    if not os.path.exists(ADAPTER_COMMANDS_DIR):
        print(f"Error: Source adapter directory {ADAPTER_COMMANDS_DIR} not found", file=sys.stderr)
        sys.exit(1)

    installed = []
    source_mop_dir = os.path.join(ADAPTER_COMMANDS_DIR, "mop")
    dest_mop_dir = os.path.join(dest_dir, "mop")
    if os.path.isdir(source_mop_dir):
        os.makedirs(dest_mop_dir, exist_ok=True)
        for f in os.listdir(source_mop_dir):
            if f.endswith(".md"):
                shutil.copy2(os.path.join(source_mop_dir, f), os.path.join(dest_mop_dir, f))
                installed.append(f"mop:{f[:-3]}")

    for f in os.listdir(ADAPTER_COMMANDS_DIR):
        if f.endswith(".md"):
            src = os.path.join(ADAPTER_COMMANDS_DIR, f)
            dst = os.path.join(dest_dir, f)
            shutil.copy2(src, dst)
            installed.append(f[:-3])

    print(f"Successfully installed {len(installed)} Mopheus commands into {dest_dir}:")
    for cmd in installed:
        print(f"  - /{cmd}")
    print("\nYou can now use these commands directly in Claude Code (e.g. /mop:ticket).")


if __name__ == "__main__":
    main()

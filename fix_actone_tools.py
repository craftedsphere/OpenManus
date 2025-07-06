#!/usr/bin/env python3
"""
Fix ActOne Tools Script
Updates all ActOne tools to return strings instead of ToolResult objects.
"""

import os
import re


def fix_tool_file(file_path):
    """Fix a single tool file to return strings instead of ToolResult."""
    with open(file_path, "r") as f:
        content = f.read()

    # Change return type annotation
    content = re.sub(
        r"async def execute\(self, \*\*kwargs\) -> ToolResult:",
        "async def execute(self, **kwargs) -> str:",
        content,
    )

    # Replace ToolResult(output=...) with string returns
    content = re.sub(
        r"return ToolResult\(output=([^)]+)\)",
        lambda m: f"return str({m.group(1)})",
        content,
    )

    # Replace ToolResult(error=...) with string returns
    content = re.sub(
        r"return ToolResult\(error=([^)]+)\)", lambda m: f"return {m.group(1)}", content
    )

    with open(file_path, "w") as f:
        f.write(content)

    print(f"Fixed: {file_path}")


def main():
    """Fix all ActOne tool files."""
    actone_tools_dir = "app/tool/actone"

    tool_files = [
        "hris_adapter.py",
        "skill_analyzer.py",
        "training_generator.py",
        "compliance_checker.py",
        "dashboard_generator.py",
    ]

    for tool_file in tool_files:
        file_path = os.path.join(actone_tools_dir, tool_file)
        if os.path.exists(file_path):
            fix_tool_file(file_path)
        else:
            print(f"File not found: {file_path}")


if __name__ == "__main__":
    main()

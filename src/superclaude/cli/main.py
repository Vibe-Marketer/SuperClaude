"""
SuperClaude CLI Main Entry Point

Provides command-line interface for SuperClaude operations.
"""

import sys
from pathlib import Path

import click

# Add parent directory to path to import superclaude
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from superclaude import __version__


@click.group()
@click.version_option(version=__version__, prog_name="SuperClaude")
def main():
    """
    SuperClaude - AI-enhanced development framework for Claude Code

    A pytest plugin providing PM Agent capabilities and optional skills system.
    """
    pass


@main.command()
@click.option(
    "--target",
    default="~/.claude/commands/sc",
    help="Installation directory (default: ~/.claude/commands/sc)",
)
@click.option(
    "--force",
    is_flag=True,
    help="Force reinstall if commands already exist",
)
@click.option(
    "--list",
    "list_only",
    is_flag=True,
    help="List available commands without installing",
)
def install(target: str, force: bool, list_only: bool):
    """
    Install SuperClaude commands to Claude Code

    Installs all slash commands (/sc:research, /sc:index-repo, etc.) to your
    ~/.claude/commands/sc directory so you can use them in Claude Code.

    Examples:
        superclaude install
        superclaude install --force
        superclaude install --list
        superclaude install --target /custom/path
    """
    from .install_commands import (
        install_commands,
        list_available_commands,
        list_installed_commands,
    )

    # List only mode
    if list_only:
        available = list_available_commands()
        installed = list_installed_commands()

        click.echo("📋 Available Commands:")
        for cmd in available:
            status = "✅ installed" if cmd in installed else "⬜ not installed"
            click.echo(f"   /{cmd:20} {status}")

        click.echo(f"\nTotal: {len(available)} available, {len(installed)} installed")
        return

    # Install commands
    target_path = Path(target).expanduser()

    click.echo(f"📦 Installing SuperClaude commands to {target_path}...")
    click.echo()

    success, message = install_commands(target_path=target_path, force=force)

    click.echo(message)

    if not success:
        sys.exit(1)


@main.command()
@click.option("--servers", "-s", multiple=True, help="Specific MCP servers to install")
@click.option("--list", "list_only", is_flag=True, help="List available MCP servers")
@click.option(
    "--scope",
    default="user",
    type=click.Choice(["local", "project", "user"]),
    help="Installation scope",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show what would be installed without actually installing",
)
def mcp(servers, list_only, scope, dry_run):
    """
    Install and manage MCP servers for Claude Code

    Examples:
        superclaude mcp --list
        superclaude mcp --servers tavily --servers context7
        superclaude mcp --scope project
        superclaude mcp --dry-run
    """
    from .install_mcp import install_mcp_servers, list_available_servers

    if list_only:
        list_available_servers()
        return

    click.echo(f"🔌 Installing MCP servers (scope: {scope})...")
    click.echo()

    success, message = install_mcp_servers(
        selected_servers=list(servers) if servers else None,
        scope=scope,
        dry_run=dry_run,
    )

    click.echo(message)

    if not success:
        sys.exit(1)


@main.command()
@click.option(
    "--target",
    default="~/.claude/commands/sc",
    help="Installation directory (default: ~/.claude/commands/sc)",
)
def update(target: str):
    """
    Update SuperClaude commands to latest version

    Re-installs all slash commands to match the current package version.
    This is a convenience command equivalent to 'install --force'.

    Example:
        superclaude update
        superclaude update --target /custom/path
    """
    from .install_commands import install_commands

    target_path = Path(target).expanduser()

    click.echo(f"🔄 Updating SuperClaude commands to version {__version__}...")
    click.echo()

    success, message = install_commands(target_path=target_path, force=True)

    click.echo(message)

    if not success:
        sys.exit(1)


@main.command()
@click.argument("skill_name")
@click.option(
    "--target",
    default="~/.claude/skills",
    help="Installation directory (default: ~/.claude/skills)",
)
@click.option(
    "--force",
    is_flag=True,
    help="Force reinstall if skill already exists",
)
def install_skill(skill_name: str, target: str, force: bool):
    """
    Install a SuperClaude skill to Claude Code

    SKILL_NAME: Name of the skill to install (e.g., pm-agent)

    Example:
        superclaude install-skill pm-agent
        superclaude install-skill pm-agent --target ~/.claude/skills --force
    """
    from .install_skill import install_skill_command

    target_path = Path(target).expanduser()

    click.echo(f"📦 Installing skill '{skill_name}' to {target_path}...")

    success, message = install_skill_command(
        skill_name=skill_name, target_path=target_path, force=force
    )

    if success:
        click.echo(f"✅ {message}")
    else:
        click.echo(f"❌ {message}", err=True)
        sys.exit(1)


@main.command()
@click.option(
    "--verbose",
    is_flag=True,
    help="Show detailed diagnostic information",
)
def doctor(verbose: bool):
    """
    Check SuperClaude installation health

    Verifies:
        - pytest plugin loaded correctly
        - Skills installed (if any)
        - Configuration files present
    """
    from .doctor import run_doctor

    click.echo("🔍 SuperClaude Doctor\n")

    results = run_doctor(verbose=verbose)

    # Display results
    for check in results["checks"]:
        status_symbol = "✅" if check["passed"] else "❌"
        click.echo(f"{status_symbol} {check['name']}")

        if verbose and check.get("details"):
            for detail in check["details"]:
                click.echo(f"    {detail}")

    # Summary
    click.echo()
    total = len(results["checks"])
    passed = sum(1 for check in results["checks"] if check["passed"])

    if passed == total:
        click.echo("✅ SuperClaude is healthy")
    else:
        click.echo(f"⚠️  {total - passed}/{total} checks failed")
        sys.exit(1)


@main.command()
def version():
    """Show SuperClaude version"""
    click.echo(f"SuperClaude version {__version__}")


@main.command()
@click.option(
    "--project",
    "-p",
    default=".",
    help="Project directory to configure (default: current directory)",
)
@click.option(
    "--global",
    "global_only",
    is_flag=True,
    help="Only add global MCP servers (run once, works everywhere)",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show what would be configured without making changes",
)
def setup(project: str, global_only: bool, dry_run: bool):
    """
    Configure SuperClaude MCP servers for a project

    WORKFLOW:
    1. Run 'superclaude setup --global' ONCE (adds global MCPs)
    2. Run 'superclaude setup' in each new project (adds Serena only)

    Global MCPs (install once, work everywhere):
    - context7-sse: Documentation lookup
    - sequential-thinking: Structured reasoning
    - tavily: Web search (requires TAVILY_API_KEY)

    Project-specific (must run per-project):
    - serena: Session memory for /sc:load and /sc:save

    Examples:
        superclaude setup --global           # One-time global setup
        superclaude setup                    # Add Serena to current project
        superclaude setup -p /path/to/project
        superclaude setup --dry-run          # Preview changes
    """
    import json
    import os

    claude_config_path = Path.home() / ".claude.json"

    # Load existing config
    if claude_config_path.exists():
        try:
            with open(claude_config_path, "r") as f:
                config = json.load(f)
        except json.JSONDecodeError:
            click.echo(f"❌ Invalid JSON in {claude_config_path}", err=True)
            sys.exit(1)
    else:
        config = {}

    changes_made = []

    # Ensure root-level mcpServers exists
    if "mcpServers" not in config:
        config["mcpServers"] = {}

    if global_only:
        # GLOBAL SETUP MODE: Add all global MCPs to ALL editors
        click.echo("🔧 SuperClaude Global Setup (All Editors)")
        click.echo()

        tavily_key = os.environ.get("TAVILY_API_KEY")
        if not tavily_key:
            click.echo("ℹ️  TAVILY_API_KEY not set - skipping Tavily MCP")
            click.echo("   Set it and re-run to add web search capability")
            click.echo()

        # Define global servers for Claude Code format
        claude_servers = {
            "context7-sse": {
                "type": "sse",
                "url": "https://gitmcp.io/context7/mcp"
            },
            "sequential-thinking": {
                "type": "stdio",
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
                "env": {}
            },
        }
        if tavily_key:
            claude_servers["tavily"] = {
                "type": "stdio",
                "command": "npx",
                "args": ["-y", "tavily-mcp"],
                "env": {"TAVILY_API_KEY": tavily_key}
            }

        # Define global servers for Cursor/Windsurf format (no "type" field)
        cursor_servers = {
            "sequential-thinking": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
            },
        }
        if tavily_key:
            cursor_servers["tavily"] = {
                "command": "npx",
                "args": ["-y", "tavily-mcp"],
                "env": {"TAVILY_API_KEY": tavily_key}
            }

        # 1. Configure Claude Code (~/.claude.json)
        click.echo(f"📁 Claude Code: {claude_config_path}")
        for server_name, server_config in claude_servers.items():
            if server_name not in config["mcpServers"]:
                config["mcpServers"][server_name] = server_config
                changes_made.append(f"[Claude Code] Added: {server_name}")
            else:
                click.echo(f"   ✓ {server_name} already configured")

        # 2. Configure Cursor (~/.cursor/mcp.json)
        cursor_config_path = Path.home() / ".cursor" / "mcp.json"
        if cursor_config_path.parent.exists():
            click.echo(f"📁 Cursor: {cursor_config_path}")
            cursor_config = {}
            if cursor_config_path.exists():
                try:
                    with open(cursor_config_path, "r") as f:
                        cursor_config = json.load(f)
                except json.JSONDecodeError:
                    click.echo(f"   ⚠️  Invalid JSON, will create fresh config")
                    cursor_config = {}

            if "mcpServers" not in cursor_config:
                cursor_config["mcpServers"] = {}

            cursor_changed = False
            for server_name, server_config in cursor_servers.items():
                if server_name not in cursor_config["mcpServers"]:
                    cursor_config["mcpServers"][server_name] = server_config
                    changes_made.append(f"[Cursor] Added: {server_name}")
                    cursor_changed = True
                else:
                    click.echo(f"   ✓ {server_name} already configured")

            if cursor_changed and not dry_run:
                with open(cursor_config_path, "w") as f:
                    json.dump(cursor_config, f, indent=2)

        # 3. Configure Windsurf (~/.codeium/windsurf/mcp.json)
        windsurf_config_path = Path.home() / ".codeium" / "windsurf" / "mcp.json"
        if windsurf_config_path.parent.exists():
            click.echo(f"📁 Windsurf: {windsurf_config_path}")
            windsurf_config = {}
            if windsurf_config_path.exists():
                try:
                    with open(windsurf_config_path, "r") as f:
                        windsurf_config = json.load(f)
                except json.JSONDecodeError:
                    windsurf_config = {}

            if "mcpServers" not in windsurf_config:
                windsurf_config["mcpServers"] = {}

            windsurf_changed = False
            for server_name, server_config in cursor_servers.items():
                if server_name not in windsurf_config["mcpServers"]:
                    windsurf_config["mcpServers"][server_name] = server_config
                    changes_made.append(f"[Windsurf] Added: {server_name}")
                    windsurf_changed = True
                else:
                    click.echo(f"   ✓ {server_name} already configured")

            if windsurf_changed and not dry_run:
                windsurf_config_path.parent.mkdir(parents=True, exist_ok=True)
                with open(windsurf_config_path, "w") as f:
                    json.dump(windsurf_config, f, indent=2)

    else:
        # PROJECT SETUP MODE: Add only Serena for this project
        project_path = Path(project).resolve()

        if not project_path.exists():
            click.echo(f"❌ Project path does not exist: {project_path}", err=True)
            sys.exit(1)

        click.echo("🔧 SuperClaude Project Setup")
        click.echo(f"   Project: {project_path}")
        click.echo(f"   Config:  {claude_config_path}")
        click.echo()

        # Check if global MCPs are configured
        has_global = "sequential-thinking" in config.get("mcpServers", {})
        if not has_global:
            click.echo("⚠️  Global MCPs not configured!")
            click.echo("   Run 'superclaude setup --global' first for best experience.")
            click.echo()

        # Ensure projects dict exists
        if "projects" not in config:
            config["projects"] = {}

        project_key = str(project_path)

        # Ensure project entry exists
        if project_key not in config["projects"]:
            config["projects"][project_key] = {
                "allowedTools": [],
                "mcpContextUris": [],
                "mcpServers": {},
                "hasTrustDialogAccepted": True,
            }
            changes_made.append(f"Created project entry")

        # Ensure project mcpServers exists
        if "mcpServers" not in config["projects"][project_key]:
            config["projects"][project_key]["mcpServers"] = {}

        project_mcps = config["projects"][project_key]["mcpServers"]

        # Add ONLY Serena for this specific project
        if "serena" not in project_mcps:
            project_mcps["serena"] = {
                "type": "stdio",
                "command": "uvx",
                "args": [
                    "--from",
                    "git+https://github.com/oraios/serena",
                    "serena",
                    "start-mcp-server",
                    "--context",
                    "ide-assistant",
                    "--project",
                    str(project_path)
                ],
                "env": {}
            }
            changes_made.append(f"Added Serena MCP for session memory")
        else:
            click.echo("   ✓ Serena already configured for this project")

    # Report changes
    if not changes_made:
        click.echo("✅ Already configured! No changes needed.")
        return

    click.echo("📝 Changes:")
    for change in changes_made:
        click.echo(f"   • {change}")
    click.echo()

    if dry_run:
        click.echo("[DRY RUN] No changes written.")
        return

    # Write config
    try:
        with open(claude_config_path, "w") as f:
            json.dump(config, f, indent=2)
        click.echo(f"✅ Configuration saved!")
        click.echo()
        click.echo("⚠️  Restart Claude Code for changes to take effect!")
        if not global_only:
            click.echo()
            click.echo("After restart, run /sc:load to initialize session memory.")
    except Exception as e:
        click.echo(f"❌ Failed to write config: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()

# Computer Use Skill

> Desktop automation for AI agents — screenshot, click, type, scroll, accessibility trees, form filling, menu navigation, scripts (AppleScript/JXA/PowerShell), app/window management. 49 tools.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-computer--use--mcp-green)](https://github.com/zavora-ai/computer-use-mcp)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | What It Achieves |
|----------|-------|------------------|
| See → Click → Verify | 3 | Screenshot, interact, confirm |
| Fill Form | 2 | Find fields → fill all |
| Menu Action | 2 | Find shortcut → press key |
| Script Automation | 1 | Complex AppleScript/PowerShell |
| App Management | 2 | List → activate |

### Approach Priority
1. **Keyboard shortcut** — fastest (1 call)
2. **Accessibility click** — most reliable (click_element)
3. **Script** — most powerful (run_script)
4. **Coordinate click** — fallback (screenshot + left_click)

## Installation

```bash
git clone https://github.com/zavora-ai/skill-computer-use.git \
  ~/.skills/skills/computer-use
```

## Requirements

**Required:** `computer-use-mcp` (49 tools)
**Platforms:** macOS (AppleScript/JXA), Windows (PowerShell)
**Permissions:** Accessibility access in System Settings

**Cross-MCP:**
- `mcp-browser` — web automation
- `worksheet-mcp` — open generated reports
- `mcp-slack` — desktop notification context

## Success Criteria

| Metric | Target |
|--------|--------|
| Click accuracy | Correct element on first attempt |
| Safety | Never click without screenshot |
| Approach | Accessibility over coordinates |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)

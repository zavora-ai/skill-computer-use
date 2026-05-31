---
name: computer-use
description: Orchestrate desktop computer control — take screenshots, click/type/scroll, manage windows and apps, read accessibility trees, fill forms, run scripts (AppleScript/JXA/PowerShell), manage clipboard, and navigate UI elements. Use when automating desktop tasks, clicking buttons, filling forms, reading screen content, controlling apps, or running desktop scripts.
license: Apache-2.0
compatibility: Requires computer-use-mcp server. macOS (AppleScript/JXA) and Windows (PowerShell). Accessibility permissions required.
allowed-tools: [screenshot, zoom, doctor, policy_status, agent_pointer, openai_computer, left_click, right_click, middle_click, double_click, triple_click, mouse_move, left_click_drag, left_mouse_down, left_mouse_up, scroll, cursor_position, type, key, hold_key, read_clipboard, write_clipboard, open_application, list_running_apps, hide_app, unhide_app, get_window, get_cursor_window, list_windows, get_frontmost_app, activate_app, activate_window, get_display_size, list_displays, wait, get_ui_tree, get_focused_element, find_element, click_element, set_value, press_button, list_menu_bar, select_menu_item, fill_form, run_script, get_app_dictionary, get_tool_guide, get_app_capabilities, list_spaces, get_active_space]
metadata:
  author: Zavora AI
  mcp-server: computer-use-mcp
  category: mcp-enhancement
  success-criteria:
    trigger-rate: "90% on desktop automation queries"
    accuracy: "Click correct element on first attempt"
    safety: "Never click without screenshot verification"
---

# Computer Use

You control the desktop — screenshot to see, click/type to interact, read accessibility trees for precision, fill forms, run scripts, and manage apps/windows. Always screenshot first. Prefer accessibility (click_element) over coordinate clicks. Use get_tool_guide before complex tasks.

## Decision Tree

```
├── "what's on screen", "show me"? → screenshot
├── "click", "press button"? → click_element / left_click
├── "type", "enter text"? → type / set_value
├── "fill form"? → fill_form
├── "open app"? → open_application
├── "menu", "File > Save"? → list_menu_bar → select_menu_item (or key shortcut)
├── "copy", "paste", "clipboard"? → read_clipboard / write_clipboard / key("command+c")
├── "scroll"? → scroll
├── "what app is open"? → get_frontmost_app / list_running_apps
├── "find button", "where is"? → find_element / get_ui_tree
├── "run script", "AppleScript"? → run_script
├── "how should I do this"? → get_tool_guide
```

## Key Workflows

### See → Click → Verify (3 calls)
1. `screenshot()` → see current state
2. `left_click(coordinate: [x, y])` or `click_element(role, label)` → interact
3. `screenshot()` → verify result

### Fill a Form (2 calls)
1. `get_ui_tree(target_app)` → find all fields
2. `fill_form(fields: [{role: "AXTextField", label: "Name", value: "James"}, ...])` → all filled

### Menu Action (2 calls)
1. `list_menu_bar(bundle_id)` → find shortcut (e.g., cmd+s for Save)
2. `key(text: "command+s")` → faster than menu walk

### Script Automation (1 call)
`run_script(language: "applescript", script: 'tell app "Finder" to ...')` → complex automation

### App Management (2 calls)
1. `list_running_apps()` → what's open
2. `activate_app(bundle_id: "com.apple.Safari")` → bring to front

## MUST DO
- Always `screenshot` before clicking (verify target is visible)
- Prefer `click_element`/`press_button` over coordinate clicks (more reliable)
- Use `get_tool_guide` before complex multi-step tasks
- Use `list_menu_bar` to find keyboard shortcuts (faster than menu navigation)
- Verify actions with follow-up `screenshot`

## MUST NOT DO
- Don't click without seeing the screen first
- Don't use coordinate clicks when accessibility elements are available
- Don't type into wrong field (check `get_focused_element` first)
- Don't run destructive scripts without user confirmation
- Don't interact with apps outside the allow list (check `policy_status`)

## Approach Priority

1. **Keyboard shortcut** (fastest) — `key("command+s")`
2. **Accessibility click** (reliable) — `click_element(role, label)`
3. **Script** (powerful) — `run_script` for complex automation
4. **Coordinate click** (fallback) — `left_click([x, y])` when no accessibility

## Cross-MCP Orchestration

### Computer Use + Browser: Web Automation
```
COMPUTER: open_application(bundle_id: "com.apple.Safari")
COMPUTER: screenshot() → see page
BROWSER: navigate(url) → load page (if browser MCP available)
COMPUTER: fill_form(fields) → fill web form (fallback if no browser MCP)
```

### Computer Use + Excel: Desktop Report
```
EXCEL: create_workbook → write data → save("report.xlsx")
COMPUTER: open_application(bundle_id: "com.microsoft.Excel")
COMPUTER: screenshot() → verify report opened correctly
```

## Troubleshooting

**Element not found:** App may not be accessible. Run `get_app_capabilities` to check. Try `screenshot` + coordinate click as fallback.

**Click hits wrong target:** Window may have moved. Take fresh `screenshot`, recalculate coordinates.

**Permission denied:** Run `doctor` for diagnostics. Accessibility permissions needed in System Settings.

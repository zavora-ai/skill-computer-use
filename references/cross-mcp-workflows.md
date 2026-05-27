# Computer Use Cross-MCP Workflows

## Computer Use + Browser: Web Form Automation
```
COMPUTER: open_application("com.apple.Safari")
COMPUTER: screenshot() → see page
COMPUTER: fill_form(fields) → fill web form
COMPUTER: press_button(label: "Submit")
```

## Computer Use + Excel: Open Generated Report
```
EXCEL: save_workbook(path: "report.xlsx")
COMPUTER: run_script(language: "applescript", script: 'tell app "Finder" to open "report.xlsx"')
COMPUTER: screenshot() → verify opened
```

## Computer Use + Slack: Desktop Notification Check
```
COMPUTER: screenshot() → see notification
COMPUTER: left_click(notification_coords) → open
SLACK: get_messages(channel) → context
```

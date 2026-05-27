# Computer Use Examples

## Example 1: "Click the Submit button in Safari"
```
screenshot(target_app: "com.apple.Safari") → [see page with Submit button at (512, 680)]
click_element(role: "AXButton", label: "Submit", target_app: "com.apple.Safari") → clicked
screenshot() → verify form submitted
```
Response: "Clicked Submit button. Page now shows 'Thank you' confirmation."

## Example 2: "Fill in the registration form"
```
get_ui_tree(target_app: "com.apple.Safari") → [fields: Name, Email, Phone]
fill_form(fields: [
  {role: "AXTextField", label: "Name", value: "James Maina"},
  {role: "AXTextField", label: "Email", value: "james@example.com"},
  {role: "AXTextField", label: "Phone", value: "+254700000000"}
], target_app: "com.apple.Safari") → {filled: 3, failed: 0}
```
Response: "Form filled: Name, Email, Phone — all 3 fields set successfully."

## Example 3: "Save the current document"
```
list_menu_bar(bundle_id: "com.apple.TextEdit") → {File: [{name: "Save", shortcut: "command+s"}]}
key(text: "command+s") → pressed
```
Response: "Document saved (⌘S)."

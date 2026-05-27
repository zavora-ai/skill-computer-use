#!/usr/bin/env python3
"""Check if approach should use accessibility or coordinates."""
import json, sys

def recommend(data):
    has_accessibility = data.get("accessible", False)
    has_label = data.get("has_label", False)
    if has_accessibility and has_label:
        return {"approach": "click_element", "reason": "Accessibility available — most reliable"}
    elif has_accessibility:
        return {"approach": "find_element + click", "reason": "Accessible but no direct label"}
    else:
        return {"approach": "screenshot + coordinate click", "reason": "No accessibility — use visual"}

if __name__ == "__main__":
    print(json.dumps(recommend(json.loads(sys.argv[1])), indent=2))

# Safe Placeholder Pattern

This document explains the SafePlaceholder pattern for preventing template variable crashes.

---

## 🛡️ Template Safety (CRITICAL)

> **"Prevent crashes from missing template variables."**

---

## SafePlaceholder Pattern

```python
class SafePlaceholder:
    """Prevents KeyError crashes when template variables are missing."""

    def __getattr__(self, name):
        return self  # Returns self for any missing attribute

    def __format__(self, format_spec):
        return str(self)  # Safe formatting

    def __str__(self):
        return "{placeholder}"  # Visual indicator
```

---

## Usage Example

```python
# ❌ WRONG - Crashes if TITLE missing
template = "Title: {TITLE}".format(TITLE=paper_title)

# ✅ RIGHT - Safe even if TITLE missing
safe_dict = SafePlaceholder()
safe_dict.TITLE = paper_title  # If this line is missing, no crash!
template = "Title: {TITLE}".format_map(safe_dict)
```

---

## When to Use

- LaTeX templates with variable substitution
- Report generation with dynamic content
- Any string formatting with user-provided variables

---

## Key Benefit

If a variable is missing, you get `{placeholder}` instead of a crash.

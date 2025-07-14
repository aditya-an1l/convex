---
name: Security Issue Template
about: Report a security bug in the codebase
title: 'security: <insert title>'
labels: bug
assignees: aditya-an1l

---

### Affected Component

**Specify the part of the codebase affected** 
(e.g., `translator.py`, `parser.py`, input handler, etc.)

---

### Vulnerability Description

**Clearly explain the issue and why it poses a security threat.**

For example:

> The translator currently uses Python’s `exec()` function on user-provided code without restrictions. This allows execution of arbitrary and potentially dangerous code on the host machine.

---

### Impact

**Describe the potential consequences of exploiting this vulnerability.**

Examples include:

* Arbitrary file system access or deletion
* Execution of system-level commands
* Denial of Service (infinite loops, resource exhaustion)
* Unauthorized access to sensitive data or environment

---

### Steps to Reproduce

**Provide a minimal example that clearly demonstrates the vulnerability**

Example:

Running the following will lead to deletion of all files in the directory
```python
import os
os.system("rm -rf ./")
```

or:

Running the following code will lead to infinite loop
```python
while True:
    pass  # infinite loop causing the system to hang
```

---

### Suggested Fix (optional)

Propose one or more approaches to mitigate the issue (if possible)

### If proposed a fix, check the relevant options from the following:

* [ ] Vulnerable behavior is blocked or isolated
* [ ] Legitimate code continues to function correctly
* [ ] Fix is tested and reproducible examples are handled securely
* [ ] Fix does not introduce new vulnerabilities

---

### Additional Notes

Include any links, references, or related issues that may assist in resolving the vulnerability.

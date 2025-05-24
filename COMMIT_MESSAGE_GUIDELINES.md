# ✅ Commit Message Guidelines

Writing clear and consistent commit messages makes collaboration easier, improves code review, and enhances project maintainability. Here’s how to write effective commit messages.

---

## ✍️ General Guidelines

* **Use imperative mood** in the summary
  *Example: "Add feature" (✔️) instead of "Added feature" (✖️)*

* **Start with a short summary** (max 50 characters if possible).
  This summary should clearly state **what** the change does.

* **Add an optional body** to explain the **why**, **how**, or **impact** of the change.
  Keep lines within 72 characters.

* **Group commits by intent** using standard commit types (see below).

---

## 🧠 Why This Matters

* Makes the commit history easy to read
* Helps reviewers understand your changes quickly
* Enables better release notes and changelogs

---

## 🏷️ Commit Types

Use the following tags at the start of your commit message:

| Type       | Description                                          |
| ---------- | ---------------------------------------------------- |
| `feat`     | Add a new feature                                    |
| `fix`      | Fix a bug                                            |
| `docs`     | Update documentation                                 |
| `style`    | Code style changes (spacing, formatting, etc.)       |
| `refactor` | Code changes that don't fix bugs or add features     |
| `test`     | Add or update tests                                  |
| `chore`    | Maintenance tasks (e.g., dependency updates)         |
| `perf`     | Improve performance                                  |
| `security` | Address security issues                              |
| `merge`    | Merge branches                                       |
| `revert`   | Revert a previous commit                             |
| `build`    | Modify build system or dependencies                  |
| `ci`       | CI-related changes (GitHub Actions, etc.)            |
| `config`   | Changes to config files (e.g., `.env`, `.gitignore`) |
| `deploy`   | Changes related to deployment process                |
| `init`     | Initial commit or project setup                      |
| `move`     | Move files/directories                               |
| `rename`   | Rename files/directories                             |
| `remove`   | Delete files/directories                             |
| `update`   | General updates that don't fall into other types     |

---

## 🧪 Examples

```txt
feat: Add user authentication module
fix: Resolve crash on startup due to null pointer
docs: Update README with setup instructions
style: Reformat code using Black
refactor: Simplify conditional logic in parser
test: Add tests for Hindi keyword mapping
chore: Bump version in pyproject.toml
```

---

## 🧩 Custom Tags

If your team introduces new commit types, document and **add them to this list**. Submit a PR to update this file so others can follow the standard.

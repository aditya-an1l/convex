# ✅ Commit Message Guidelines

Clear and consistent commit messages make your project easier to understand, maintain, and scale. This guide helps contributors write high-quality, standardized commit messages.


## ✍️ General Guidelines

-   **Use imperative mood**  
    _Example: "Add feature" (✔️) instead of "Added feature" (✖️)_
-   **Make atomic commits**  
    Each commit should contain one logical change. Avoid combining unrelated changes in a single commit.
-   **Write a concise summary** (≤ 50 characters preferred)  
    It should clearly describe **what** the change does.
-   **Wrap commit title in the body at 72 characters**  
    This makes logs easier to read across tools.
-   **Use the commit description to explain _why_ and _how_**, not just _what_.  
    Include reasoning, edge cases handled, limitations, or relevant context.
    

## 📄 Commit Message Template

```txt
<type>: <short summary>

[Optional longer description providing context and reasoning]

[Optional footer: e.g., Closes #123, Related to #456]

```

### 🔍 Example

```txt
feat: Add Hindi-to-Python translation support

This adds a parser that maps Hindi keywords to Python syntax 
using a JSON language pack. Includes basic error handling 
for unknown keywords and missing files.

Closes #12

```



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


### Example  of Different Commit Type

```txt
feat: Add user authentication module
fix: Resolve crash on startup due to null pointer
docs: Update README with setup instructions
style: Reformat code using Black
refactor: Simplify conditional logic in parser
test: Add tests for Hindi keyword mapping
chore: Bump version in pyproject.toml
```

## 🧪 Tips for Better Commits

✅ Do:

-   Make each commit purposeful and atomic
    
-   Write clear summaries and helpful bodies
    
-   Reference relevant issues (`Closes #<put-issue-number-here>`)
    

🚫 Don’t:

-   Write vague messages like “fix stuff” or “changes”
    
-   Mix unrelated changes in a single commit
    
-   Use past tense in the summary
    
## 🧩 Custom Types

If your team adds new commit types, document them here and submit a PR to update this guide.

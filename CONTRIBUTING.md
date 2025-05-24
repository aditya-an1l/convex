## 🤝 Contributing to Convex

Thank you for your interest in contributing to **Convex**! We follow a clear, collaborative workflow to ensure code quality and shared ownership. Please read through these steps before submitting your first contribution.

***Do not hesitate to ask the [maintainers](https://github.com/aditya-an1l/convex/tree/main?tab=readme-ov-file#-collaborators) for help***

---

### 📋 Prerequisites

1. **Git installed** on your machine (version ≥2.20).  
2. A **GitHub account** with access to this repository.  
3. (Optional but recommended) A local **Python** (3.8+) and **Node.js** (14+) setup to run tests and preview the app.

---

### 🚀 1. Fork & Clone

1. **Fork** the Convex repository on GitHub (top-right “Fork” button).  
2. **Clone** your fork locally:
   ```sh
   git clone https://github.com/aditya-an1l/convex.git
   cd convex
   ```

3. **Add the upstream remote** to keep your fork in sync:

   ```sh
   git remote add upstream https://github.com/aditya-an1l/convex.git
   git fetch upstream
   ```

---

### 🌿 2. Create a Feature Branch

1. **Checkout** the latest `main`:

   ```sh
   git checkout main
   git pull upstream main
   ```
2. **Create a new branch** for your work. Use a clear, descriptive name:

   ```sh
   git checkout -b feature/<short-description>
   ```

   *Example:* `feature/hindi-syntax-support`

---

### ✏️ 3. Implement Your Changes

* Make your code changes
* Keep commits **small** and **focused**.
* Write **clear commit messages**. Refer to [COMMIT_MESSAGE_GUIDELINES](https://github.com/aditya-an1l/convex/blob/main/COMMIT_MESSAGE_GUIDELINES.md) to know about writing clear and consistent commit messages. Following are some examples:

  ```
  feat: add loop support to Hindi translator
  fix: correct JSON syntax in tamil.json
  docs: update CONTRIBUTING.md with branch policy
  ```

---

### ☁️ 4. Push Your Branch

```sh
git push origin feature/<short-description>
```

---

### 🔀 5. Open a Pull Request

1. Go to your fork on GitHub, select your branch, and click **“New Pull Request”**.
2. Ensure the base repository is `aditya-an1l/convex` and base branch is `main`.
3. In the PR description:

   * **Summarize** your changes and why they’re needed.
   * Link any relevant issues: “Closes #123”.
   * Provide **screenshots** or examples if applicable.
4. Choose **“Request a review”** from one or more collaborators.

---

### ✅ 6. Code Review & Approval

Your PR must:

* ✅ Receive **at least 1 approval** from a repository collaborator.
* 🚫 **Not be merged** by the same person who made the last commit on `main`.

> Collaborators will do their best to review and respond promptly (typically within 48 hours).

---

### ➕ 7. Merging Your PR

Once approved:

1. A **different collaborator** (not the last committer on `main`) will merge your PR.
2. To ensure synchronicity, other contributor must  pull the updated `main` into their local clone and push, ensuring branch protection remains intact.

---

### 📞 Need Help?

* **Ask questions** on the [issue](https://github.com/aditya-an1l/convex/issues) tracker or in our [Discussion](https://github.com/aditya-an1l/convex/discussions) channel.
* **Ping any collaborator** directly for guidance or unblockers.

---

### 🔄 Why This Policy?

* **Peer review** ensures higher code quality and shared knowledge.
* **Branch protection** prevents accidental direct pushes to `main`.
* **Two-person merge rule** encourages collaboration and accountability.

> 💡 **Note:** Pull requests that do not follow this process will be blocked by our GitHub branch protection settings.

Thank you for helping make Convex better and more inclusive! 🌏✨

--- 

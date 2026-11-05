# Validation for 0.27.22

[简体中文](TEST_RESULTS.md) | **English**

All 18 fixed release gates passed. Production files stayed unchanged during final QA; every VSIX file matches the audited bytes.
Coverage includes Node regressions, source/citation contracts, Python compatibility, editing workflows, history restoration, browser checks, and isolated pytest projects.

Portable-backend checks copy only distribution files, clear external backend paths, disable third-party Python site packages, and complete static analysis and chain protocol checks.

A dedicated sample used live Codex for cold-start structure generation, a main-root explanation, and a leaf-function return-use explanation. Its three pytest cases passed.
Source-to-output inspection checked truth-value filtering, whitespace preservation, the actual unguarded append behavior, and the scope of return-value uses.
These checks do not access the developer's business project or establish compatibility with every project or model.

The audited VSIX was also installed in separate VS Code user and extension directories. Activation, command registration, bundled-backend analysis, and the structure-window connection passed.
That step reused a source-version-bound sample model, made no online provider calls, used no personal API key, and did not replace the everyday extension.

Packaging uses an explicit file list, excluding chats, test projects, development caches, and personal settings. Credential patterns are scanned during packaging.
Users must provide their own model key or login.

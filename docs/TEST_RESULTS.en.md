# Preview validation

[简体中文](TEST_RESULTS.md) | **English**

## 0.27.24

In an isolated Windows VS Code installation of the release package, tracing the sample and selecting **Open use site** for `open_app` highlighted line 17. The sidebar browser suite passed, including source navigation for a fresh trace after chat restoration and read-only older traces. All 20 call-chain tests passed.

## 0.27.23

The distributed VSIX was installed in isolated Windows VS Code user and extension directories. Using the public `demo/desktop.py`, the static trace followed `make_launch_request()` into `on_start_click()` and the `open_app(request)` use site without model configuration.

All 156 Node regressions and 20 call-chain tests passed. The standalone provider suite still has one assertion failure about prompt wording.

## 0.27.22

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

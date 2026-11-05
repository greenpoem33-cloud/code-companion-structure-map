# Code Companion Structure Map

[简体中文](README.md) | **English**

A VS Code tool for exploring Python project structure, following call chains, and getting source-linked AI explanations.

**Preview release 0.27.22.** This repository provides installable test packages, documentation, and a place to report feedback.
The development source and test project are not publicly released. A future open-source release may be considered after the product stabilizes; no open-source license is granted with this preview.

## Download and setup

Download the VSIX from [Releases](https://github.com/greenpoem33-cloud/code-companion-structure-map/releases),
choose **Install from VSIX…** in VS Code, and reload the window.
See [Installation](docs/INSTALL.en.md) for prerequisites and configuration.

Each user must supply their own DeepSeek API key or sign in to their own Codex account.
The package does not include the developer's API keys, login credentials, personal settings, or chat history.

## What to try

- Analyze a project and explore its structure map in the sidebar, editor area, or a separate window.
- Follow source-backed calls from an entry point or selected function. Open code or continue explaining from a node.
- Inspect how a leaf function's return value is received, stored, passed onward, or returned by its callers.
- Distinguish static relationships, observations from passing tests, and unresolved relationships.
- Review code diffs before applying changes. Confirm structural impact before writing; cancelling keeps the proposal without changing source.

## Feedback

Use [Issues](https://github.com/greenpoem33-cloud/code-companion-structure-map/issues) to report a reproducible problem or suggest an improvement.
English and Chinese forms are available. Include your versions, steps, expected behavior, and actual result, ideally with a minimal example you can share publicly.
Do not post keys, credentials, or private project source.

[Current scope](docs/KNOWN_ISSUES.en.md) · [Data and credentials](docs/PRIVACY.en.md) · [Validation](docs/TEST_RESULTS.en.md)

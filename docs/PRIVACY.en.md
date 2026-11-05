# Data and credentials

[简体中文](PRIVACY.md) | **English**

Each user configures their own model service. The package includes no developer keys or developer login state.

DeepSeek keys are entered in the plugin and stored locally using VS Code Secret Storage, rather than written into project source.
Codex uses the user's locally authenticated CLI. Auto selection follows local settings and environment; choose an explicit provider to fix the service used.

AI analysis, questions, explanations, and proposed edits send the relevant question, source excerpts, and necessary context to the selected model service.
Initial analysis reads project structure and bounded implementation excerpts. Provider-side handling depends on the service you choose.
Chat history, analysis caches, and test records are stored locally and are not release assets.
The project provides no shared account, shared API key, or funded quota.

Only attach examples and screenshots you have the right to publish when reporting feedback.
Do not upload keys, account credentials, full private logs, or private project source.

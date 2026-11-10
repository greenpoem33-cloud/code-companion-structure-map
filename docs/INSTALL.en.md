# Installation and configuration

[简体中文](INSTALL.md) | **English**

Validated on Windows. Requires VS Code 1.90+ and Python 3.10+; Python 3.11 or later is recommended.

## Install and trace a return value

1. [Download the 0.27.23 preview VSIX](https://github.com/greenpoem33-cloud/code-companion-structure-map/releases/download/v0.27.23-preview.1/code-companion-structure-map-0.27.23.vsix).
2. In the VS Code Extensions menu, choose **Install from VSIX…**, then reload the window.
3. Open [desktop.py](../demo/desktop.py) and select **Download raw file** and open its folder and the file in VS Code. Select a Python interpreter or set `codeCompanion.pythonCommand` to its full path.
4. Right-click inside `make_launch_request()` and choose **Code Companion: 追踪返回值去向** (Trace return value). Select **Open use site** next to the `open_app` entry to see `return open_app(request)`.

This command reads saved source and runs without model configuration or an initial project analysis.

CLI installation:

```powershell
code --install-extension .\code-companion-structure-map-0.27.23.vsix --force
```

The analysis backend is bundled. No separate html-skill download is required.
If an older `codeCompanion.htmlSkillRoot` or `HTML_SKILL_ROOT` override points to a missing installation, clear that override to use the bundled backend.
Python 3.10 requires `tomli` in the selected environment. Basic analysis on Python 3.11+ uses only the standard library.
Running existing project tests also requires the project's dependencies and pytest. Chain analysis may run existing tests; request “Read source only; do not run tests” when you only want static analysis.

## Optional AI features

For semantic project analysis or AI explanations, configure your own DeepSeek key in Code Companion or install and sign in to the Codex CLI. Then run **Code Companion: 安装自检** (installation check) and choose **Analyze**.

To select DeepSeek explicitly (save the key in the plugin, not in this file):

```json
{
  "codeCompanion.semanticProvider": "deepseek",
  "codeCompanion.editingProvider": "deepseek"
}
```

For Codex, use `codex` for both settings and complete `codex login` in a terminal.
Initial semantic analysis requires an available model service. Usage and quota belong to each user's own account.

New installations store chats in VS Code's persistent extension storage. Existing legacy history stays in place.
Use `codeCompanion.historyDirectory` to specify a different local directory.

Before applying code, a confirmation dialog reports observed changes to definitions, signatures, imports, or call expressions.
Cancelling or closing it keeps the proposal and writes no source. After confirmation, the host checks that the preview and source are still current.
Structure is re-read after applying; previous explanations and call chains may need regeneration.

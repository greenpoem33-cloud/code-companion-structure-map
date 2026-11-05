# Installation and configuration

[简体中文](INSTALL.md) | **English**

Validated on Windows. Requires VS Code 1.90+ and Python 3.10+; Python 3.11 or later is recommended.

1. Download `code-companion-structure-map-0.27.22.vsix` from Releases.
2. In VS Code's Extensions menu, select **Install from VSIX…**, then reload the window.
3. Open a Python project and select its Python interpreter. If the Python extension is unavailable, set `codeCompanion.pythonCommand` to the interpreter's full path.
4. Configure your own AI service. For DeepSeek, expand the DeepSeek configuration area in Code Companion, enter your own API key, and save it. For Codex, install the CLI and sign in with your own account.
5. Run **Code Companion: 安装自检** (installation check), then click **Analyze** once and wait for completion.

CLI installation:

```powershell
code --install-extension .\code-companion-structure-map-0.27.22.vsix --force
```

The analysis backend is bundled. No separate html-skill download is required.
If an older `codeCompanion.htmlSkillRoot` or `HTML_SKILL_ROOT` override points to a missing installation, clear that override to use the bundled backend.
Python 3.10 requires `tomli` in the selected environment. Basic analysis on Python 3.11+ uses only the standard library.
Running existing project tests also requires the project's dependencies and pytest. Chain analysis may run existing tests; request “Read source only; do not run tests” when you only want static analysis.

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

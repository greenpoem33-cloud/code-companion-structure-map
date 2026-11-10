# Code Companion Structure Map

[简体中文](README.md) | **English**

**Where does a Python function's return value go?** Code Companion links the return statement, the caller that receives the value, and its later uses in VS Code. Every step points back to the source.

## Try the Windows desktop demo

Click **Notepad** (记事本) or **Calculator** (计算器) in the simulated Start menu. Follow the launch request as `make_launch_request()` returns it, `on_start_click()` receives it, and `open_app()` consumes it. Select a step to highlight its Python source.

[![Simulated Windows desktop with the source trace for a launch request](demo/preview.jpg)](demo/index.html)

Open the [interactive demo file](demo/index.html), use **Download raw file** to save the HTML, then open it in your browser. The demo uses the included [Python example](demo/desktop.py) and precomputed source evidence. It requires no VS Code installation, Python runtime, or model credentials.

<details>
<summary>Follow the four steps here on GitHub</summary>

1. [Create the request](demo/desktop.py#L7-L8) · `make_launch_request()` returns a dictionary with the app ID and window configuration.
2. [Receive the value](demo/desktop.py#L15-L16) · `on_start_click()` saves the result in `request`.
3. [Pass it to the window handler](demo/desktop.py#L17) · `request` is passed to `open_app()`.
4. [Read the window configuration](demo/desktop.py#L11-L12) · `open_app()` returns `request['window']`.

</details>

## Try it in VS Code

Download the **0.27.22 preview** VSIX from [Releases](https://github.com/greenpoem33-cloud/code-companion-structure-map/releases), choose **Install from VSIX…** in VS Code, and open a Python project. Set up your own DeepSeek key or Codex login, then run the call-chain explanation on a function and open **View return value and uses**. See the [installation guide](docs/INSTALL.en.md).

The preview also includes project maps, source-linked call chains, and a structural change summary before applying edits. Static relationships, test observations, and unresolved links are displayed separately.

## Feedback

First impressions are welcome. **When did you last trace a function's return value, how did you do it, and what took the most time?** [Share feedback](https://github.com/greenpoem33-cloud/code-companion-structure-map/issues/new?template=desktop-feedback.md) · [Report a bug](https://github.com/greenpoem33-cloud/code-companion-structure-map/issues/new/choose)

This public repository distributes preview packages, documentation, and the standalone demo example. The extension development source and internal test projects remain private. No open-source license is granted with this preview. Please keep credentials and private code out of feedback.

[Current scope](docs/KNOWN_ISSUES.en.md) · [Data and credentials](docs/PRIVACY.en.md) · [Validation](docs/TEST_RESULTS.en.md)

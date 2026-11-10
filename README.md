# Code Companion Structure Map

**简体中文** | [English](README.en.md)

**一个 Python 函数返回的数据，接下来去了哪里？** Code Companion 在 VS Code 里把返回语句、调用方接收位置和后续使用连接起来，每一步都能回到源码。

## 30 秒试玩 Windows 桌面

点图打开模拟桌面，选「记事本」或「计算器」，30 秒追到启动请求对应的 Python 源码。

[![模拟 Windows 桌面和启动请求的源码追踪](demo/preview.jpg)](https://greenpoem33-cloud.github.io/code-companion-structure-map/demo/)

**[在线试玩](https://greenpoem33-cloud.github.io/code-companion-structure-map/demo/)** · [下载 HTML 离线版](demo/index.html)（点 **Download raw file**）。

<details>
<summary>直接在 GitHub 查看启动请求的 4 步去向</summary>

1. [创建请求](demo/desktop.py#L7-L8) · `make_launch_request()` 返回包含应用 ID 和窗口配置的字典。
2. [接收结果](demo/desktop.py#L15-L16) · `on_start_click()` 将结果保存在 `request`。
3. [传递请求](demo/desktop.py#L17) · `request` 作为参数传入 `open_app()`。
4. [读取窗口配置](demo/desktop.py#L11-L12) · `open_app()` 读取并返回 `request['window']`。

</details>

## 在 VS Code 里试用

**[下载 0.27.23 预览版 VSIX](https://github.com/greenpoem33-cloud/code-companion-structure-map/releases/download/v0.27.23-preview.1/code-companion-structure-map-0.27.23.vsix)** · [发布说明](https://github.com/greenpoem33-cloud/code-companion-structure-map/releases/tag/v0.27.23-preview.1)

1. 在 VS Code 的扩展菜单选择「从 VSIX 安装」，安装后重载窗口。
2. 打开 [desktop.py](demo/desktop.py)，点 **Download raw file** 保存到本地，打开它所在的文件夹，再打开这个 Python 文件。
3. 在 `make_launch_request()` 函数内右键选择「Code Companion: 追踪返回值去向」，在 `open_app` 的传入记录旁点「查看使用位置」。

这条追踪只读已保存的源码，无需配置模型。环境要求和可选 AI 功能见 [安装与配置](docs/INSTALL.md)。

预览版也支持项目结构图、调用链源码导航和修改前的差异与结构影响确认。静态关系、测试观察与未知关系分别显示。

## 想听你的意见

只看过演示也可以反馈。**你最近一次想追的是哪个函数的返回值？你当时怎么查的，最费时间的是哪一步？** [分享试用感受](https://github.com/greenpoem33-cloud/code-companion-structure-map/issues/new?template=desktop-feedback.md) · [报告 Bug](https://github.com/greenpoem33-cloud/code-companion-structure-map/issues/new/choose)

这是公开预览分发仓库，提供安装包、说明与独立演示样例。插件开发源码及内部测试工程暂未公开，本次预览未授予开源许可证。请勿在反馈里提交凭据或私有源码。

[已知范围](docs/KNOWN_ISSUES.md) · [数据与凭据](docs/PRIVACY.md) · [本版验证](docs/TEST_RESULTS.md)

# Code Companion Structure Map

VS Code 中的 Python 项目结构图、调用链路与 AI 讲解工具。

**当前阶段：预览测试。** 这里提供测试安装包、使用说明和反馈入口，开发源码及测试工程暂未公开。
待版本稳定并收集使用反馈后，再决定后续开源安排。本次未授予开源许可证。

## 下载与使用

前往 [Releases](https://github.com/greenpoem33-cloud/code-companion-structure-map/releases) 下载 **0.27.22 预览测试版**的 VSIX。
在 VS Code 扩展菜单选择“从 VSIX 安装”，重载窗口后打开 Python 项目。
详细步骤见 [安装与配置](docs/INSTALL.md)。

每位用户填写自己的 DeepSeek 密钥，或登录自己的 Codex 账号。
安装包不包含开发者的密钥、登录凭据、个人配置或聊天记录。

## 可以体验什么

- 分析项目结构，在侧栏、编辑区或新窗口查看思维导图。
- 从入口或指定函数查看调用链，点击节点跳转源码或继续讲解。
- 查看叶函数返回结果在调用方中的接收、写入、传参和返回位置。
- 区分静态调用关系、成功用例中的观察和未解析关系。
- 修改方案先看差异；应用前提示结构影响并由你确认，取消不会写入源码。

## 反馈

请通过 [Issues](https://github.com/greenpoem33-cloud/code-companion-structure-map/issues) 提交可复现的问题或改进建议。
提供版本、操作步骤、预期与实际结果，尽量附一个可公开的最小样例。
请勿提交密钥、登录凭据或私有项目源码。

[已知范围](docs/KNOWN_ISSUES.md) · [数据与凭据](docs/PRIVACY.md) · [本版验证](docs/TEST_RESULTS.md)

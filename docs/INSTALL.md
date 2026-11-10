# 安装与配置

已验收环境为 Windows。需要 VS Code 1.90+、Python 3.10+，建议 Python 3.11 或更新版本。

## 安装并试一次返回值追踪

1. [下载 0.27.24 预览版 VSIX](https://github.com/greenpoem33-cloud/code-companion-structure-map/releases/download/v0.27.24-preview.1/code-companion-structure-map-0.27.24.vsix)。
2. 在 VS Code 的扩展菜单选择「从 VSIX 安装」，安装后重载窗口。
3. 打开 [desktop.py](../demo/desktop.py)，点 **Download raw file** 保存到本地，在 VS Code 中打开它所在的文件夹和该文件。选择 Python 解释器，或将 `codeCompanion.pythonCommand` 设置为解释器的完整路径。
4. 把光标放进 `make_launch_request()`，右键选择「Code Companion: 追踪返回值去向」。在 `open_app` 的传入记录旁点「查看使用位置」，查看 `return open_app(request)`。

此命令只读已保存的源码，无需配置模型，也无需先运行「分析」。

命令行安装等效于：

```powershell
code --install-extension .\code-companion-structure-map-0.27.24.vsix --force
```

分析后端已包含在包中，首次使用无需额外下载 html-skill。
如果旧的 `codeCompanion.htmlSkillRoot` 或 `HTML_SKILL_ROOT` 指向失效目录，请清空该覆盖设置后重试。
Python 3.10 需要在所选解释器中安装 `tomli`；3.11+ 的基础分析仅使用标准库。
运行项目测试需要项目自身依赖和 pytest。链路分析可能运行已有用例；只想读源码时，可明确输入“只读取源码，不运行测试”。

## 可选 AI 功能

如需项目语义分析或 AI 讲解，可在插件内配置自己的 DeepSeek 密钥，或安装 Codex CLI 并登录。配置后可运行「Code Companion: 安装自检」，再点「分析」。

显式选择 DeepSeek 的设置示例（密钥不写入配置文件）：

```json
{
  "codeCompanion.semanticProvider": "deepseek",
  "codeCompanion.editingProvider": "deepseek"
}
```

使用 Codex 时，将两个值改为 `codex`，在终端完成 `codex login`。
首次分析需要可用模型服务，各用户的服务费用和配额由自己的账号承担。

新安装的聊天保存在 VS Code 的插件持久存储目录，更新插件保留记录。
有旧历史目录的用户继续原位使用，也可通过 `codeCompanion.historyDirectory` 指定位置。

应用修改前会显示已确认的定义、签名、导入或调用表达式变化；确认后再次核对预览和源码。
取消或关闭确认框会保留方案，不写入源码。修改后旧说明和链路可能需要重新生成。

# AI Development Workflow

[简体中文](#中文说明) | [English](#english)

A reusable agent skill for software development with **GitHub Issues, branches, pull requests, GitHub Actions, and Vercel previews**. Its current workflow is interactive and keeps shared project conventions suitable for future background agents.

## 中文说明

### 功能

`ai-development-workflow` 用于指导具备代码访问和执行工具的 AI 助手完成软件开发任务，涵盖仓库检查、需求分析、实现与测试、创建或更新 Pull Request、核查 GitHub Actions，以及检查 Vercel 预览。它会区分已经执行的检查和无法执行的检查，避免提供未经核实的预览链接。

适用场景：新增功能、修复问题、继续已有 PR、检查 CI 失败、对用户界面进行迭代，以及将项目规范交给其他开发 Agent。

### 获取与安装

1. 在本仓库的 **Code → Download ZIP** 下载源码，或运行：

   ```bash
   git clone https://github.com/harrissherlock/ai-development-workflow.git
   ```

2. 将包含 `SKILL.md`、`references/` 和 `templates/` 的目录放入目标 AI 编程工具所支持的 Skill 目录中，并按照该工具的说明启用。
3. 在 ChatGPT 等产品中，也可使用产品提供的 Skill 安装功能。不同产品的安装方式和外部工具访问权限可能不同；仅复制 GitHub 地址不会自动完成安装。
4. 连接具有相应权限的 GitHub 仓库，配置项目自己的 GitHub Actions 和 Vercel（如果需要在线预览）。

### 调用示例

> 使用 `ai-development-workflow`，给 `owner/repo` 增加日历视图，支持月视图、周视图、拖动修改任务日期，并与现有任务数据同步。运行相关测试，创建 PR，并提供已核实的 Vercel 预览链接。

后续可以继续说：

> 继续处理原 PR。把任务卡片改成紧凑布局，周视图增加时间轴。读取最新代码后修改并重新测试。

### 目录

```text
.
├── SKILL.md                         # Skill 的主要指令
├── references/                     # 开发、测试、预览及安全说明
├── templates/                      # AGENTS.md、Issue、PR、CI 示例
├── docs/guide.html                 # 中文功能介绍与使用说明
├── docs/architecture-options.md    # 两种开发方案的背景资料
├── scripts/validate_skill.py       # 本地结构检查
└── .github/workflows/validate.yml  # 自动检查 Skill 文件
```

### 当前范围与未来扩展

当前以 ChatGPT Work 或类似的交互式编程助手作为开发执行者，使用现有 GitHub 和 Vercel 工具；不要求自行部署 MCP Server。未来可通过共同的 `AGENTS.md`、Issues、PR、测试命令和提交 SHA 与 OpenHands 等后台 Agent 协作。自动领取 Issue、后台执行及自动修复 CI 失败需要额外的运行环境和调度配置。

使用说明：[查看中文 HTML 指南](docs/guide.html)。方案设计背景：[查看完整方案比较](docs/architecture-options.md)。

### 开发与验证

```bash
python scripts/validate_skill.py
```

欢迎通过 Issues 和 Pull Requests 提交建议或改进。版权 © 2026 harock。许可证：[MIT](LICENSE)。

## English

### What it does

A reusable instruction package for coding agents that can inspect repositories, implement changes, run appropriate checks, create or update PRs, examine GitHub Actions for the current commit, and verify real Vercel previews when available.

### Install

Clone or download this repository, then place its contents in the Skill directory supported by your agent. Follow the target agent's installation instructions. GitHub and Vercel capabilities depend on the tools and permissions actually connected to that agent.

### Example

> Use `ai-development-workflow` in `owner/repo` to build a month/week calendar, persist task date changes, run the relevant tests, open a PR, and report the verified Vercel preview URL if one exists.

See [SKILL.md](SKILL.md), the [Chinese user guide](docs/guide.html), and [the architecture comparison](docs/architecture-options.md). The workflow is currently interactive; background automation requires a separately deployed agent and scheduler.

### License

Copyright © 2026 harock. Licensed under MIT. See [LICENSE](LICENSE).

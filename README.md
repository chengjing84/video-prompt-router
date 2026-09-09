# 视频生成提示词技能包

本仓库收录 `video-prompt-router` 路由入口，以及它依赖的 MiniMax H3、打斗、动漫 PV 和完整 Seedance 2.0 技能包。路由入口会按平台和任务选择专项技能；具体提示词规则、参考资料、示例和校验脚本都随仓库提供。

## 收录内容

| 模块 | 入口 | 技能入口数 | 原始文件数 |
| --- | --- | ---: | ---: |
| 视频提示词路由 | [SKILL.md](SKILL.md) | 1 | 1 |
| MiniMax H3 通用提示词及高密度打斗 | [h3-prompt-writing/SKILL.md](h3-prompt-writing/SKILL.md) | 2 | 7 |
| 动漫 PV | [anime-pv-i2va-generator/SKILL.md](anime-pv-i2va-generator/SKILL.md) | 1 | 4 |
| Seedance 2.0 完整技能包 | [seedance-20/SKILL.md](seedance-20/SKILL.md) | 29 | 269 |
| **合计** | | **33** | **281** |

Seedance 包含 28 个专项技能，涵盖提示词、长序列、续写、镜头、角色、动作、灯光、声音、特效、视觉风格、故障排查和多语言表达。它的参考文档、示例、脚本、测试、素材和许可证均保留在原目录中。

本次整合保留上述 281 个原始文件的内容和内部目录结构。根目录的 README、文件清单和校验脚本是整合时新增的说明与工具。

## 安装到本地技能目录

下载整个仓库，或运行：

```sh
git clone https://github.com/chengjing84/video-prompt-router.git
```

将下列四项放入你的技能根目录。默认位置是 `~/.codex/skills`；如果设置了 `CODEX_HOME`，则使用该目录下的 `skills` 文件夹。

| 仓库内容 | 技能根目录中的目标 |
| --- | --- |
| 根目录 `SKILL.md` | `video-prompt-router/SKILL.md` |
| 整个 `h3-prompt-writing/` 目录 | `h3-prompt-writing/` |
| 整个 `anime-pv-i2va-generator/` 目录 | `anime-pv-i2va-generator/` |
| 整个 `seedance-20/` 目录 | `seedance-20/` |

保留子目录结构，尤其是各包的 `references/` 和 Seedance 的 `skills/`。若目标目录已有你修改过的版本，先备份再替换。安装后重新打开 Codex，让技能列表重新加载。

也可以直接让支持读取本地文件的代理从本仓库的 `SKILL.md` 开始，并依据下表读取所选专项技能。

## 路由入口直接引用的 12 个专项技能

| 技能名 | 仓库内文件 |
| --- | --- |
| `high-density-fight-prompt` | [打斗入口](h3-prompt-writing/references/fight/SKILL.md) |
| `anime-pv-i2va-generator` | [动漫 PV 入口](anime-pv-i2va-generator/SKILL.md) |
| `h3-prompt-writing` | [H3 通用入口](h3-prompt-writing/SKILL.md) |
| `seedance-prompt` | [提示词](seedance-20/skills/seedance-prompt/SKILL.md) |
| `seedance-sequence` | [长序列](seedance-20/skills/seedance-sequence/SKILL.md) |
| `seedance-continuation` | [续写](seedance-20/skills/seedance-continuation/SKILL.md) |
| `seedance-audio` | [声音](seedance-20/skills/seedance-audio/SKILL.md) |
| `seedance-camera` | [镜头](seedance-20/skills/seedance-camera/SKILL.md) |
| `seedance-characters` | [角色](seedance-20/skills/seedance-characters/SKILL.md) |
| `seedance-motion` | [动作](seedance-20/skills/seedance-motion/SKILL.md) |
| `seedance-filter` | [提示词拒绝排查](seedance-20/skills/seedance-filter/SKILL.md) |
| `seedance-troubleshoot` | [生成故障排查](seedance-20/skills/seedance-troubleshoot/SKILL.md) |

使用示例：

```text
使用 video-prompt-router，帮我写一条 Seedance 2.0 的 10 秒视频提示词：
雨夜街头，一位撑伞的人停下脚步回头，镜头缓慢推近，16:9。
```

这些技能用于编写和检查视频生成提示词。实际生成视频需要在对应平台使用提示词及参考素材。

## 完整性校验

[BUNDLE-MANIFEST.json](BUNDLE-MANIFEST.json) 记录每个原始文件的相对路径、大小、SHA-256 和 Git blob SHA，以及全部技能入口。使用 Python 3 在仓库目录运行：

```sh
python scripts/verify_bundle.py
```

脚本会检查 281 个原始文件的字节内容、额外文件、技能入口和路由依赖。校验通过表示与本次打包快照一致；视频生成质量仍取决于实际输入和生成平台。

## 来源和许可

本仓库整合自本地安装的同名技能包。Seedance 包保留原项目 [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) 的来源说明和 [MIT 许可证](seedance-20/LICENSE)，字体许可见 [OFL.txt](seedance-20/assets/fonts/OFL.txt)。本仓库未替其他模块新增许可声明，各模块以自身附带的声明为准。

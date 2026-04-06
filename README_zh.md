# PromptChan AI 图像生成器

> 🎨 支持多种艺术风格、姿势和滤镜的高级 AI 图像生成平台

**免费试用：** 新用户完成简单任务即可获得 **100 免费 Gems**！

[English](README.md) | [日本語](README_ja.md)

## 📋 目录

- [快速开始](#-快速开始)
- [注册与 API Key](#-注册与-api-key)
- [使用方法](#-使用方法)
- [可用风格](#-可用风格)
- [可用姿势](#-可用姿势)
- [可用滤镜](#-可用滤镜)
- [费用说明](#-费用说明)
- [示例](#-示例)
- [故障排除](#-故障排除)
- [API 参考](#-api-参考)

---

## 🚀 快速开始

### 环境要求

```bash
pip install requests
```

### 基础用法

生成图片：

```bash
python scripts/promptchan_generate.py \
  --prompt "cute girl, school uniform, city at night, long hair" \
  --api-key "your-api-key-here" \
  --output images/output.png
```

### 查询剩余 Gems

```bash
python scripts/promptchan_status.py --api-key "your-api-key-here"
```

---

## 📝 注册与 API Key

### 1️⃣ 注册账号

**重要：** 使用下方专属注册链接可获得免费起始 Gems！

👉 **注册：** https://promptchan.com/m/YCYAZJj7uKQcbpP1wMcFuzA5zIY2/3hov

### 2️⃣ 生成 API Key

1. 登录后进入设置：**https://promptchan.com/settings**
2. 滚动到 **API Key** 部分
3. 点击 **"Generate"** 生成密钥
4. 复制并保存 API Key（仅显示一次！）

### 3️⃣ 充值 Gems

- API 使用 **Gems** 作为货币
- **1 Gem = 1 张图片**
- **新用户：完成简单任务即可获得 100 免费 Gems！**
- 充值：https://promptchan.com/pricing

---

## 💻 使用方法

### 命令行参数

#### 必需参数
| 参数 | 说明 |
|------|------|
| `--prompt`, `-p` | 描述期望图像的正向提示词 |
| `--api-key` | 您的 PromptChan API Key |

#### 可选参数

**风格设置：**
| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--style`, `-s` | Cinematic | 艺术风格（见 [风格列表](#-可用风格)） |
| `--poses` | Default | 角色姿势（见 [姿势列表](#-可用姿势)） |
| `--filter`, `-f` | Default | 滤镜效果（见 [滤镜列表](#-可用滤镜)） |

**质量设置：**
| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--quality`, `-q` | Ultra | 质量等级（Ultra/Extreme/Max） |
| `--detail` | 0 | 细节级别（-2 到 2） |
| `--creativity`, `-c` | 50 | 创意程度（30/50/70） |

**其他参数：**
| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--image_size` | 512x768 | 图像尺寸（512x512/512x768/768x512） |
| `--seed` | -1 | 随机种子（-1 为随机） |
| `--negative-prompt`, `-n` | - | 负向提示词 |
| `--restore_faces` | false | 人脸修复（+1 Gem，仅写实风格） |
| `--output`, `-o` | 自动 | 输出文件路径 |

### 完整示例

```bash
python scripts/promptchan_generate.py \
  --prompt "beautiful girl, long hair, sunset, detailed eyes, masterpiece" \
  --negative-prompt "ugly, deformed, noisy, blurry" \
  --style "Anime" \
  --poses "Default" \
  --filter "Cinematic" \
  --detail 1 \
  --creativity 50 \
  --quality "Ultra" \
  --image_size "512x768" \
  --seed 12345 \
  --api-key "your-api-key-here" \
  --output images/anime-girl.png
```

---

## 🎨 可用风格

| 风格 | 说明 |
|------|------|
| Cinematic | 电影风格渲染 |
| Anime | 日式动画风格 |
| Hyperreal | 照片级写实 |
| Hyperanime | 增强动漫风格 |
| K-Pop | 韩国流行风格 |
| Fur | 兽人艺术风格 |
| Furtoon | 兽人卡通 |
| Render XL+ | 增强 3D 渲染 |
| Illustration XL+ | 增强插画 |
| Anime XL | 大型动漫模型 |
| Anime XL+ | 增强大型动漫 |
| Hardcore XL | 强烈风格 |
| Cinematic XL | 大型电影模型 |
| Photo XL+ | 增强照片风格 |
| Hyperreal XL+ | 增强超写实 |

**列出所有风格：**
```bash
python scripts/promptchan_styles.py --type styles
```

---

## 🧍 可用姿势

超过 100 种姿势选项，适用于各种场景和构图需求：

**常用姿势：**
- Default - 标准站姿
- Kneeling - 跪姿
- Sitting - 坐姿
- Standing - 站姿
- Lying Down - 躺姿
- Cuddling - 拥抱姿势
- Smiling - 微笑表情
- Looking Up - 仰视
- From Behind - 背部视角
- Close-up - 特写镜头

**高级姿势（Pro 功能）：**
- 多种亲密互动姿势
- 动态动作姿势
- 多角色互动姿势

> 📌 **注意：** 共 116+ 种姿势可用。完整列表见 [SKILL.md](SKILL.md)。部分姿势需要 Pro 订阅。

---

## 🌈 可用滤镜

| 滤镜 | 说明 |
|------|------|
| Default | 无滤镜 |
| Cyberpunk | 霓虹未来风 |
| VHS | 复古录像带 |
| Manga | 漫画风格 |
| Flash | 相机闪光灯 |
| Analog | 胶片相机效果 |
| Professional | 工作室品质 |
| Cinematic | 电影级 |
| Studio | 专业灯光 |
| Polaroid | 即时照片 |
| Vintage | 复古做旧 |

**列出所有滤镜：**
```bash
python scripts/promptchan_styles.py --type filters
```

---

## 💰 费用说明

| 项目 | 费用 |
|------|------|
| 基础生成 | 1 Gem/张 |
| Extreme 质量 | +1 Gem |
| Max 质量 | +2 Gem |
| 人脸修复 | +1 Gem（仅写实风格） |
| 高峰时段 | +0.25 Gem（可能收取） |

**注意：** 1 Gem = 1 张图片

---

## 📋 示例

### 1. 动漫风格女孩

```bash
python scripts/promptchan_generate.py \
  --prompt "cute anime girl, long pink hair, school uniform, cherry blossoms" \
  --style "Anime XL+" \
  --poses "Smiling" \
  --filter "Manga" \
  --creativity 50 \
  --quality "Ultra" \
  --api-key "your-api-key" \
  --output images/anime-girl.png
```

### 2. 写实人像

```bash
python scripts/promptchan_generate.py \
  --prompt "beautiful korean woman, long black hair, elegant dress, studio lighting" \
  --style "Hyperreal XL+" \
  --poses "Sitting" \
  --filter "Professional" \
  --detail 1 \
  --restore_faces \
  --api-key "your-api-key" \
  --output images/portrait.png
```

### 3. 赛博朋克风格

```bash
python scripts/promptchan_generate.py \
  --prompt "cyberpunk girl, neon lights, futuristic city, night" \
  --style "Cinematic XL" \
  --filter "Cyberpunk" \
  --creativity 70 \
  --api-key "your-api-key" \
  --output images/cyberpunk.png
```

### 4. 批量生成

```bash
for seed in 1 2 3 4 5; do
  python scripts/promptchan_generate.py \
    --prompt "beautiful girl, sunset" \
    --style "Anime" \
    --seed $seed \
    --api-key "your-api-key" \
    --output images/batch_$seed.png
done
```

---

## 🔧 故障排除

### 错误：API Key 无效
- 确认 API Key 复制正确
- 检查是否有多余空格
- 在设置中重新生成 API Key

### 错误：Gems 不足
- 在 https://promptchan.com/pricing 充值
- 检查是否已领取免费起始 Gems

### 错误：请求超时
- 高峰时段可能导致延迟
- 检查网络连接
- 稍后重试

### 质量不佳
- 增加 `--detail` 参数（1 或 2）
- 使用 `--quality "Extreme"` 或 `"Max"`
- 优化提示词，增加细节描述

---

## 📚 脚本说明

| 脚本 | 说明 |
|------|------|
| `promptchan_generate.py` | 生成图像 |
| `promptchan_status.py` | 查询余额和状态 |
| `promptchan_styles.py` | 列出可用风格/姿势/滤镜 |

---

## ⚠️ 重要提示

1. **API Key 安全**：请妥善保管 API Key，不要提交到版本控制
2. **内容规范**：不要生成违法内容（有封号风险）
3. **费用控制**：生成前确保有足够的 Gems
4. **高峰时段**：可能收取额外费用（0.25 Gem/张）
5. **人脸修复**：仅用于写实风格，动漫风格不需要

---

## 🔗 链接

- **注册**：https://promptchan.com/m/YCYAZJj7uKQcbpP1wMcFuzA5zIY2/3hov
- **官方文档**：https://promptchan.com/docs
- **API 设置**：https://promptchan.com/settings
- **价格**：https://promptchan.com/pricing
- **创作**：https://promptchan.com/create

---

## 📄 许可证

MIT License

---

## 🤝 贡献

欢迎贡献！提交 PR 前请阅读我们的贡献指南。

---

## 📞 支持

- **Discord**：[加入服务器](https://discord.gg/promptchan)
- **邮箱**：support@promptchan.com
- **问题**：[GitHub Issues](https://github.com/promptchan/api/issues)

---

## 🤖 在 OpenClaw 中使用

本技能可集成到 OpenClaw 中，实现无缝的 AI 图像生成。

### 方式一：自然语言提示词

直接在聊天中描述想要的图片：

```
生成一张图片：可爱的动漫女孩，粉色长发，校服，樱花
```

```
创建一张赛博朋克风格的图片：霓虹灯，未来城市，夜景
```

### 方式二：在 openclaw.json 中配置

在 `openclaw.json` 中添加技能配置：

```json
{
  "skills": {
    "promptchan-for-openclaw": {
      "enabled": true,
      "apiKey": "你的 API Key",
      "defaultStyle": "Anime",
      "defaultQuality": "Ultra"
    }
  }
}
```

然后使用简短命令：

```
/pc 生成一张动漫女孩，粉色头发，微笑
```

```
/promptchan 赛博朋克风格，霓虹灯，未来城市
```

### 方式三：使用 sessions_spawn

通过代码调用技能：

```python
from openclaw import sessions_spawn

sessions_spawn(
    task="使用 PromptChan API 生成图片：可爱的动漫女孩，校服，樱花",
    runtime="subagent",
    mode="run"
)
```

### 方式四：配置为 OpenClaw 工具

在 `openclaw.json` 的 tools 部分添加：

```json
{
  "tools": {
    "promptchan": {
      "type": "script",
      "path": "skills/promptchan-for-openclaw/scripts/promptchan_generate.py",
      "description": "使用 PromptChan AI 生成图片",
      "parameters": {
        "prompt": {"type": "string", "required": true},
        "style": {"type": "string", "default": "Anime"},
        "quality": {"type": "string", "default": "Ultra"}
      }
    }
  }
}
```

然后在聊天中使用：

```
使用 promptchan 工具生成：可爱的女孩，校服，城市夜景
```

### 提示词编写技巧

**好的提示词：**
- 具体描述：`可爱的动漫女孩，粉色长发，蓝色眼睛，校服，樱花，微笑`
- 包含质量词：`杰作，最佳质量，精致的眼睛，8k`
- 描述光线和氛围：`日落，电影灯光，情绪化氛围`

**避免：**
- 太模糊：`一个女孩`
- 矛盾描述：`白天和夜晚的混合`
- 太复杂：一个提示词包含太多元素

### OpenClaw 工作流程示例

1. 用户：`生成一张粉色头发的动漫女孩，穿校服`
2. OpenClaw 调用 `promptchan_generate.py` 脚本
3. 脚本发送请求到 PromptChan API
4. API 返回生成的图片
5. OpenClaw 向用户展示图片

更多详情请参阅 [OpenClaw 文档](https://docs.openclaw.ai)。

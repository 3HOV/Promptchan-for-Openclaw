# PromptChan AI 图像生成器

> 🎨 支持多种艺术风格和滤镜的高级 AI 图像生成平台

**免费试用：** 新用户完成简单任务即可获得 **100 免费 Gems**！

[English](README.md) | [日本語](README_ja.md)
 
## 🎯 概述

PromptChan AI 图像生成器是一个强大的工具，可生成各种艺术风格的高质量 AI 图像。非常适合需要快速专业图像生成的艺术家、内容创作者和开发者。

## 📋 目录

- [快速开始](#-快速开始)
- [注册与 API Key](#-注册与-api-key)
- [使用方法](#-使用方法)
- [可用风格](#-可用风格)
- [可用滤镜](#-可用滤镜)
- [费用说明](#-费用说明)
- [示例](#-示例)
- [故障排除](#-故障排除)
- [在 OpenClaw 中使用](#-在-openclaw-中使用)

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

### 1️⃣ 创建账号

**重要：** 使用下方专属注册链接可获得免费起始 Gems！

👉 **注册：** [https://promptchan.com/](https://promptchan.com/m/YCYAZJj7uKQcbpP1wMcFuzA5zIY2/3hov)

### 2️⃣ 生成 API Key

1. 登录后进入设置：https://promptchan.com/settings
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
| `--style`, `-s` | Cinematic | 艺术风格（见 [可用风格](#-可用风格)） |
| `--filter`, `-f` | Default | 滤镜效果（见 [可用滤镜](#-可用滤镜)） |

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
| `--output`, `-o` | 自动 | 输出文件路径 |

### 完整示例

```bash
python scripts/promptchan_generate.py \
  --prompt "beautiful girl, long hair, sunset, detailed eyes, masterpiece" \
  --negative-prompt "ugly, deformed, noisy, blurry" \
  --style "Anime" \
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

15+ 种专业艺术风格，适用于不同场景：

**常用风格：**
- Cinematic - 电影风格渲染
- Anime - 日式动画风格
- Hyperreal - 照片级写实
- Hyperanime - 增强动漫风格
- K-Pop - 韩国流行风格
- Render XL+ - 增强 3D 渲染
- Illustration XL+ - 专业插画
- Photo XL+ - 增强照片风格

**列出所有风格：**
```bash
python scripts/promptchan_styles.py --type styles
```

---

## 🌈 可用滤镜

11 种专业滤镜，适用于不同氛围：

- Default - 无滤镜
- Cyberpunk - 霓虹未来风
- VHS - 复古录像带
- Manga - 漫画风格
- Flash - 相机闪光灯
- Analog - 胶片相机效果
- Professional - 工作室品质
- Cinematic - 电影级
- Studio - 专业灯光
- Polaroid - 即时照片
- Vintage - 复古做旧

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
| 高峰时段 | 可能 +0.25 Gem |

**注意：** 1 Gem = 1 张图片

---

## 📋 示例

### 1. 动漫风格角色

```bash
python scripts/promptchan_generate.py \
  --prompt "cute anime girl, long pink hair, school uniform, cherry blossoms" \
  --style "Anime XL+" \
  --filter "Manga" \
  --creativity 50 \
  --quality "Ultra" \
  --api-key "your-api-key" \
  --output images/anime-girl.png
```

### 2. 专业人像

```bash
python scripts/promptchan_generate.py \
  --prompt "beautiful woman, long black hair, elegant dress, studio lighting" \
  --style "Hyperreal XL+" \
  --filter "Professional" \
  --detail 1 \
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

## 🤖 在 OpenClaw 中使用

本技能可集成到 OpenClaw 中，实现无缝的 AI 图像生成。

### 方式一：自然语言提示词

直接在聊天中描述想要的图片：

```
生成一张图片：可爱的动漫女孩，粉色长发，校服，樱花
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

### 提示词编写技巧

**好的提示词：**
- 具体描述：`可爱的动漫女孩，粉色长发，蓝色眼睛，校服，樱花，微笑`
- 包含质量词：`杰作，最佳质量，精致的眼睛，8k`
- 描述光线和氛围：`日落，电影灯光，情绪化氛围`

**避免：**
- 太模糊：`一个女孩`
- 矛盾描述：`白天和夜晚的混合`
- 太复杂：一个提示词包含太多元素

---

## 🔗 链接

- **注册：** [https://promptchan.com/](https://promptchan.com/m/YCYAZJj7uKQcbpP1wMcFuzA5zIY2/3hov)
- **官方文档：** https://promptchan.com/docs
- **API 设置：** https://promptchan.com/settings
- **价格：** https://promptchan.com/pricing

---

## 📄 许可证

MIT License

---

## 🤝 贡献

详见 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📞 支持

- **Discord：** [加入服务器](https://discord.gg/promptchan)
- **邮箱：** support@promptchan.com
- **问题：** [GitHub Issues](https://github.com/promptchan/api/issues)

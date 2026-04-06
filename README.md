# PromptChan AI Image Generator

> 🎨 Advanced AI image generation platform with multiple art styles and filters

**Free Trial:** New users receive **100 free Gems** after completing simple tasks!

[中文文档](README_zh.md) | [日本語ドキュメント](README_ja.md)

## 🎯 Overview

PromptChan AI Image Generator is a powerful tool for creating high-quality AI-generated images with various artistic styles. Perfect for artists, content creators, and developers who need fast, professional image generation.

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Registration & API Key](#-registration--api-key)
- [Usage](#-usage)
- [Available Styles](#-available-styles)
- [Available Filters](#-available-filters)
- [Pricing](#-pricing)
- [Examples](#-examples)
- [Troubleshooting](#-troubleshooting)
- [Using with OpenClaw](#-using-with-openclaw)
- 
---

## 🚀 Quick Start

### Prerequisites

```bash
pip install requests
```

### Basic Usage

Generate an image:

```bash
python scripts/promptchan_generate.py \
  --prompt "cute girl, school uniform, city at night, long hair" \
  --api-key "your-api-key-here" \
  --output images/output.png
```

### Check Remaining Gems

```bash
python scripts/promptchan_status.py --api-key "your-api-key-here"
```

---

## 📝 Registration & API Key

### 1️⃣ Create Account

**Important:** Use the exclusive registration link below for free starter Gems!

👉 **Register:** [https://promptchan.com/](https://promptchan.com/m/YCYAZJj7uKQcbpP1wMcFuzA5zIY2/3hov)

### 2️⃣ Generate API Key

1. Login and go to Settings: https://promptchan.com/settings
2. Scroll to **API Key** section
3. Click **"Generate"** to create your key
4. Copy and save your API Key (shown only once!)

### 3️⃣ Top Up Gems

- API uses **Gems** as currency
- **1 Gem = 1 Image**
- **New users: Complete simple tasks to get 100 free Gems!**
- Top up: https://promptchan.com/pricing

---

## 💻 Usage

### Command Line Arguments

#### Required
| Argument | Description |
|----------|-------------|
| `--prompt`, `-p` | Text prompt describing the desired image |
| `--api-key` | Your PromptChan API Key |

#### Optional

**Style Settings:**
| Argument | Default | Description |
|----------|---------|-------------|
| `--style`, `-s` | Cinematic | Art style (see [Available Styles](#-available-styles)) |
| `--filter`, `-f` | Default | Filter effect (see [Available Filters](#-available-filters)) |

**Quality Settings:**
| Argument | Default | Description |
|----------|---------|-------------|
| `--quality`, `-q` | Ultra | Quality level (Ultra/Extreme/Max) |
| `--detail` | 0 | Detail level (-2 to 2) |
| `--creativity`, `-c` | 50 | Creativity level (30/50/70) |

**Other:**
| Argument | Default | Description |
|----------|---------|-------------|
| `--image_size` | 512x768 | Image size (512x512/512x768/768x512) |
| `--seed` | -1 | Random seed (-1 for random) |
| `--negative-prompt`, `-n` | - | Negative prompt |
| `--output`, `-o` | Auto | Output file path |

### Full Example

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

## 🎨 Available Styles

15+ professional art styles for different use cases:

**Popular Styles:**
- Cinematic - Movie-style rendering
- Anime - Japanese animation style
- Hyperreal - Photorealistic images
- Hyperanime - Enhanced anime style
- K-Pop - Korean pop aesthetic
- Render XL+ - Enhanced 3D rendering
- Illustration XL+ - Professional illustration
- Photo XL+ - Enhanced photography style

**List all styles:**
```bash
python scripts/promptchan_styles.py --type styles
```

---

## 🌈 Available Filters

11 professional filters for different moods:

- Default - No filter
- Cyberpunk - Neon futuristic
- VHS - Retro videotape
- Manga - Comic book style
- Flash - Camera flash
- Analog - Film camera look
- Professional - Studio quality
- Cinematic - Movie grade
- Studio - Professional lighting
- Polaroid - Instant photo
- Vintage - Retro aged

**List all filters:**
```bash
python scripts/promptchan_styles.py --type filters
```

---

## 💰 Pricing

| Item | Cost |
|------|------|
| Base generation | 1 Gem/image |
| Extreme quality | +1 Gem |
| Max quality | +2 Gem |
| Face restoration | +1 Gem (realistic styles only) |
| Peak hours | +0.25 Gem (may apply) |

**Note:** 1 Gem = 1 Image

---

## 📋 Examples

### 1. Anime Style Character

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

### 2. Professional Portrait

```bash
python scripts/promptchan_generate.py \
  --prompt "beautiful woman, long black hair, elegant dress, studio lighting" \
  --style "Hyperreal XL+" \
  --filter "Professional" \
  --detail 1 \
  --api-key "your-api-key" \
  --output images/portrait.png
```

### 3. Cyberpunk Style

```bash
python scripts/promptchan_generate.py \
  --prompt "cyberpunk girl, neon lights, futuristic city, night" \
  --style "Cinematic XL" \
  --filter "Cyberpunk" \
  --creativity 70 \
  --api-key "your-api-key" \
  --output images/cyberpunk.png
```

### 4. Batch Generation

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

## 🔧 Troubleshooting

### Error: Invalid API Key
- Verify API Key is copied correctly
- Check for extra spaces
- Regenerate API Key in settings

### Error: Insufficient Gems
- Top up at https://promptchan.com/pricing
- Check if free starter Gems are claimed

### Error: Request Timeout
- Peak hours may cause delays
- Check network connection
- Retry later

### Poor Quality Results
- Increase `--detail` parameter (1 or 2)
- Use `--quality "Extreme"` or `"Max"`
- Improve prompt with more details

---

## 🤖 Using with OpenClaw

This skill can be integrated with OpenClaw for seamless AI image generation.

### Method 1: Natural Language Prompts

Simply describe the image you want in chat:

```
Generate an image: cute anime girl, long pink hair, school uniform, cherry blossoms
```

### Method 2: Configure in openclaw.json

Add skill configuration to `openclaw.json`:

```json
{
  "skills": {
    "promptchan-for-openclaw": {
      "enabled": true,
      "apiKey": "your-api-key-here",
      "defaultStyle": "Anime",
      "defaultQuality": "Ultra"
    }
  }
}
```

### Prompt Writing Tips

**Good prompts:**
- Be specific: `cute anime girl, long pink hair, blue eyes, school uniform, cherry blossoms, smiling`
- Include quality terms: `masterpiece, best quality, detailed eyes, 8k`
- Describe lighting and atmosphere: `sunset, cinematic lighting, moody atmosphere`

**Avoid:**
- Too vague: `a girl`
- Contradictory: `day and night mixed`
- Too complex: too many elements in one prompt

---

## 🔗 Links

- **Register:** [https://promptchan.com/](https://promptchan.com/m/YCYAZJj7uKQcbpP1wMcFuzA5zIY2/3hov)
- **Official Docs:** https://promptchan.com/docs
- **API Settings:** https://promptchan.com/settings
- **Pricing:** https://promptchan.com/pricing

---

## 📄 License

MIT License

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute.

---

## 📞 Support

- **Discord:** [Join our server](https://discord.gg/promptchan)
- **Email:** support@promptchan.com
- **Issues:** [GitHub Issues](https://github.com/promptchan/api/issues)

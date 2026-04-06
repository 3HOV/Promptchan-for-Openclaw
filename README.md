# PromptChan AI Image Generator

> 🎨 Advanced AI image generation platform with multiple art styles, poses, and filters

**Free Trial:** New users receive **100 free Gems** after completing simple tasks!

[中文文档](README_zh.md) | [日本語ドキュメント](README_ja.md)

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Registration & API Key](#-registration--api-key)
- [Usage](#-usage)
- [Available Styles](#-available-styles)
- [Available Poses](#-available-poses)
- [Available Filters](#-available-filters)
- [Pricing](#-pricing)
- [Examples](#-examples)
- [Troubleshooting](#-troubleshooting)
- [API Reference](#-api-reference)

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

👉 **Register:** [Click here to register](https://promptchan.com/register)

### 2️⃣ Generate API Key

1. Login and go to Settings: **https://promptchan.com/settings**
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
| `--style`, `-s` | Cinematic | Art style (see [Styles](#-available-styles)) |
| `--poses` | Default | Character pose (see [Poses](#-available-poses)) |
| `--filter`, `-f` | Default | Filter effect (see [Filters](#-available-filters)) |

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
| `--restore_faces` | false | Face restoration (+1 Gem, realistic only) |
| `--output`, `-o` | auto | Output file path |

### Full Example

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

## 🎨 Available Styles

| Style | Description |
|-------|-------------|
| Cinematic | Movie-style rendering |
| Anime | Japanese animation style |
| Hyperreal | Photorealistic |
| Hyperanime | Enhanced anime |
| K-Pop | Korean pop style |
| Fur | Furry art style |
| Furtoon | Furry cartoon |
| Render XL+ | Enhanced 3D render |
| Illustration XL+ | Enhanced illustration |
| Anime XL | Large anime model |
| Anime XL+ | Enhanced large anime |
| Hardcore XL | Intense style |
| Cinematic XL | Large cinematic model |
| Photo XL+ | Enhanced photo style |
| Hyperreal XL+ | Enhanced hyperreal |

**List all styles:**
```bash
python scripts/promptchan_styles.py --type styles
```

---

## 🧍 Available Poses

Over 100 pose options for various scenarios and compositions:

**Common poses:**
- Default - Neutral standing pose
- Kneeling - Kneeling position
- Sitting - Seated position
- Standing - Standing pose
- Lying Down - Reclining pose
- Cuddling - Embrace position
- Smiling - Happy expression
- Looking Up - Upward gaze
- From Behind - Rear view
- Close-up - Portrait focus

**Advanced poses (Pro features):**
- Various intimate positions
- Dynamic action poses
- Multi-subject interactions

> 📌 **Note:** 116+ poses available in total. See [SKILL.md](SKILL.md) for complete list. Some poses may require Pro subscription.

---

## 🌈 Available Filters

| Filter | Description |
|--------|-------------|
| Default | No filter |
| Cyberpunk | Neon futuristic |
| VHS | Retro videotape |
| Manga | Comic book style |
| Flash | Camera flash |
| Analog | Film camera look |
| Professional | Studio quality |
| Cinematic | Movie grade |
| Studio | Professional lighting |
| Polaroid | Instant photo |
| Vintage | Retro aged |

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
| Face restoration | +1 Gem (realistic only) |
| Peak hours | +0.25 Gem (may apply) |

**Note:** 1 Gem = 1 Image

---

## 📋 Examples

### 1. Anime Style Girl

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

### 2. Realistic Portrait

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

## 📚 Scripts

| Script | Description |
|--------|-------------|
| `promptchan_generate.py` | Generate images |
| `promptchan_status.py` | Check balance and status |
| `promptchan_styles.py` | List available styles/poses/filters |

---

## ⚠️ Important Notes

1. **API Key Security**: Keep your API Key private, do not commit to version control
2. **Content Guidelines**: Do not generate illegal content (account ban risk)
3. **Cost Control**: Ensure sufficient Gems before generation
4. **Peak Hours**: Additional charges may apply (0.25 Gem/image)
5. **Face Restoration**: Only use with realistic styles, not needed for anime

---

## 🔗 Links

- **Register**: https://promptchan.com/register
- **Official Docs**: https://promptchan.com/docs
- **API Settings**: https://promptchan.com/settings
- **Pricing**: https://promptchan.com/pricing
- **Create**: https://promptchan.com/create

---

## 📄 License

MIT License

---

## 🤝 Contributing

Contributions welcome! Please read our contributing guidelines before submitting PRs.

---

## 📞 Support

- **Discord**: [Join our server](https://discord.gg/promptchan)
- **Email**: support@promptchan.com
- **Issues**: [GitHub Issues](https://github.com/promptchan/api/issues)

---

## 🤖 Using with OpenClaw

This skill can be integrated with OpenClaw for seamless AI image generation.

### Method 1: Natural Language Prompts

Simply describe the image you want in chat:

```
Generate an image: cute anime girl, long pink hair, school uniform, cherry blossoms
```

```
Create a cyberpunk style image: neon lights, futuristic city, night
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

Then use short commands:

```
/pc Generate an anime girl, pink hair, smiling
```

```
/promptchan Cyberpunk style, neon lights, futuristic city
```

### Method 3: Use sessions_spawn

Call the skill programmatically:

```python
from openclaw import sessions_spawn

sessions_spawn(
    task="Generate an image using PromptChan API: cute anime girl, school uniform, cherry blossoms",
    runtime="subagent",
    mode="run"
)
```

### Method 4: Configure as OpenClaw Tool

Add to `openclaw.json` tools section:

```json
{
  "tools": {
    "promptchan": {
      "type": "script",
      "path": "skills/promptchan-for-openclaw/scripts/promptchan_generate.py",
      "description": "Generate images using PromptChan AI",
      "parameters": {
        "prompt": {"type": "string", "required": true},
        "style": {"type": "string", "default": "Anime"},
        "quality": {"type": "string", "default": "Ultra"}
      }
    }
  }
}
```

Then use in chat:

```
Use promptchan tool to generate: cute girl, school uniform, city at night
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

### Example OpenClaw Workflow

1. User: `Generate an anime girl with pink hair in school uniform`
2. OpenClaw calls `promptchan_generate.py` with the prompt
3. Script sends request to PromptChan API
4. API returns generated image
5. OpenClaw displays the image to user

For more details, see the [OpenClaw documentation](https://docs.openclaw.ai).

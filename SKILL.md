---
name: promptchan-for-openclaw
description: PromptChan AI Image Generation API Skill for OpenClaw - Support for multiple art styles, poses, and filters
---

# PromptChan API Skill for OpenClaw

AI image generation based on PromptChan AI platform, supporting multiple art styles, poses, filters and advanced features.

## 🌍 Languages

- [English](README.md) (Default)
- [中文](README_zh.md)
- [日本語](README_ja.md)

## 📝 Registration & API Key

### Step 1: Create Account

**Important:** Use the exclusive registration link below for free starter Gems!

**Register here:** https://promptchan.com/m/YCYAZJj7uKQcbpP1wMcFuzA5zIY2/3hov

### Step 2: Generate API Key

1. Login and go to Settings: https://promptchan.com/settings
2. Scroll to **API Key** section
3. Click **"Generate"** to create your key
4. Copy and save your API Key (shown only once!)

### Step 3: Top Up Gems (Optional)

- API uses **Gems** as currency
- **1 Gem = 1 Image**
- New users receive free starter Gems
- Top up: https://promptchan.com/pricing

## Configuration

Add to `openclaw.json`:

```json
{
  "promptchan": {
    "apiKey": "your-api-key-here",
    "baseUrl": "https://promptchan.com"
  }
}
```

Or use environment variables:
- `PROMPTCHAN_API_KEY` - API Key
- `PROMPTCHAN_BASE_URL` - Base URL (default: https://promptchan.com)

## Usage

### Basic Image Generation

```bash
python scripts/promptchan_generate.py \
  --prompt "cute girl, school uniform, city at night" \
  --api-key "your-api-key" \
  --output images/output.png
```

### Full Example

```bash
python scripts/promptchan_generate.py \
  --prompt "beautiful girl, long hair, sunset, detailed eyes" \
  --negative-prompt "ugly, deformed, noisy" \
  --style "Anime" \
  --poses "Default" \
  --filter "Cinematic" \
  --detail 1 \
  --creativity 50 \
  --quality "Ultra" \
  --image_size "512x768" \
  --seed 12345 \
  --api-key "your-api-key" \
  --output images/anime-girl.png
```

### Check Remaining Gems

```bash
python scripts/promptchan_status.py --api-key "your-api-key"
```

## Scripts

| Script | Description |
|--------|-------------|
| `scripts/promptchan_generate.py` | Generate images |
| `scripts/promptchan_status.py` | Check balance and status |
| `scripts/promptchan_styles.py` | List available styles/poses/filters |

## Available Styles (15 total)

- Cinematic - Movie-style rendering
- Anime - Japanese animation style
- Hyperreal - Photorealistic
- Hyperanime - Enhanced anime
- K-Pop - Korean pop style
- Fur - Furry art style
- Furtoon - Furry cartoon
- Render XL+ - Enhanced 3D render
- Illustration XL+ - Enhanced illustration
- Anime XL - Large anime model
- Anime XL+ - Enhanced large anime
- Hardcore XL - Intense style
- Cinematic XL - Large cinematic model
- Photo XL+ - Enhanced photo style
- Hyperreal XL+ - Enhanced hyperreal

## Available Poses (116 total)

Common poses:
- Default - Neutral pose
- POV Missionary - POV missionary position
- POV Doggystyle - POV rear entry
- POV Blowjob - POV oral
- Cum in Mouth - Oral finish
- Titjob - Breast job
- POV Cowgirl - POV woman on top
- Mating Press - Intimate press
- Spread Ass - Exposed rear
- Cumshot - Body finish
- Kneeling - Kneeling position
- Sitting - Seated position
- Showering - In shower
- Cuddling - Embrace
- Smiling - Happy expression
- Orgasm Face - Climax expression
- POV Anal - POV anal
- Bukkake - Group finish

See README.md for complete list.

## Available Filters (11 total)

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

## Examples

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

## Pricing

| Item | Cost |
|------|------|
| Base generation | 1 Gem/image |
| Extreme quality | +1 Gem |
| Max quality | +2 Gem |
| Face restoration | +1 Gem (realistic only) |
| Peak hours | +0.25 Gem (may apply) |

**Note:** 1 Gem = 1 Image

## Troubleshooting

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

## Important Notes

1. **API Key Security**: Keep your API Key private, do not commit to version control
2. **Content Guidelines**: Do not generate illegal content (account ban risk)
3. **Cost Control**: Ensure sufficient Gems before generation
4. **Peak Hours**: Additional charges may apply (0.25 Gem/image)
5. **Face Restoration**: Only use with realistic styles, not needed for anime

## Links

- **Register:** https://promptchan.com/m/YCYAZJj7uKQcbpP1wMcFuzA5zIY2/3hov
- **Official Docs:** https://promptchan.com/docs
- **API Settings:** https://promptchan.com/settings
- **Pricing:** https://promptchan.com/pricing
- **Create:** https://promptchan.com/create

## License

MIT License

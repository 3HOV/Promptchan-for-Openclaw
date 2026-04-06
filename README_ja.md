# PromptChan AI 画像ジェネレーター

> 🎨 複数のアートスタイルとフィルターをサポートする高度な AI 画像生成プラットフォーム

**無料トライアル：** 新規ユーザーは簡単なタスクを完了すると **100 無料 Gems** を獲得できます！

[English](README.md) | [中文](README_zh.md)

## 🎯 概要

PromptChan AI 画像ジェネレーターは、さまざまなアートスタイルの高品質な AI 生成画像を作成するための強力なツールです。迅速なプロフェッショナル画像生成が必要なアーティスト、コンテンツクリエイター、開発者に最適です。

## 📋 目次

- [クイックスタート](#-クイックスタート)
- [登録と API キー](#-登録と-api-キー)
- [使い方](#-使い方)
- [利用可能なスタイル](#-利用可能なスタイル)
- [利用可能なフィルター](#-利用可能なフィルター)
- [料金](#-料金)
- [使用例](#-使用例)
- [トラブルシューティング](#-トラブルシューティング)
- [OpenClaw での使用方法](#-openclaw-での使用方法)

---

## 🚀 クイックスタート

### 前提条件

```bash
pip install requests
```

### 基本的な使い方

画像を生成：

```bash
python scripts/promptchan_generate.py \
  --prompt "cute girl, school uniform, city at night, long hair" \
  --api-key "your-api-key-here" \
  --output images/output.png
```

### 残量 Gems を確認

```bash
python scripts/promptchan_status.py --api-key "your-api-key-here"
```

---

## 📝 登録と API キー

### 1️⃣ アカウント作成

**重要：** 以下の専用登録リンクを使用すると、無料スタート Gems がもらえます！

👉 **登録：** [https://promptchan.com/](https://promptchan.com/m/YCYAZJj7uKQcbpP1wMcFuzA5zIY2/3hov)

### 2️⃣ API キーの生成

1. ログインして設定へ：https://promptchan.com/settings
2. **API Key** セクションにスクロール
3. **"Generate"** をクリックしてキーを作成
4. API キーをコピーして保存（1 回のみ表示！）

### 3️⃣ Gems のチャージ

- API は **Gems** を通貨として使用
- **1 Gem = 1 画像**
- **新規ユーザー：簡単なタスクを完了すると 100 無料 Gems！**
- チャージ：https://promptchan.com/pricing

---

## 💻 使い方

### コマンドライン引数

#### 必須引数
| 引数 | 説明 |
|------|------|
| `--prompt`, `-p` | 生成したい画像を説明するプロンプト |
| `--api-key` | あなたの PromptChan API キー |

#### オプション引数

**スタイル設定：**
| 引数 | デフォルト | 説明 |
|------|--------|------|
| `--style`, `-s` | Cinematic | アートスタイル（[利用可能なスタイル](#-利用可能なスタイル) を参照） |
| `--filter`, `-f` | Default | フィルター効果（[利用可能なフィルター](#-利用可能なフィルター) を参照） |

**品質設定：**
| 引数 | デフォルト | 説明 |
|------|--------|------|
| `--quality`, `-q` | Ultra | 品質レベル（Ultra/Extreme/Max） |
| `--detail` | 0 | 詳細レベル（-2 から 2） |
| `--creativity`, `-c` | 50 | 創造性レベル（30/50/70） |

**その他：**
| 引数 | デフォルト | 説明 |
|------|--------|------|
| `--image_size` | 512x768 | 画像サイズ（512x512/512x768/768x512） |
| `--seed` | -1 | ランダムシード（-1 でランダム） |
| `--negative-prompt`, `-n` | - | ネガティブプロンプト |
| `--output`, `-o` | 自動 | 出力ファイルパス |

### 完全な例

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

## 🎨 利用可能なスタイル

15 種類以上のプロフェッショナルアートスタイル：

**人気のスタイル：**
- Cinematic - 映画的レンダリング
- Anime - 日本アニメスタイル
- Hyperreal - 写真級写実
- Hyperanime - 強化アニメ
- K-Pop - 韓国ポップスタイル
- Render XL+ - 強化 3D レンダー
- Illustration XL+ - プロフェッショナルイラスト
- Photo XL+ - 強化フォトスタイル

**すべてのスタイルを一覧表示：**
```bash
python scripts/promptchan_styles.py --type styles
```

---

## 🌈 利用可能なフィルター

11 種類のプロフェッショナルフィルター：

- Default - フィルターなし
- Cyberpunk - ネオンフューチャリスティック
- VHS - レトロビデオテープ
- Manga - コミックブックスタイル
- Flash - カメラフラッシュ
- Analog - フィルムカメラ風
- Professional - スタジオ品質
- Cinematic - 映画グレード
- Studio - プロフェッショナル照明
- Polaroid - インスタントフォト
- Vintage - レトロエイジ

**すべてのフィルターを一覧表示：**
```bash
python scripts/promptchan_styles.py --type filters
```

---

## 💰 料金

| 項目 | コスト |
|------|------|
| 基本生成 | 1 Gem/画像 |
| Extreme 品質 | +1 Gem |
| Max 品質 | +2 Gem |
| 顔修復 | +1 Gem（写実的スタイルのみ） |
| ピーク時 | +0.25 Gem（適用される場合あり） |

**注意：** 1 Gem = 1 画像

---

## 📋 使用例

### 1. アニメスタイルのキャラクター

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

### 2. プロフェッショナルポートレート

```bash
python scripts/promptchan_generate.py \
  --prompt "beautiful woman, long black hair, elegant dress, studio lighting" \
  --style "Hyperreal XL+" \
  --filter "Professional" \
  --detail 1 \
  --api-key "your-api-key" \
  --output images/portrait.png
```

### 3. サイバーパンクスタイル

```bash
python scripts/promptchan_generate.py \
  --prompt "cyberpunk girl, neon lights, futuristic city, night" \
  --style "Cinematic XL" \
  --filter "Cyberpunk" \
  --creativity 70 \
  --api-key "your-api-key" \
  --output images/cyberpunk.png
```

### 4. バッチ生成

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

## 🔧 トラブルシューティング

### エラー：無効な API キー
- API キーが正しくコピーされているか確認
- 余分なスペースがないか確認
- 設定で API キーを再生成

### エラー：Gems 不足
- https://promptchan.com/pricing でチャージ
- 無料スタート Gems を請求済みか確認

### エラー：リクエストタイムアウト
- ピーク時は遅延が発生する可能性
- ネットワーク接続を確認
- 後で再試行

### 品質が低い
- `--detail` パラメータを増やす（1 または 2）
- `--quality "Extreme"` または `"Max"` を使用
- プロンプトを改善して詳細を追加

---

## 🤖 OpenClaw での使用方法

このスキルは OpenClaw に統合して、シームレスな AI 画像生成を実現できます。

### 方法 1：自然言語プロンプト

チャットで生成したい画像を説明するだけです：

```
画像を生成：かわいいアニメの女の子、ピンクの長い髪、制服、桜
```

### 方法 2：openclaw.json で設定

`openclaw.json` にスキル設定を追加：

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

### プロンプト作成のヒント

**良いプロンプト：**
- 具体的に：`かわいいアニメの女の子、ピンクの長い髪、青い目、制服、桜、笑顔`
- 品質用語を含む：`傑作、最高品質、詳細な目、8k`
- 照明と雰囲気：`夕日、映画的照明、ムーディーな雰囲気`

**避けるべきこと：**
- 曖昧すぎる：`女の子`
- 矛盾：`昼と夜の混合`
- 複雑すぎる：1 つのプロンプトに要素が多すぎる

---

## 🔗 リンク

- **登録：** [https://promptchan.com/](https://promptchan.com/m/YCYAZJj7uKQcbpP1wMcFuzA5zIY2/3hov)
- **公式ドキュメント：** https://promptchan.com/docs
- **API 設定：** https://promptchan.com/settings
- **料金：** https://promptchan.com/pricing

---

## 📄 ライセンス

MIT License

---

## 🤝 貢献

詳細は [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。

---

## 📞 サポート

- **Discord**：[サーバーに参加](https://discord.gg/promptchan)
- **メール**：support@promptchan.com
- **イシュー**：[GitHub Issues](https://github.com/promptchan/api/issues)

# PromptChan AI 画像ジェネレーター

> 🎨 複数のアートスタイル、ポーズ、フィルターをサポートする高度な AI 画像生成プラットフォーム

**無料トライアル：** 新規ユーザーは簡単なタスクを完了すると **100 無料 Gems** を獲得できます！

[English](README.md) | [中文](README_zh.md)

## 📋 目次

- [クイックスタート](#-クイックスタート)
- [登録と API キー](#-登録と-api-キー)
- [使い方](#-使い方)
- [利用可能なスタイル](#-利用可能なスタイル)
- [利用可能なポーズ](#-利用可能なポーズ)
- [利用可能なフィルター](#-利用可能なフィルター)
- [料金](#-料金)
- [使用例](#-使用例)
- [トラブルシューティング](#-トラブルシューティング)
- [API リファレンス](#-api-リファレンス)

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

👉 **登録：** https://promptchan.com/m/YCYAZJj7uKQcbpP1wMcFuzA5zIY2/3hov

### 2️⃣ API キーの生成

1. ログインして設定へ：**https://promptchan.com/settings**
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
| `--style`, `-s` | Cinematic | アートスタイル（[スタイル一覧](#-利用可能なスタイル) を参照） |
| `--poses` | Default | キャラクターポーズ（[ポーズ一覧](#-利用可能なポーズ) を参照） |
| `--filter`, `-f` | Default | フィルター効果（[フィルター一覧](#-利用可能なフィルター) を参照） |

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
| `--restore_faces` | false | 顔修復（+1 Gem、写実的スタイルのみ） |
| `--output`, `-o` | 自動 | 出力ファイルパス |

### 完全な例

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

## 🎨 利用可能なスタイル

| スタイル | 説明 |
|------|------|
| Cinematic | 映画的レンダリング |
| Anime | 日本アニメスタイル |
| Hyperreal | 写真級写実 |
| Hyperanime | 強化アニメ |
| K-Pop | 韓国ポップスタイル |
| Fur | ファリーアート |
| Furtoon | ファリーカートゥーン |
| Render XL+ | 強化 3D レンダー |
| Illustration XL+ | 強化イラスト |
| Anime XL | 大型アニメモデル |
| Anime XL+ | 強化大型アニメ |
| Hardcore XL | インテンススタイル |
| Cinematic XL | 大型映画モデル |
| Photo XL+ | 強化フォトスタイル |
| Hyperreal XL+ | 強化超写実 |

**すべてのスタイルを一覧表示：**
```bash
python scripts/promptchan_styles.py --type styles
```

---

## 🧍 利用可能なポーズ

100 種類以上のポーズオプション、様々なシーンや構図に対応：

**一般的なポーズ：**
- Default - 標準立ちポーズ
- Kneeling - 膝立ちポーズ
- Sitting - 座位ポーズ
- Standing - 立ちポーズ
- Lying Down - 横たわるポーズ
- Cuddling - 抱擁ポーズ
- Smiling - 笑顔
- Looking Up - 見上げる
- From Behind - 背面ビュー
- Close-up - クローズアップ

**高度なポーズ（Pro 機能）：**
- 様々な親密なポーズ
- ダイナミックアクションポーズ
- 複数キャラクターのインタラクション

> 📌 **注意：** 合計 116 種類以上のポーズが利用可能。完全なリストは [SKILL.md](SKILL.md) を参照。一部のポーズは Pro サブスクリプションが必要です。

---

## 🌈 利用可能なフィルター

| フィルター | 説明 |
|--------|------|
| Default | フィルターなし |
| Cyberpunk | ネオンフューチャリスティック |
| VHS | レトロビデオテープ |
| Manga | コミックブックスタイル |
| Flash | カメラフラッシュ |
| Analog | フィルムカメラ風 |
| Professional | スタジオ品質 |
| Cinematic | 映画グレード |
| Studio | プロフェッショナル照明 |
| Polaroid | インスタントフォト |
| Vintage | レトロエイジ |

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

### 1. アニメスタイルの女の子

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

### 2. 写実的ポートレート

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

## 📚 スクリプト

| スクリプト | 説明 |
|--------|-------------|
| `promptchan_generate.py` | 画像生成 |
| `promptchan_status.py` | 残高とステータスを確認 |
| `promptchan_styles.py` | 利用可能なスタイル/ポーズ/フィルターを一覧表示 |

---

## ⚠️ 重要なお知らせ

1. **API キーのセキュリティ**：API キーは非公開にし、バージョン管理にコミットしないでください
2. **コンテンツガイドライン**：違法なコンテンツを生成しないでください（アカウント停止のリスク）
3. **コスト管理**：生成前に十分な Gems があることを確認
4. **ピーク時**：追加料金が発生する可能性があります（0.25 Gem/画像）
5. **顔修復**：写実的スタイルでのみ使用、アニメスタイルでは不要

---

## 🔗 リンク

- **登録**：https://promptchan.com/m/YCYAZJj7uKQcbpP1wMcFuzA5zIY2/3hov
- **公式ドキュメント**：https://promptchan.com/docs
- **API 設定**：https://promptchan.com/settings
- **料金**：https://promptchan.com/pricing
- **作成**：https://promptchan.com/create

---

## 📄 ライセンス

MIT License

---

## 🤝 貢献

貢献を歓迎します！PR を送信する前に、貢献ガイドラインをお読みください。

---

## 📞 サポート

- **Discord**：[サーバーに参加](https://discord.gg/promptchan)
- **メール**：support@promptchan.com
- **_issues**：[GitHub Issues](https://github.com/promptchan/api/issues)

---

## 🤖 OpenClaw での使用方法

このスキルは OpenClaw に統合して、シームレスな AI 画像生成を実現できます。

### 方法 1：自然言語プロンプト

チャットで生成したい画像を説明するだけです：

`
画像を生成：かわいいアニメの女の子、ピンクの長い髪、制服、桜
`

`
サイバーパンクスタイルの画像を作成：ネオンライト、未来都市、夜景
`

### 方法 2：openclaw.json で設定

openclaw.json にスキル設定を追加：

`json
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
`

短いコマンドを使用：

`
/pc アニメの女の子を生成、ピンクの髪、笑顔
`

`
/promptchan サイバーパンクスタイル、ネオンライト、未来都市
`

### 方法 3：sessions_spawn を使用

プログラムからスキルを呼び出し：

`python
from openclaw import sessions_spawn

sessions_spawn(
    task="PromptChan API で画像を生成：かわいいアニメの女の子、制服、桜",
    runtime="subagent",
    mode="run"
)
`

### 方法 4：OpenClaw ツールとして設定

openclaw.json の tools セクションに追加：

`json
{
  "tools": {
    "promptchan": {
      "type": "script",
      "path": "skills/promptchan-for-openclaw/scripts/promptchan_generate.py",
      "description": "PromptChan AI で画像を生成",
      "parameters": {
        "prompt": {"type": "string", "required": true},
        "style": {"type": "string", "default": "Anime"},
        "quality": {"type": "string", "default": "Ultra"}
      }
    }
  }
}
`

チャットで使用：

`
promptchan ツールを使用して生成：かわいい女の子、制服、都市の夜景
`

### プロンプト作成のヒント

**良いプロンプト：**
- 具体的に：かわいいアニメの女の子、ピンクの長い髪、青い目、制服、桜、笑顔
- 品質用語を含む：傑作、最高品質、詳細な目、8k
- 照明と雰囲気：夕日、映画的照明、ムーディーな雰囲気

**避けるべきこと：**
- 曖昧すぎる：女の子
- 矛盾：昼と夜の混合
- 複雑すぎる：1 つのプロンプトに要素が多すぎる

### OpenClaw ワークフローの例

1. ユーザー：ピンクの髪のアニメの女の子を生成、制服を着ている
2. OpenClaw が promptchan_generate.py スクリプトを呼び出し
3. スクリプトが PromptChan API にリクエストを送信
4. API が生成された画像を返す
5. OpenClaw がユーザーに画像を表示

詳細については、[OpenClaw ドキュメント](https://docs.openclaw.ai) を参照してください。

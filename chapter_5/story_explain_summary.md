# 第5章　開発リソースは足りないのに増え続ける重圧 — ストーリー／解説要約

> 参照: `chapter_5.md` / `plot.md` / `pain_points.md` / `setting/reference/merged_references.md`

## ストーリー要約（重圧・ペインベース）

- 改善は進んでも「スピードを上げろ／現有リソースでどうにかして」が重なり、足りないのは人数なのか判断力なのかが見えない重圧になる
- AIを道具として既存プロセスに載せるだけでは失敗し、疲れ・説明責任・レビュー待ちが個人速度の裏側で膨らむ
- ボトルネックは実装から合意・検収・人間の対応荒れへ移り、「人が足りない」が「考える時間が足りない」にすり替わる
- 投資区分（新規／エンハンス／保守／運用）で可視化し、AIを入口拡大とOps置換の戦略に落とし、成果が組織に波及し始める

## 解説パート要約（文献リンク付き）

### 5-1 AIを「コードを早く書く道具」以上のパートナーに

- 「人が足りない」とき、足りないのは実装人数ではなく**何を作るかの決定**かもしれない
- 逼迫時の増員は [ブルックス『人月の神話』](https://www.amazon.co.jp/dp/4865944583) で逆効果になりうる
- AIは安い増員ではなく、プロセスと役割の再設計前提のリソース

### 5-2 AI活用の実践と組織的課題

- 個人タスクは速くなりうる一方、組織成果は頭打ち——アムダールの法則：並列化できない判断・レビューが天井になる
- 実証はばらつく：Copilot RCTでの速度向上（Peng et al.；Demirer et al. 約26%増等）の一方、ベテランOSSではAI使用群が平均19%遅い例（[METR 2025](https://arxiv.org/pdf/2507.09089)）
- 下流品質・負債リスク（[GitClear](https://www.gitclear.com/)）、レビュー負荷と組織スループットの乖離（[Faros AI](https://www.faros.ai/ai-productivity-paradox)；PRレビュー時間91%増等）
- AIは増幅器。制御なしの変更増は不安定化（[DORA 2025](https://dora.dev/research/2025/dora-report/)）。価値実現は人材・プロセスに依存（[BCG *Where's the Value in AI?*](https://www.bcg.com/publications/2024/wheres-value-in-ai) 10-20-70）
- AI疲れ・仕事の強化（[HBR: AI Doesn't Reduce Work—It Intensifies It](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it)）、認知的負債（[Cognitive Debt](https://www.rockoder.com/beyondthecode/cognitive-debt-when-velocity-exceeds-comprehension/)）
- レビューをコードから意図へ移す視点（[How to Kill the Code Review](https://www.latent.space/p/reviews-dead)）

### 5-3／5-4 投資区分による戦略転換と成果

- 開発生産性ツリー：新しい価値の工数 vs 運用・保守の工数を分け、AI戦略を「Increment」と「Capacity」に整理する
- リソース効率とフロー効率のバランス（待ちを減らす／バッチを小さくする）
- 成果は速度だけでなく障害・他部署の実感・計画の安定として現れることを説明する

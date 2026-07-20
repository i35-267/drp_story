# 第3章　測れない開発生産性を求められる重圧 — ストーリー／解説要約

> 参照: `chapter_3.md` / `plot.md` / `pain_points.md` / `setting/reference/merged_references.md`

## ストーリー要約（重圧・ペインベース）

- バグ対応が続き新規開発が止まり、「今のやり方は持続可能か」という問いがチームの重圧になる
- 平均PR数などは動いているように見えても、同じ規模の機能が遅くなる——見た目の指標と実態の乖離が説明できない痛み
- 負債の影響を可視化しようとしても一人では限界で、経営が求める「数字」に翻訳できず孤立する
- コスト換算と予兆の観点を手がかりにチームへ共有し、「測れない価値」を議論する土台に初めて手が届く

## 解説パート要約（文献リンク付き）

### 3-1 技術的負債が開発速度に与える影響

- 重圧の背景は、**負債が確実に速度を落とすのに従来指標では測れず説明できない構造**
- 時間の流出の基準線として [Stripe / Harris Poll *The Developer Coefficient*](https://stripe.com/reports/developer-coefficient-2018)（2018）：週約42%が負債・バッドコード対応に相当する見立て（自社同一とは限らない）
- 内部品質と変更コストの議論は [Fowler *Is High Quality Software Worth the Cost?*](https://martinfowler.com/articles/is-quality-worth-cost.html) と補完関係
- 可視化は単一KPIではなく、多角的な予兆検知が要る（[石垣「技術負債の『予兆検知』と『状況異変』のススメ」](https://speakerdeck.com/i35_267/ji-shu-fu-zhai-no-yu-zhao-jian-zhi-to-zhuang-kuang-yi-bian-nosusume)）

### 3-2 「今は動くから」の先にある持続不可能性

- 「動いている／テストも通る」でも、理解が追いつかないと負債は加速する（認知的負債の前段。詳細は第5章／[Cognitive Debt](https://www.rockoder.com/beyondthecode/cognitive-debt-when-velocity-exceeds-comprehension/)）
- AI支援下では Churn 増・リファクタ減などの下流リスクが報告される（[GitClear](https://www.gitclear.com/) Coding on Copilot / AI Code Quality レポート）
- 投資しても統計に現れない構造としてソロー／生産性パラドックス（Solow 1987；[Brynjolfsson 1993](https://dl.acm.org/doi/10.1145/163298.163309)）がある
- 組織適応なき局所改善は、事業側の「良くなった実感」に届かない

### 3-3 エンジニアとしての説明責任を果たす方法

- 遅れること自体より、**なぜ遅れたか／次はどう変わるか**を説明できないことが信頼を壊す
- 技術を財務の言葉に翻訳する（時間の流出・コスト増・返済後に戻る速度）
- 枠組みは [DORA](https://dora.dev/guides/dora-metrics/)／[SPACE](https://dl.acm.org/doi/10.1145/3453928) を内部健全性として使い、事業向けには計画信頼性とコスト換算を併記する
- 単純な output/input 比や評価直結は歪みとゲーミングを招く（[Petersen 2011](https://doi.org/10.1016/j.infsof.2010.12.001)）
- McKinsey の技術的負債議論も経営説明の補助線になりうる（[Demystifying Digital Dark Matter](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/demystifying-digital-dark-matter-a-new-standard-to-tame-technical-debt) 等）

# 第2章　開発生産性の目的を求められる重圧 — ストーリー／解説要約

> 参照: `chapter_2.md` / `plot.md` / `pain_points.md` / `setting/reference/merged_references.md`

## ストーリー要約（重圧・ペインベース）

- 障害のあと「開発生産性って何？」と自問しても、指標記事は一面的で答えにならない重圧が残る
- 山田（負債・持続可能性）、高橋（品質・テスト時間）、飛鳥（ユーザー価値）、部長（数字・売上）——同じ言葉で別の痛みを話し、共通理解ができない
- 「数字を出せ」と言われても、物的生産性と付加価値のどちらを測るか合意がなく、説明の糸口が握れない
- 他者の視点を想像して初めてずれの構造が見え、「持続可能な開発には何が必要か／測れない価値をどう可視化するか」という次の重圧に移る

## 解説パート要約（文献リンク付き）

### 2-1 ステークホルダーごとに異なる定義と、他者の視点を想像する重要性

- 重圧の背景は、**定義が職種ごとにバラバラで統合されていない構造**にある
- エンジニアリング側の枠組みとして、速度と安定性を対で見る [DORA / Four Keys](https://dora.dev/guides/dora-metrics/)、多次元で活動量偏重を戒める [SPACE](https://dl.acm.org/doi/10.1145/3453928)（Forsgren et al., 2021）
- 体感・フロー・認知負荷の軸として [DevEx](https://queue.acm.org/detail.cfm?id=3595878)（Noda et al., 2023）および [DevEx in Action](https://queue.acm.org/detail.cfm?id=3639443)（Forsgren et al., 2024）
- 単一指標で揃える危険を踏まえ、まず「誰が何を開発生産性だと思っているか」を認識し、視点を接続する

### 2-2 持続可能な開発とは何か

- 持続可能な開発は、短期の活動量最大化ではなく、**約束の信頼性を保ちながら価値を届け続けること**
- 技術的負債は単なる「汚いコード」ではなく返済義務と利息として捉える（[Ward Cunningham OOPSLA '92](https://martinfowler.com/bliki/TechnicalDebt.html)／[Fowler Technical Debt Quadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html)）
- 負債による開発者時間の流出は実証でも大きい（[Besker et al., JSS 2019](https://doi.org/10.1016/j.jss.2019.06.004) では平均約23〜36%が負債起因、と推定）
- 全体スループットの視点として制約理論（Goldratt『ザ・ゴール』／『クリティカルチェーン』）。律速箇所を見ずに局所最適化しない

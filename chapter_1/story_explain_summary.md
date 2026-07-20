# 第1章　明日までに改善して！と言われる重圧 — ストーリー／解説要約

> 参照: `chapter_1.md` / `plot.md` / `pain_points.md` / `setting/reference/merged_references.md`

## ストーリー要約（重圧・ペインベース）

- 「数字を出せ／明日までに改善して」と言われるが、何を測り何を直せばよいか共有されておらず、定義なき重圧だけが降る
- 生産性向上の宿題と同日に「来月末リリース必須」が乗り、計画の信頼性が「とにかく早く」にすり替わる
- 要件は大枠のまま、仕様変更・手戻り・テスト削り・残業が連鎖し、現場の痛み（疲弊・負債・品質不安）が蓄積する
- 障害対応の地獄で「速く出せ＝良くなった」が崩壊し、測れないまま詰められる孤独と「守れなかった」後悔が残る

## 解説パート要約（文献リンク付き）

### 1-1「開発生産性」という言葉が持つ構造的問題

- 重圧の正体は「遅さ」そのものではなく、**何が問題か・何を測るかが揃っていない状態でイメージだけが作られること**
- 本質は活動量ではなく、**約束の信頼性**（いつまでに、どの品質で届くか）。内部フローは [DORA metrics](https://dora.dev/guides/dora-metrics/) / [Four Keys](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance) で見えやすいが、事業側の計画信頼性を直接測るものではない
- 立場ごとに分子・分母が違い、現場の「速くなった体感」と経営の「価値の数字」には時間差がある。[Forsgren ら *The SPACE of Developer Productivity*](https://dl.acm.org/doi/10.1145/3453928)（ACM Queue, 2021）も単一の活動量指標では足りないとする
- 最初に揃えるのは施策ではなく三問：何のため／どの指標／誰の何のために使うか

### 1-2 スピード重視の技術的背景と問題点

- 「大枠で進めて」は計画柔軟ではなく、**修正コストを後工程に先送りする選択**。[NIST *The Economic Impacts of Inadequate Infrastructure for Software Testing*](https://www.nist.gov/system/files/documents/director/planning/report02-3.pdf)（2002）は、設計段階の欠陥修正コストを1としたとき実装で約5倍、リリース後で最大約30倍と報告
- 設計軽視 → テスト省略 → 負債・疲弊 → またスピード、の負のスパイラル。[Martin Fowler *Is High Quality Software Worth the Cost?*](https://martinfowler.com/articles/is-quality-worth-cost.html) は、内部品質の低下が数週間で変更速度を鈍らせると論じる
- 「品質かスピードか」は偽の二択。[SPACE](https://dl.acm.org/doi/10.1145/3453928) は活動量だけを増やすと悪化しうると警告（関連 [Noda ら *DevEx*](https://queue.acm.org/detail.cfm?id=3595878)）
- 逼迫時の増員は [ブルックス『人月の神話』](https://www.amazon.co.jp/dp/4865944583) の法則で逆効果になりうる。動かすならスコープ／日程／品質の合意が先

### 1-3 持続可能な開発への転換点

- 障害の地獄は「生産性向上の失敗」ではなく、**速度と品質のどちらかを選ぶ問いが間違っていた**ことの証拠
- 改善が進まない背景に、**説明できる共通言語（コスト・ROI）がない**ことがある
- 難しさは本質的複雑性（銀の弾丸なし）と偶有的複雑性（設計・負債で減らせる）に分かれる。[Brooks *No Silver Bullet*](https://www.cs.unc.edu/techreports/86-020.pdf)／[『人月の神話』](https://www.amazon.co.jp/dp/4865944583)
- 転換点は特効薬探しではなく、**本質に向き合い、定義・測定・説明可能性を関係者で揃えること**

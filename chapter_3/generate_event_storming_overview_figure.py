#!/usr/bin/env python3
"""Generate chapter_3/assets/event_storming_overview.png — white bg, black lines/text only.

イベントストーミングの進め方（段階的肉付け）と参加者・戦略的設計の位置づけを示す概念図。
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager as fm

for name in ["Hiragino Sans", "Hiragino Maru Gothic ProN", "Apple SD Gothic Neo"]:
    if any(name in f.name for f in fm.fontManager.ttflist):
        plt.rcParams["font.family"] = name
        break

plt.rcParams["figure.facecolor"] = "white"

fig, ax = plt.subplots(figsize=(9.8, 5.0), dpi=220)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.2)
ax.axis("off")
ax.set_facecolor("white")


def box(ax, x, y, w, h, text, fs=7.5):
    p = mpatches.FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        linewidth=1.0,
        edgecolor="black",
        facecolor="white",
    )
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color="black", linespacing=1.15)


def arrow(ax, x1, y1, x2, y2):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="-|>",
            color="black",
            lw=1.0,
            mutation_scale=9,
            shrinkA=1,
            shrinkB=1,
        ),
    )


# 見出し
ax.text(
    5.0,
    5.95,
    "イベントストーミングの進め方（概念図）",
    ha="center",
    va="top",
    fontsize=10.5,
    color="black",
)

# 参加者（同席）
ax.text(5.0, 5.35, "参加者（ワークショップで同席する例）", ha="center", va="top", fontsize=8.5, color="black")
roles = [
    (0.55, "ファシリテータ"),
    (2.65, "ドメイン\nエキスパート"),
    (4.75, "開発者／\n技術側"),
    (6.85, "プロダクト\nマネージャー"),
]
rw, rh = 1.85, 0.62
for i, (rx, lab) in enumerate(roles):
    box(ax, rx, 4.5, rw, rh, lab, fs=6.8)
    if i < len(roles) - 1:
        arrow(ax, rx + rw + 0.05, 4.5 + rh / 2, roles[i + 1][0] - 0.05, 4.5 + rh / 2)

ax.text(5.0, 4.25, "壁一面のボードに付箋を貼りながら、次の段階へ肉付けしていく", ha="center", va="top", fontsize=8.0, color="black")

# 4ステップ（本文の「段階的に肉付け」に対応）
y_step = 2.05
h_step = 1.35
w_step = 2.05
gap = 0.35
x0 = 0.5

steps = [
    ("①", "ドメインイベントを\n並べる（過去形）\nタイムライン"),
    ("②", "コマンド・役割・\n外部システムなどで\nフローを埋める"),
    ("③", "集約を\n見出す"),
    ("④", "境界づけられた\nコンテキストと\nコンテキスト間関係"),
]

for i, (num, body) in enumerate(steps):
    x = x0 + i * (w_step + gap)
    p = mpatches.FancyBboxPatch(
        (x, y_step),
        w_step,
        h_step,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        linewidth=1.05,
        edgecolor="black",
        facecolor="white",
    )
    ax.add_patch(p)
    ax.text(x + 0.28, y_step + h_step - 0.22, num, ha="left", va="top", fontsize=9, fontweight="bold", color="black")
    ax.text(x + w_step / 2, y_step + h_step / 2 - 0.06, body, ha="center", va="center", fontsize=7.0, color="black", linespacing=1.2)
    if i < len(steps) - 1:
        arrow(ax, x + w_step + 0.02, y_step + h_step / 2, x + w_step + gap - 0.02, y_step + h_step / 2)

# DDDでの位置づけ
ax.text(
    5.0,
    1.35,
    "ドメイン駆動設計における位置づけ（例）",
    ha="center",
    va="top",
    fontsize=8.5,
    color="black",
)
bw, bh = 4.35, 0.55
y_b = 0.55
p1 = mpatches.FancyBboxPatch(
    (0.65, y_b),
    bw,
    bh,
    boxstyle="round,pad=0.02,rounding_size=0.08",
    linewidth=1.0,
    edgecolor="black",
    facecolor="white",
)
p2 = mpatches.FancyBboxPatch(
    (5.0, y_b),
    bw,
    bh,
    boxstyle="round,pad=0.02,rounding_size=0.08",
    linewidth=1.0,
    edgecolor="black",
    facecolor="white",
)
ax.add_patch(p1)
ax.add_patch(p2)
ax.text(
    0.65 + bw / 2,
    y_b + bh / 2,
    "戦略的設計（全体像・境界の合意）← イベントストーミングが主に寄与",
    ha="center",
    va="center",
    fontsize=7.3,
    color="black",
)
ax.text(
    5.0 + bw / 2,
    y_b + bh / 2,
    "戦術的設計（実装の詳細）← 別の技法・議論で深める",
    ha="center",
    va="center",
    fontsize=7.3,
    color="black",
)

plt.tight_layout(pad=0.15)
out_dir = Path(__file__).resolve().parent / "assets"
out_dir.mkdir(parents=True, exist_ok=True)
out = out_dir / "event_storming_overview.png"
fig.savefig(out, dpi=220, facecolor="white", edgecolor="none", bbox_inches="tight")
print(out)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate figures for serialization/02_metrics.md."""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
import numpy as np

plt.rcParams["font.family"] = "Hiragino Sans"
plt.rcParams["axes.unicode_minus"] = False

COLOR = "black"
ASSETS = "/Users/ishigaki-masato/Desktop/drp_story/serialization/assets"


def figure_goodhart_law():
    labels = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8"]
    x = np.arange(len(labels))
    metric = np.array([62, 65, 68, 74, 82, 91, 98, 108], dtype=float)
    performance = np.array([88, 86, 84, 79, 72, 65, 58, 51], dtype=float)

    fig, ax = plt.subplots(figsize=(8.2, 4.8), dpi=220)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.plot(x, metric, color=COLOR, linewidth=2.0, marker="o", markersize=4.5, zorder=4)
    ax.plot(x, performance, color=COLOR, linewidth=2.0, linestyle=(0, (6, 4)),
            marker="s", markersize=4.0, zorder=4)
    kpi_idx = 2
    ax.axvline(kpi_idx - 0.5, color=COLOR, linewidth=0.7, linestyle=(0, (2, 3)), zorder=1)
    ax.text(kpi_idx - 0.48, 112, "指標が\n目標化", fontsize=7.8, color=COLOR, ha="left", va="top")
    ax.annotate("", xy=(6.2, metric[6]), xytext=(6.2, performance[6]),
                arrowprops=dict(arrowstyle="<->", color=COLOR, lw=0.85))
    ax.text(6.55, (metric[6] + performance[6]) / 2, "見かけと\n実態の乖離",
            fontsize=7.6, color=COLOR, ha="left", va="center")
    ax.set_title("グッドハートの法則：追う数値は上がるが、実際のパフォーマンスは下がる（概念図）",
                 fontsize=10.2, color=COLOR, pad=10)
    ax.set_xlabel("時間（四半期）", fontsize=10, color=COLOR)
    ax.set_ylabel("相対指数（概念値）", fontsize=10, color=COLOR)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9, color=COLOR)
    ax.set_ylim(40, 118)
    ax.set_yticks([50, 70, 90, 110])
    for spine in ax.spines.values():
        spine.set_color(COLOR)
        spine.set_linewidth(0.75)
    ax.tick_params(colors=COLOR)
    leg = ax.legend(
        handles=[
            Line2D([0], [0], color=COLOR, linewidth=2.0, marker="o",
                   label="追う数値指標（例：ベロシティ・PR数）"),
            Line2D([0], [0], color=COLOR, linewidth=2.0, linestyle=(0, (6, 4)), marker="s",
                   label="実際のパフォーマンス（品質・価値・信頼など）"),
        ],
        loc="upper left", frameon=True, edgecolor=COLOR, facecolor="white", fontsize=7.8,
    )
    leg.get_frame().set_linewidth(0.6)
    out = f"{ASSETS}/serialization_02_goodhart_law.png"
    plt.tight_layout()
    plt.savefig(out, facecolor="white", edgecolor="none", bbox_inches="tight", pad_inches=0.32)
    plt.close()
    print(out)


def _cell(ax, x, y, w, h, text, fontsize=7.6, bold=False, ha="center", face="white"):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="square,pad=0",
        facecolor=face, edgecolor=COLOR, linewidth=0.65, zorder=3,
    ))
    weight = "bold" if bold else "normal"
    ax.text(x + w / 2, y + h / 2, text, ha=ha, va="center",
            fontsize=fontsize, color=COLOR, fontweight=weight, zorder=4)


def _link(ax, p1, p2, style="-", rad=0.0, lw=0.7):
    ls = (0, (4, 3)) if style == "--" else "-"
    ax.add_patch(FancyArrowPatch(
        p1, p2, arrowstyle="-", color=COLOR, linewidth=lw,
        linestyle=ls, connectionstyle=f"arc3,rad={rad}",
        zorder=1,
    ))


def figure_dora_space_correlation():
    fig, ax = plt.subplots(figsize=(9.4, 6.2), dpi=220)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.2)
    ax.axis("off")

    ax.text(5, 7.75, "測るなら「対」と「束」で：DORA と SPACE の対応（概念図）",
            ha="center", fontsize=10.5, color=COLOR)

    # --- DORA table (left) ---
    lx, lw = 0.35, 3.55
    ax.text(lx + lw / 2, 7.15, "DORA Four Keys（対で見る）", ha="center", fontsize=9.0, color=COLOR)

    # group box: speed
    ax.add_patch(Rectangle((lx, 4.55), lw, 1.85, fill=False, edgecolor=COLOR, linewidth=0.55, linestyle=(0, (4, 2)), zorder=2))
    _cell(ax, lx, 6.05, lw, 0.42, "軸", fontsize=7.2, bold=True, face="#f5f5f5")
    _cell(ax, lx, 5.63, lw, 0.42, "指標", fontsize=7.2, bold=True, face="#f5f5f5")
    _cell(ax, lx, 5.21, 0.95, 0.42, "スピード", fontsize=7.4, bold=True)
    _cell(ax, lx + 0.95, 5.21, lw - 0.95, 0.42, "デプロイ頻度", fontsize=7.4)
    _cell(ax, lx, 4.79, 0.95, 0.42, "", fontsize=7.4)
    _cell(ax, lx + 0.95, 4.79, lw - 0.95, 0.42, "変更リードタイム", fontsize=7.4)

    # group box: stability
    ax.add_patch(Rectangle((lx, 2.75), lw, 1.85, fill=False, edgecolor=COLOR, linewidth=0.55, linestyle=(0, (4, 2)), zorder=2))
    _cell(ax, lx, 4.15, 0.95, 0.42, "安定性", fontsize=7.4, bold=True)
    _cell(ax, lx + 0.95, 4.15, lw - 0.95, 0.42, "変更失敗率", fontsize=7.4)
    _cell(ax, lx, 3.73, 0.95, 0.42, "", fontsize=7.4)
    _cell(ax, lx + 0.95, 3.73, lw - 0.95, 0.42, "復元時間", fontsize=7.4)

    ax.text(lx + lw / 2, 2.45, "どちらか一方だけを追わない", ha="center", fontsize=7.2, color=COLOR)

    # --- SPACE table (right) ---
    rx, rw = 6.1, 3.55
    ax.text(rx + rw / 2, 7.15, "SPACE（束で見る）", ha="center", fontsize=9.0, color=COLOR)

    space_rows = [
        ("S", "満足度・ウェルビーイング"),
        ("P", "成果・パフォーマンス"),
        ("A", "活動量"),
        ("C", "コミュニケーション・協働"),
        ("E", "効率・フロー"),
    ]
    _cell(ax, rx, 6.05, 0.55, 0.42, "次元", fontsize=7.2, bold=True, face="#f5f5f5")
    _cell(ax, rx + 0.55, 6.05, rw - 0.55, 0.42, "内容", fontsize=7.2, bold=True, face="#f5f5f5")

    space_centers = {}
    y = 5.63
    for key, label in space_rows:
        _cell(ax, rx, y, 0.55, 0.48, key, fontsize=8.0, bold=True)
        _cell(ax, rx + 0.55, y, rw - 0.55, 0.48, label, fontsize=7.3, ha="left")
        space_centers[key] = (rx, y + 0.24)
        y -= 0.52

    ax.text(rx + rw / 2, 2.45, "多次元をセットで見る", ha="center", fontsize=7.2, color=COLOR)

    # row centers for DORA metrics (right edge of cells)
    dora = {
        "deploy": (lx + lw, 5.42),
        "lead": (lx + lw, 5.0),
        "fail": (lx + lw, 4.36),
        "restore": (lx + lw, 3.94),
    }
    space_right = {k: (rx, v[1]) for k, v in space_centers.items()}

    # correlations (conceptual)
    links_solid = [
        (dora["deploy"], space_right["E"], 0.08),
        (dora["lead"], space_right["E"], -0.05),
        (dora["fail"], space_right["P"], 0.05),
        (dora["restore"], space_right["P"], -0.08),
        (dora["fail"], space_right["S"], 0.18),
        (dora["lead"], space_right["C"], -0.12),
    ]
    for p1, p2, rad in links_solid:
        _link(ax, p1, p2, style="-", rad=rad)

    # tension relations (dashed)
    links_dash = [
        (dora["deploy"], space_right["A"], 0.22),
    ]
    for p1, p2, rad in links_dash:
        _link(ax, p1, p2, style="--", rad=rad)

    ax.text(5.0, 5.55, "相関・\n補完", ha="center", fontsize=7.0, color=COLOR)
    ax.text(5.0, 4.55, "緊張\n関係", ha="center", fontsize=7.0, color=COLOR)

    # legend
    leg = ax.legend(
        handles=[
            Line2D([0], [0], color=COLOR, linewidth=1.0, label="実線：相関・補完（セットで見る）"),
            Line2D([0], [0], color=COLOR, linewidth=1.0, linestyle=(0, (4, 3)),
                   label="破線：緊張関係（単独追及に注意）"),
        ],
        loc="lower center", bbox_to_anchor=(0.5, 0.02), frameon=True,
        edgecolor=COLOR, facecolor="white", fontsize=7.6, ncol=2,
    )
    leg.get_frame().set_linewidth(0.6)

    out = f"{ASSETS}/serialization_02_dora_space_correlation.png"
    plt.tight_layout()
    plt.savefig(out, facecolor="white", edgecolor="none", bbox_inches="tight", pad_inches=0.28)
    plt.close()
    print(out)


if __name__ == "__main__":
    figure_goodhart_law()
    figure_dora_space_correlation()

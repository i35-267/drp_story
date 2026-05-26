#!/usr/bin/env python3
"""Generate serialization_01_waste_asset_accumulation.png (white bg, black only)."""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.transforms import blended_transform_factory
import numpy as np

plt.rcParams["font.family"] = "Hiragino Sans"
plt.rcParams["axes.unicode_minus"] = False

color = "black"
n_periods = 8
x = np.arange(n_periods)

increments = np.array([4, 5, 5, 6, 10, 14, 19, 27], dtype=float)
hatches = ["", "///"] * (n_periods // 2)
project_codes = [f"PRJ-{i + 1:04d}" for i in range(n_periods)]

end_year, end_q = 2026, 1
time_labels = []
y, q = end_year, end_q
for _ in range(n_periods):
    time_labels.append(f"{y}/Q{q}")
    q -= 1
    if q == 0:
        q, y = 4, y - 1
time_labels.reverse()

ai_start_index = 4
callout_x = 3.25

fig, ax = plt.subplots(figsize=(8.2, 4.8), dpi=220)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
text_trans = blended_transform_factory(ax.transAxes, ax.transData)

bottom = np.zeros(n_periods)
for i, inc in enumerate(increments):
    segment = np.zeros(n_periods)
    segment[i:] = inc
    ax.bar(
        x,
        segment,
        bottom=bottom,
        width=0.62,
        facecolor="white",
        edgecolor=color,
        linewidth=0.65,
        hatch=hatches[i],
        zorder=2,
    )
    bottom += segment

cumulative = np.cumsum(increments)

bar_right = n_periods - 1 + 0.31
layer_bottom = 0.0
for inc, code in zip(increments, project_codes):
    mid_y = layer_bottom + inc / 2
    ax.annotate(
        code,
        xy=(bar_right, mid_y),
        xycoords="data",
        xytext=(1.02, mid_y),
        textcoords=text_trans,
        fontsize=7.0,
        color=color,
        ha="left",
        va="center",
        annotation_clip=False,
        arrowprops=dict(arrowstyle="-", color=color, lw=0.55, shrinkA=0, shrinkB=2),
    )
    layer_bottom += inc

x_line = np.linspace(0, n_periods - 1, 320)
maintenance = np.exp(0.62 * x_line) - 1.0
maintenance = maintenance / maintenance.max() * cumulative[-1] * 1.18
ax.plot(x_line, maintenance, color=color, linewidth=1.8, linestyle=(0, (6, 3)), zorder=4)

ai_x = ai_start_index - 0.5
ax.axvline(ai_x, color=color, linewidth=0.75, linestyle=(0, (2, 2)), zorder=1)
ax.text(
    ai_x - 0.05,
    cumulative[-1] * 0.38,
    "AIエージェント活用開始",
    fontsize=7.3,
    color=color,
    ha="center",
    va="center",
)
ax.annotate(
    "",
    xy=(ai_start_index + 1.6, cumulative[ai_start_index + 1] * 0.95),
    xytext=(callout_x, cumulative[-1] * 0.82),
    arrowprops=dict(arrowstyle="-|>", color=color, lw=0.85, connectionstyle="arc3,rad=0.12"),
)
ax.text(
    callout_x,
    cumulative[-1] * 0.92,
    "AIエージェントにより\nソフトウェア資産の積み上がりが加速",
    ha="center",
    va="center",
    fontsize=9.0,
    color=color,
    linespacing=1.35,
    bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor=color, linewidth=0.65),
    zorder=6,
)

ax.set_title(
    "ソフトウェア資産の積み上がりと保守工数の増加のイメージ",
    fontsize=10.5,
    color=color,
    pad=10,
)

ax.set_xlabel("時間", fontsize=11, color=color)
ax.set_ylabel("相対規模", fontsize=11, color=color)
ax.set_xlim(-0.55, n_periods - 0.45)
ymax = max(cumulative[-1], maintenance.max()) * 1.12
ax.set_ylim(0, ymax)

ax.set_xticks(x)
ax.set_xticklabels(time_labels, fontsize=7.2, color=color, rotation=35, ha="right")
ax.set_yticks(np.linspace(0, ymax, 5))
ax.set_yticklabels([""] * 5)

for spine in ax.spines.values():
    spine.set_color(color)
    spine.set_linewidth(0.75)
ax.tick_params(colors=color, labelsize=9)

legend_elements = [
    Patch(facecolor="white", edgecolor=color, hatch="///", linewidth=0.65, label="ソフトウェア資産（コード・機能）"),
    Line2D([0], [0], color=color, linewidth=1.8, linestyle=(0, (6, 3)), label="保守工数"),
]
leg = ax.legend(
    handles=legend_elements,
    loc="upper right",
    frameon=True,
    edgecolor=color,
    facecolor="white",
    fontsize=8.8,
    handletextpad=0.6,
)
leg.get_frame().set_linewidth(0.6)

fig.subplots_adjust(right=0.76)
plt.tight_layout()
out = "/Users/ishigaki-masato/Desktop/drp_story/serialization/assets/serialization_01_waste_asset_accumulation.png"
plt.savefig(out, facecolor="white", edgecolor="none", bbox_inches="tight", pad_inches=0.32)
print(out)

#!/usr/bin/env python3
"""Generate assets/event_storming_board_bw.png

カラー版イベントストーミングボード相当の構図を、白背景・黒線の付箋風に再描画。
2つの Context・aggregate の丸・コンテキスト間の橋・曲線矢印を保持し、
付箋位置は読みやすさのため原文より間隔を広げて整理している。
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib import font_manager as fm
from matplotlib.patches import Ellipse, FancyArrowPatch, Polygon

for name in ["Hiragino Sans", "Hiragino Maru Gothic ProN", "Apple SD Gothic Neo"]:
    if any(name in f.name for f in fm.fontManager.ttflist):
        plt.rcParams["font.family"] = name
        break

plt.rcParams["figure.facecolor"] = "white"


def sticky(ax, cx, cy, w, h, text, fs=6.8, deg=0.0):
    w2, h2 = w / 2, h / 2
    f = min(0.14, 0.22 * min(w, h))
    verts_local = np.array(
        [
            [-w2, -h2],
            [w2, -h2],
            [w2, h2 - f],
            [w2 - f, h2],
            [-w2, h2],
        ],
        dtype=float,
    )
    theta = np.radians(deg)
    rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    verts = verts_local @ rot.T + np.array([cx, cy])
    ax.add_patch(
        Polygon(
            verts,
            closed=True,
            linewidth=0.95,
            edgecolor="black",
            facecolor="white",
            joinstyle="round",
            zorder=3,
        )
    )
    p1 = (rot @ np.array([w2 - f, h2])) + np.array([cx, cy])
    p2 = (rot @ np.array([w2, h2 - f])) + np.array([cx, cy])
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color="black", lw=0.55, zorder=4)
    y_line = h2 - 0.09
    q1 = (rot @ np.array([-w2 + 0.1, y_line])) + np.array([cx, cy])
    q2 = (rot @ np.array([w2 - f - 0.1, y_line])) + np.array([cx, cy])
    ax.plot([q1[0], q2[0]], [q1[1], q2[1]], color="black", lw=0.4, zorder=4)
    ax.text(
        cx,
        cy,
        text,
        ha="center",
        va="center",
        fontsize=fs,
        color="black",
        rotation=deg,
        rotation_mode="anchor",
        linespacing=1.05,
        zorder=5,
    )
    return cx, cy


def context_ellipse(ax, cx, cy, w, h, label):
    e = Ellipse(
        (cx, cy),
        w,
        h,
        fill=False,
        edgecolor="black",
        linewidth=1.15,
        linestyle=(0, (5, 4)),
        zorder=0,
    )
    ax.add_patch(e)
    ax.text(cx, cy + h / 2 - 0.32, label, ha="center", va="top", fontsize=8.5, color="black", zorder=1)


def agg_ellipse(ax, cx, cy, w, h):
    e = Ellipse(
        (cx, cy),
        w,
        h,
        fill=False,
        edgecolor="black",
        linewidth=0.9,
        linestyle=(0, (3, 3)),
        zorder=1,
    )
    ax.add_patch(e)
    ax.text(
        cx,
        cy - h / 2 + 0.2,
        "aggregate",
        ha="center",
        va="bottom",
        fontsize=6.0,
        color="black",
        style="italic",
        zorder=2,
    )


def arrow(ax, a, b, rad=0.12):
    fa = FancyArrowPatch(
        a,
        b,
        arrowstyle="-|>",
        mutation_scale=8,
        linewidth=0.85,
        color="black",
        connectionstyle=f"arc3,rad={rad}",
        shrinkA=8,
        shrinkB=8,
        zorder=2,
    )
    ax.add_patch(fa)


fig, ax = plt.subplots(figsize=(11.8, 6.0), dpi=220)
ax.set_xlim(0, 14)
ax.set_ylim(0, 7.6)
ax.axis("off")
ax.set_facecolor("white")

# 大きなコンテキスト境界（配置をやや横に広げて中央の橋に余白）
context_ellipse(ax, 4.05, 3.75, 7.0, 5.8, "◇◇ Context")
context_ellipse(ax, 11.1, 3.75, 6.6, 5.8, "□□ Context")

# ---- 左 ◇◇：下から上へ流れ + aggregate 1 つ ----
sticky(ax, 1.75, 1.95, 0.95, 0.46, "User", fs=6.5, deg=-5)
sticky(ax, 2.75, 2.55, 1.1, 0.5, "Command", fs=6.4, deg=2)
sticky(ax, 3.95, 1.95, 1.2, 0.52, "Domain\nEvent", fs=6.0, deg=-2)

agg_ellipse(ax, 3.45, 3.35, 2.5, 1.5)
sticky(ax, 2.95, 3.45, 1.05, 0.44, "Event", fs=6.2, deg=-1)
sticky(ax, 3.85, 3.25, 1.05, 0.44, "Command", fs=6.0, deg=2)

sticky(ax, 5.35, 4.15, 1.15, 0.5, "Policy", fs=6.3, deg=-3)
sticky(ax, 5.15, 5.05, 1.15, 0.5, "Read\nModel", fs=6.0, deg=2)

# ---- 中央ブリッジ（原文の間の付箋：やや縦に離す） ----
sticky(ax, 7.4, 3.1, 1.2, 0.52, "External\nSystem", fs=5.9, deg=1)
sticky(ax, 7.45, 4.65, 1.1, 0.48, "Event", fs=6.3, deg=-3)

# ---- 右 □□：aggregate ×2 ----
sticky(ax, 8.95, 2.05, 1.1, 0.5, "Command", fs=6.2, deg=3)

agg_ellipse(ax, 9.9, 2.85, 2.4, 1.45)
sticky(ax, 9.35, 2.9, 1.0, 0.44, "Event", fs=6.0, deg=0)
sticky(ax, 10.35, 2.75, 1.05, 0.44, "Command", fs=5.9, deg=2)

agg_ellipse(ax, 11.55, 3.95, 2.35, 1.45)
sticky(ax, 11.05, 4.0, 1.0, 0.44, "Domain\nEvent", fs=5.7, deg=-1)
sticky(ax, 11.95, 3.85, 1.05, 0.44, "Command", fs=5.9, deg=2)

sticky(ax, 12.45, 5.1, 1.15, 0.5, "Read\nModel", fs=6.0, deg=-2)
sticky(ax, 12.6, 1.85, 1.05, 0.46, "Hotspot", fs=6.0, deg=4)

# ---- 矢印（左内） ----
arrow(ax, (2.2, 2.05), (2.45, 2.35), rad=0.08)
arrow(ax, (3.25, 2.65), (3.25, 2.95), rad=0.0)
arrow(ax, (3.65, 2.35), (3.35, 3.05), rad=0.1)
arrow(ax, (4.15, 3.55), (4.85, 3.95), rad=0.1)
arrow(ax, (5.35, 4.55), (5.2, 4.75), rad=0.05)

# ---- 左 → 橋 ----
arrow(ax, (5.65, 5.0), (6.95, 4.75), rad=0.12)
arrow(ax, (5.75, 4.25), (6.95, 3.35), rad=-0.1)

# ---- 橋 → 右 ----
arrow(ax, (8.0, 4.65), (8.75, 3.2), rad=0.15)
arrow(ax, (8.05, 3.2), (8.55, 2.35), rad=0.08)

# ---- 右内 ----
arrow(ax, (9.55, 2.25), (9.55, 2.45), rad=0.0)
arrow(ax, (10.55, 2.95), (10.75, 3.55), rad=0.12)
arrow(ax, (11.35, 4.35), (11.9, 4.85), rad=0.1)
arrow(ax, (12.2, 4.5), (12.45, 2.25), rad=-0.18)

plt.tight_layout(pad=0.1)
out_dir = Path(__file__).resolve().parent / "assets"
out_dir.mkdir(parents=True, exist_ok=True)
out = out_dir / "event_storming_board_bw.png"
fig.savefig(out, dpi=220, facecolor="white", edgecolor="none", bbox_inches="tight")
print(out)

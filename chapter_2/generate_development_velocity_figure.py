#!/usr/bin/env python3
"""Generate chapter_2 development_velocity_trend.png (white bg, black only).

コード複雑度（横軸）に対し、類推見積を基準とした実績／見積の倍率（縦軸）が
複雑になるほど扇状に広がるイメージ（IPAの計画vs実績図の構図に倣った概念図）。
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

for name in ["Hiragino Sans", "Hiragino Maru Gothic ProN", "Apple SD Gothic Neo"]:
    if any(name in f.name for f in fm.fontManager.ttflist):
        plt.rcParams["font.family"] = name
        break

rng = np.random.default_rng(42)


def sigma_of(t: np.ndarray) -> np.ndarray:
    """複雑度が高いほど倍率のばらつきが大きくなる（指数で立ち上がり）。"""
    t = np.clip(t, 0.0, 1.0)
    return 0.055 + 0.58 * (np.exp(2.05 * t) - 1.0) / (np.exp(2.05) - 1.0)


def mean_log_ratio(t: np.ndarray) -> np.ndarray:
    """高複雑域でやや過小見積もり寄り（中央が1をやや上回る）。"""
    return np.log(1.0 + 0.32 * (t**1.35))


# 点は扇の形が分かる程度に抑える（過密にしない）
n = 180
x = np.concatenate(
    [
        rng.uniform(4, 28, n // 4),
        rng.uniform(28, 55, n // 4),
        rng.uniform(55, 78, n // 4),
        rng.uniform(78, 97, n - 3 * (n // 4)),
    ]
)

t = x / 100.0
sigma = sigma_of(t)
log_ratio = mean_log_ratio(t) + sigma * rng.standard_normal(n)
y = np.exp(log_ratio)
y = np.clip(y, 0.28, 4.8)

fig, ax = plt.subplots(figsize=(6.3, 4.3), dpi=220)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
color = "black"

ax.scatter(
    x,
    y,
    s=22,
    facecolors="white",
    edgecolors=color,
    linewidths=0.6,
    alpha=0.9,
    zorder=2,
)

# 見積どおりの基準線
ax.axhline(
    1.0,
    color=color,
    linestyle="-",
    linewidth=1.0,
    zorder=1,
    label="倍率1.0（見積＝実績）",
)

# ばらつきの目安（破線の包絡）
xg = np.linspace(4.0, 97.0, 160)
tg = xg / 100.0
sg = sigma_of(tg)
ml = mean_log_ratio(tg)
band = 1.65
upper = np.exp(ml + band * sg)
lower = np.exp(ml - band * sg)
lower = np.clip(lower, 0.15, None)
ax.plot(xg, upper, color=color, linestyle=(0, (4, 3)), linewidth=0.85, zorder=1, label="ばらつきの目安（概念）")
ax.plot(xg, lower, color=color, linestyle=(0, (4, 3)), linewidth=0.85, zorder=1)

ax.set_xlabel("コード複雑度（静的解析・相対）", fontsize=11, color=color)
ax.set_ylabel("実績工数／見積工数（倍率）", fontsize=10, color=color)

ax.set_xlim(0, 100)
ymax = float(np.nanmax([y.max(), upper.max(), 1.05])) * 1.06
ax.set_ylim(0, min(5.2, ymax))

for spine in ax.spines.values():
    spine.set_color(color)
    spine.set_linewidth(0.75)
ax.tick_params(colors=color, labelsize=9)

leg = ax.legend(
    loc="upper left",
    frameon=True,
    edgecolor=color,
    facecolor="white",
    fontsize=7.8,
    handletextpad=0.5,
)
leg.get_frame().set_linewidth(0.6)

plt.tight_layout()
out = "/Users/ishigaki-masato/Desktop/drp_story/chapter_2/development_velocity_trend.png"
plt.savefig(out, facecolor="white", edgecolor="none", bbox_inches="tight", pad_inches=0.32)
print(out)

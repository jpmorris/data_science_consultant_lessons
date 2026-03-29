import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.cm import ScalarMappable

# ── Setup ─────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(16, 10))
ax.set_xlim(0.4, 7.2)
ax.set_ylim(-0.5, 11.5)
ax.set_facecolor('#fafafa')
fig.patch.set_facecolor('#fafafa')

cmap = LinearSegmentedColormap.from_list('valence', ['#c0392b', '#e67e22', '#f1c40f', '#27ae60'])
norm = Normalize(vmin=0, vmax=1)

# ── Shaded Regions ────────────────────────────────────────────────────────────
# (x0, y0, w, h, hex_color, label, label_x, label_y, label_ha)
regions = [
    (4.55, 8.0,  2.1, 2.8,  '#c0392b', '"High P-Doomers"',                       4.60, 10.70, 'left'),
    (4.55, 5.6,  2.1, 3.1,  '#27ae60', '"AI Bulls" & e/acc',                      6.60, 5.65,  'right'),
    (3.1,  5.3,  2.0, 3.4,  '#b7950b', '"Cautious Believers"',                    3.15, 8.60,  'left'),
    (0.45, 4.2,  2.5, 4.3,  '#922b21', '"AI as Con Job"\n(Stochastic Parrot Camp)', 0.50, 8.40, 'left'),
    (0.45, 0.1,  4.1, 4.5,  '#1a5276', '"AI as Normal Technology"',               0.50, 4.50,  'left'),
]

for (x0, y0, w, h, color, label, lx, ly, ha) in regions:
    rect = patches.FancyBboxPatch(
        (x0, y0), w, h,
        boxstyle='round,pad=0.08',
        facecolor=color, alpha=0.13,
        edgecolor=color, linewidth=1.8, linestyle='--',
        zorder=1
    )
    ax.add_patch(rect)
    ax.text(lx, ly, label,
            fontsize=9, color=color, fontweight='bold',
            ha=ha, va='top', zorder=3,
            bbox=dict(facecolor='white', edgecolor=color, alpha=0.88,
                      boxstyle='round,pad=0.35', linewidth=1.2))

# ── People ────────────────────────────────────────────────────────────────────
# (display_name, x, y, valence 0-1, dot_size, text_dx, text_dy)
# valence: 0 = catastrophic (red), 0.5 = neutral (yellow), 1 = utopian (green)
# x: 1=Never, 2=>30yrs, 3=20-30yrs, 4=10-20yrs, 5=5-10yrs, 6=<5yrs
# y: 0-10 societal impact scale
people = [
    # ── Existing ──────────────────────────────────────────────────────────────
    ('Yudkowsky',             6.30, 9.80, 0.02, 260,  0.14,  0.00),
    ('Bostrom',               5.70, 9.20, 0.08, 185,  0.14,  0.00),
    ('Hinton',                4.90, 8.60, 0.18, 215,  0.14,  0.00),
    ('Bengio',                4.55, 8.05, 0.22, 185, -0.14, -0.40),
    ('Altman',                5.50, 8.30, 0.68, 235,  0.14,  0.00),
    ('Amodei',                5.10, 7.30, 0.60, 195,  0.14,  0.00),
    ('Kokotajlo\n(ai-2027)',  6.40, 7.60, 0.90, 195,  0.14,  0.00),
    ('Andreessen',            6.10, 6.30, 0.96, 215,  0.14,  0.00),
    ('LeCun',                 2.60, 3.90, 0.62, 215,  0.14,  0.00),
    ('Bender',                1.20, 6.80, 0.08, 185, -0.14,  0.00),
    ('Gebru',                 1.65, 7.60, 0.12, 165,  0.14,  0.00),
    ('Narayanan\n(Snake Oil)', 2.10, 2.50, 0.52, 175,  0.14,  0.00),
    ('Gary Marcus',           2.95, 3.50, 0.45, 165,  0.14,  0.00),
    ('Scott Alexander\n(ACX)', 4.20, 6.60, 0.55, 145, 0.14,  0.00),
    # ── New ───────────────────────────────────────────────────────────────────
    # x: 1=Never, 2=>30yr, 3=20-30yr, 4=10-20yr, 5=5-10yr, 6=<5yr
    # y: societal impact 0-10  |  valence: 0=catastrophic … 1=utopian
    ('Sutton',                3.50, 5.50, 0.65, 175,  0.14,  0.00),  # 25% by 2030 / 50% by 2040; anti-doomer
    ('Hassabis',              5.10, 9.50, 0.72, 195,  0.14,  0.00),  # 5-10yr AGI; "10× the Industrial Revolution"
    ('Karpathy',              4.40, 4.80, 0.68, 185,  0.14,  0.00),  # "decade away"; skeptical of hype
    ('Fei-Fei Li',            2.80, 6.30, 0.60, 175,  0.14,  0.00),  # human-centered AI; full AGI far off
    ('S. Russell',            3.80, 8.80, 0.28, 185, -0.14,  0.00),  # safety-focused; control problem; high risk
    ('J. Jang',               5.00, 5.40, 0.65, 155,  0.14,  0.00),  # OpenAI model behavior; human-AI coevolution
    ('J. Dean',               5.60, 7.00, 0.76, 175,  0.14,  0.00),  # ~2028 implied; education & health optimism
    ('Yejin Choi',            2.20, 5.50, 0.42, 165, -0.14,  0.00),  # common-sense moonshot; LLMs insufficient
    ('Pachocki',              6.00, 8.80, 0.78, 175,  0.14,  0.00),  # "<10yr superintelligence"; automated research
    ('Sutskever',             5.00, 6.80, 0.58, 185,  0.14,  0.00),  # SSI; "could happen this decade"; scaling era over
    ('Anandkumar',            3.90, 7.20, 0.76, 165,  0.14,  0.00),  # AI for science/climate; positive impact
    # ── Additional ────────────────────────────────────────────────────────────
    ('A. Ng',                 2.50, 5.00, 0.80, 175,  0.14,  0.00),  # "decades away"; AI augments not replaces; educator
    ('Dwarkesh\nPatel',       3.70, 4.50, 0.65, 155,  0.14,  0.00),  # "next decade or two"; near-term impact limited
]

for (name, x, y, valence, size, dx, dy) in people:
    color = cmap(norm(valence))
    ax.scatter(x, y, s=size, c=[color], zorder=5,
               edgecolors='white', linewidths=1.8)
    tx, ty = x + dx, y + dy
    ha = 'left' if dx >= 0 else 'right'
    ax.text(tx, ty, name,
            fontsize=7.8, ha=ha, va='center', zorder=6,
            bbox=dict(facecolor='white', alpha=0.82, edgecolor='none', pad=1.8))

# ── Axes formatting ───────────────────────────────────────────────────────────
x_ticks  = [1, 2, 3, 4, 5, 6]
x_labels = ['Never /\nMeaningless', '>30 yrs', '20–30 yrs', '10–20 yrs', '5–10 yrs', '<5 yrs']
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels, fontsize=9)
ax.set_xlabel('Believed Time to AGI   ←  Skeptic ─────────────── Believer  →',
              fontsize=11, labelpad=12)

y_ticks  = [0, 2, 4, 6, 8, 10]
y_labels = ['None', 'Low', 'Moderate', 'Significant', 'Major', 'Civilization-\nScale']
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels, fontsize=9)
ax.set_ylabel('Societal Impact in Next 10 Years', fontsize=11, labelpad=12)

ax.set_title('AI Outlook Map: Timeline Beliefs, Societal Impact & Outcome Valence',
             fontsize=14, fontweight='bold', pad=18)

# ── Colorbar ──────────────────────────────────────────────────────────────────
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, orientation='vertical', fraction=0.022, pad=0.02)
cbar.set_label('Outcome Valence  (dot color)', fontsize=10, labelpad=8)
cbar.set_ticks([0, 0.25, 0.5, 0.75, 1.0])
cbar.set_ticklabels(['Catastrophic', 'Dangerous', 'Mixed', 'Optimistic', 'Utopian'], fontsize=8)

# ── Grid & Spines ─────────────────────────────────────────────────────────────
ax.grid(True, linestyle=':', alpha=0.35, color='gray', zorder=0)
ax.spines[['top', 'right']].set_visible(False)

# ── Disclaimer ────────────────────────────────────────────────────────────────
fig.text(0.5, 0.01,
         'AI-generated — positions are approximate interpretations of public statements and may be incorrect. '
         'Verify sources before citing. Last updated 2026-03-26.',
         ha='center', va='bottom', fontsize=7.5, color='#666666', style='italic',
         wrap=True)

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.savefig('ai_outlook_map.png', dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
print("Saved ai_outlook_map.png")
plt.show()

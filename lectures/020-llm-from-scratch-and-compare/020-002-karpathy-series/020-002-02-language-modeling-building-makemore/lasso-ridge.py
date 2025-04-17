#%%

import numpy as np
import matplotlib.pyplot as plt

# Generate a grid of beta1 and beta2 values
beta1_vals = np.linspace(-3, 3, 200)
beta2_vals = np.linspace(-3, 3, 200)
B1, B2 = np.meshgrid(beta1_vals, beta2_vals)

# Define a simple RSS surface: pretend X1 and X2 are orthogonal and centered
# RSS = (beta1 - 1)^2 + 2*(beta2 - 2)^2 (just for illustration)
RSS = (B1 - 1) ** 2 + 2 * (B2 - 2) ** 2

# Plot contour of the RSS
plt.figure(figsize=(8, 6))
contour = plt.contour(B1, B2, RSS, levels=20, cmap="viridis")
plt.clabel(contour, inline=True, fontsize=8)
plt.title("Elliptical Contours of RSS in (β₁, β₂) Space")
plt.xlabel("β₁")
plt.ylabel("β₂")

# Add L1 (lasso) and L2 (ridge) constraint boundaries
t = 2
# L1 (diamond)
plt.plot([t, 0, -t, 0, t], [0, t, 0, -t, 0], "r--", label="L1 Constraint (Lasso)")
# L2 (circle)
theta = np.linspace(0, 2 * np.pi, 200)
x_circle = t * np.cos(theta)
y_circle = t * np.sin(theta)
plt.plot(x_circle, y_circle, "b--", label="L2 Constraint (Ridge)")

plt.legend()
plt.grid(True)
plt.axhline(0, color="gray", linewidth=0.5)
plt.axvline(0, color="gray", linewidth=0.5)
plt.show()

# %%

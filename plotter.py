import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

def plot_orbits(r_initial, r_final, delta_v1, delta_v2, v_initial, v_final, vtransfer_initial, vtransfer_final):
    r_initial = r_initial / 1000
    r_final = r_final / 1000

    r_transfer= (r_initial + r_final) / 2
    r_minor_axis= sqrt(r_initial * r_final)
    focal_dist = sqrt(r_transfer**2 - r_minor_axis**2)

    fig, ax = plt.subplots(figsize=(9, 9))
    fig.canvas.manager.set_window_title("Orbital Transfer Calculator")
    ax.set_aspect('equal')

    theta = np.linspace(0, 2*np.pi, 1000)

    # Plot orbits
    ax.plot(r_initial * np.cos(theta), r_initial * np.sin(theta), '--b', label='Initial Orbit')
    ax.plot(r_final * np.cos(theta), r_final * np.sin(theta), '--g', label='Final Orbit')
    ax.plot(r_transfer* np.cos(theta) - focal_dist, r_minor_axis* np.sin(theta), 'orange', label='Transfer Orbit')

    # Earth
    ax.plot(0, 0, 'o', color='black')
    ax.annotate("Earth", xy=(-50,-60), fontsize=9)

    # Legend
    legend = ax.legend(loc='upper left')

    # Display relevant values
    info_text = (
        f"r₁ = {r_initial:.0f} km\n"
        f"r₂ = {r_final:.0f} km\n\n"
        f"v₁ = {v_initial / 1000:.2f} km/s\n"
        f"v₂ = {v_final / 1000:.2f} km/s\n"
        f"vₜ₁ = {vtransfer_initial / 1000:.2f} km/s\n"
        f"vₜ₂ = {vtransfer_final / 1000:.2f} km/s\n\n"
        f"Δv₁ = {delta_v1 / 1000:.2f} km/s\n"
        f"Δv₂ = {delta_v2 / 1000:.2f} km/s\n"
        f"Δv total = {(delta_v1 + delta_v2) / 1000:.2f} km/s"
    )

    
    ax.text(
        0.02, 0.3, info_text,
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='gray')
    )

    ax.set_title("Hohmann Transfer Orbit Visualization")
    ax.set_xlabel("X Position (km)")
    ax.set_ylabel("Y Position (km)")
    ax.grid(True)

 
    lim = max(r_initial, r_final) * 1.3  
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    plt.tight_layout()
    plt.show()

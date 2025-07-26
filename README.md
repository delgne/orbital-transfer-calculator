# Orbital Transfer Calculator

A Python tool to calculate and visualize Hohmann transfers between two circular orbits around Earth.

---

## What It Does

- Takes in two orbital radii in kilometers
- Calculates the required Δv for:
  - First burn (to enter the transfer orbit)
  - Second burn (to circularize at the target orbit)
- Visualizes:
  - The initial and target orbits
  - The elliptical transfer path
  - Key values (ΔV, radii) in an info panel

---

## Method

This tool uses the [**Hohmann transfer**](https://orbital-mechanics.space/orbital-maneuvers/hohmann-transfer.html), a two-burn maneuver to move between two circular, coplanar orbits.

1. **First Burn (Perigee Kick):**  
   Speed up at your starting orbit to get onto a transfer ellipse.

2. **Coast Along Ellipse:**  
   Drift along a half-ellipse that touches both the original and final orbit.

3. **Second Burn (Apogee Kick):**  
   At the far end of the ellipse, do a second burn to circularize.

The ΔV values are calculated using the [**vis-viva equation**](https://en.wikipedia.org/wiki/Vis-viva_equation):

<img width="431" height="200" alt="Screenshot 2025-07-25 at 8 58 41 PM" src="https://github.com/user-attachments/assets/5df97d7b-6dba-4a27-bade-bbab55d5d886" />


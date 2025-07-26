from physics import hohmann_transfer
from plotter import plot_orbits

def main():
    r_initial = float(input("Input the initial orbital radius (in km): ")) *1000
    r_final = float(input("Input the target orbital radius (in km): "))*1000


    delta_v1, delta_v2, total_delta_v, v_initial, v_final, vtransfer_initial, vtransfer_final = hohmann_transfer(r_initial, r_final)

    plot_orbits(r_initial,
    r_final,
    delta_v1,
    delta_v2,
    v_initial,
    v_final,
    vtransfer_initial,
    vtransfer_final)

if __name__ == "__main__":
    main()

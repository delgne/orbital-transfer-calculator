from math import sqrt

GM_EARTH = 3.986e14

def hohmann_transfer(r_initial, r_final, GM=GM_EARTH):
    #find radius of transfer orbit
    r_transfer = (r_initial+r_final)/2

    #find initial and final velocities
    v_initial = sqrt(GM/r_initial)
    v_final = sqrt(GM/r_final)

    #Find transfer velocities
    vtransfer_initial = sqrt(GM * (2/r_initial - 1/r_transfer))
    vtransfer_final = sqrt(GM * (2/r_final - 1/r_transfer))

    #Find deltaV's
    delta_v1 = abs(vtransfer_initial - v_initial)
    delta_v2 = abs(v_final-vtransfer_final)

    total_delta_v = delta_v1+delta_v2

    return delta_v1, delta_v2, total_delta_v, v_initial, v_final, vtransfer_initial, vtransfer_final


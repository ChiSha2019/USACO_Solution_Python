import math


def get_dist(v_max, v_f):
    return (1 + v_max) * v_max / 2 + (v_max - 1 + v_f) * (v_max - v_f) / 2


with open("1.in", "r") as input_file:
    line1 = input_file.readline().split()
    total_dist = int(line1[0])
    num_speed = int(line1[1])
    v_final = []
    for i in range(0, num_speed):
        v_final.append(int(input_file.readline()))

    for vf_item in v_final:
        time = -1
        dist_accelerate_to_vf = (1 + vf_item) * vf_item / 2
        if dist_accelerate_to_vf >= total_dist:
            time = math.ceil((math.sqrt(1 + 8 * total_dist) - 1) / 2)
        else:
            vMax = v_final
            '''
            increase vMax by 1 constantly until we get total_dist
            '''
            while get_dist(vMax, v_final) < total_dist:
                vMax += 1
            time = 2 * vMax - vf_item
            dif

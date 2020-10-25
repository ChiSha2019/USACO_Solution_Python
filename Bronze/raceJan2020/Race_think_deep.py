import math


def get_dist(v_max, v_f):
    return (1 + v_max) * v_max / 2 + (v_max - 1 + v_f) * (v_max - v_f) / 2


def sharp_top_distance(t, v_f):
    return t * t / 4 + v_f * t / 2 - v_f * v_f / 4


with open("race.in", "r") as input_file:
    line1 = input_file.readline().split()
    total_dist = int(line1[0])
    num_speed = int(line1[1])
    v_final = []
    for i in range(0, num_speed):
        v_final.append(int(input_file.readline()))

    with open("race.out", "w") as output_file:
        for vf_item in v_final:
            time = -1
            dist_accelerate_to_vf = (1 + vf_item) * vf_item / 2
            if dist_accelerate_to_vf >= total_dist:
                time = math.ceil((math.sqrt(1 + 8 * total_dist) - 1) / 2)
            else:
                time_sharptop_decimal = math.sqrt(2 * vf_item * vf_item + 4 * total_dist - 2 * vf_item) - vf_item
                # if use sharptop has to use time_sharptop to finish such distance
                time = math.ceil(time_sharptop_decimal)
            '''
            check if we need to switch to flat top
            '''

            #print(time_sharptop - vf_item - 1)
            '''
            sharptop_dist = time_sharptop * time_sharptop / 2 + vf_item * time_sharptop / 2 - vf_item * vf_item / 4
            if sharptop_dist - total_dist > :
                time -= 1
            '''
            output_file.write(str(time) + "\n")

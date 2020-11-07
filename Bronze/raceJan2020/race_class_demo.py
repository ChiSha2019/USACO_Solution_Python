'''
given distance to find min time <=> given time find max distance

we acceclerate as much as possible then decrease the speed to meet Vfinal
1) the distsance is not great enough or vfinal is not small enough of speed decrement, which we just need
to accelerate
d = (1+Vf)/2*Vf
t = (sqrt(1+8d)-1)/2a
2) you need to increase then drop your speed
d = t^2/4 + Vf/2*t - Vf^2/4+Vf/2 =>
t = -Vf + sqrt(2Vf^2 -2 Vf + 4d)
'''
import math

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
            output_file.write(str(time) + "\n")


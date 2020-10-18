'''
strategy:
for each line
keep looping
if current_length + length of next word > K, change line,
    update current_length to be length of next word
else  current_length = current_length+ length of next word
'''
with open("word.in", "r") as input_file:
    line1 = input_file.readline().split()
    word_num = int(line1[0])
    max_char_num_each_line = int(line1[1])
    line2 = input_file.readline().split()

    with open("word.out", "w") as output_file:
        current_length = 0
        for i in range(0, word_num):
            if current_length + len(line2[i]) > max_char_num_each_line:
                output_file.write("\n")
                output_file.write(line2[i])
                current_length = len(line2[i])
            else:
                current_length = current_length + len(line2[i])
                output_file.write(line2[i])
            if i < word_num -1 and current_length + len(line2[i+1]) <= max_char_num_each_line:
                output_file.write(" ")



#with open("/Users/qixia/PycharmProjects/USACO/Bronze/wordProcessor/word_bronze_jan20/1.in", "r") as input_file:
with open("word.in", "r") as input_file:
    line1 = input_file.readline().split()
    word_num = int(line1[0])
    max_char_num = int(line1[1])
    result = []
    line2 = input_file.readline().split()
    #with open("/Users/qixia/PycharmProjects/USACO/Bronze/wordProcessor/word_bronze_jan20/myoutput.out","w") as output_file:
    with open("word.out", "w") as output_file:
        cur_len = 0
        for i in range(word_num):
            if len(line2[i]) + cur_len > max_char_num:
                output_file.write("\n")
                output_file.write(line2[i])
                cur_len = len(line2[i])
            else:
                output_file.write(line2[i])
                cur_len += len(line2[i])
            if i < word_num - 1 and len(line2[i + 1]) + cur_len <= max_char_num:
                output_file.write(" ")




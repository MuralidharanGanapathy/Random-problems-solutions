#for n test cases
for _ in range(int(input())):
    input_string = input()
    numbers = list("1234567890")
    sum1 = 0
    start_index = 0
    end_index = 0
    index_flag = 0
    indi_flag = 0
    num_list = []
    for i in range(len(input_string)):
        if input_string[i] in numbers and index_flag == 0:
            start_index = i
            index_flag = 1
        elif input_string[i] not in numbers and index_flag == 1 or i == len(input_string) - 1 and index_flag == 1:
            end_index = i
            index_flag = 0
            indi_flag = 1
        if indi_flag == 1:
            if end_index == len(input_string) - 1:
                end_index += 1
            num_list.append(input_string[start_index:end_index])
            indi_flag = 0
    print(sum(list(map(int, num_list))))
            
            
            
def solution(array):
    set_array = set(array)
    dict_array = {i: 0 for i in set_array}
    #print(dict_array)

    for i in array:
        dict_array[i] += 1
    #print(dict_array)
    
    # 최빈값 2개넘으면 -1 리턴
    max_value = max(dict_array.values())
    if list(dict_array.values()).count(max_value) > 1:
        return -1
    else:
        # 최빈값이 1개면 그 값 리턴
        for key, value in dict_array.items():
            if value == max_value:
                return key
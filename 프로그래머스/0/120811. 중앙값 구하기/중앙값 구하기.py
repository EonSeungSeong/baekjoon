def solution(array):
    array.sort()
    index=len(array)//2 +1
    
    
    answer = array[index-1]
    return answer
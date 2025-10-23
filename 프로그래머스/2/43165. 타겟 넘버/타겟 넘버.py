def solution(numbers, target):
    answer = 0
    all_way = []
    def get_all_ways_by_doing_plus_or_minus(numbers, current_idx, current_sum):
        if current_idx == len(numbers):
            all_way.append(current_sum)
            return
    
        get_all_ways_by_doing_plus_or_minus(numbers, current_idx+1, current_sum + numbers[current_idx])
        get_all_ways_by_doing_plus_or_minus(numbers, current_idx+1, current_sum - numbers[current_idx])    

    get_all_ways_by_doing_plus_or_minus(numbers,0,0)
    
    for way in all_way:
        if target == way:
            answer+=1
        
    return answer
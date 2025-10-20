def solution(num_list):
    even_str = int("".join([str(num) for num in num_list if num %2 ==0]))
    odd_str = int("".join(str(num) for num in num_list if num%2 !=0 or num ==1))
    print(even_str)
    print(odd_str)
    answer =even_str + odd_str
    return answer


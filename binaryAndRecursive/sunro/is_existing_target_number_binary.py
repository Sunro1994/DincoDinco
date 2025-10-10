finding_target = 14
finding_numbers = [1,2,3,4,5,6,7,8,9,10]

def is_existing_target_number_binary(target, arrays):
    current_min = 0
    current_max = len(arrays) -1
    current_guess = (current_min + current_max) //2


    if arrays[current_guess] == target:
        return True
    elif arrays[current_guess] < target:
        current_min = current_guess + 1
    else:
        current_max = current_guess - 1

    return False
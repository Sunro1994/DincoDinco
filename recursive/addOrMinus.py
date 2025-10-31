import sys

input = sys.stdin.readline


def get_count_ways_to_target_by_doing_plus_or_minus(array, target):
    all_way = []

    def get_all_ways_by_doing_plus_or_minus(array, current_idx, current_sum):
        if current_idx == len(array):
            all_way.append(current_sum)
            return

        get_all_ways_by_doing_plus_or_minus(array, current_idx + 1, current_sum + array[current_idx])
        get_all_ways_by_doing_plus_or_minus(array, current_idx + 1, current_sum - array[current_idx])

    get_all_ways_by_doing_plus_or_minus(array, 0, 0)
    target_count =0

    for way in all_way:
        if way == target:
            target_count += 1

    return target_count

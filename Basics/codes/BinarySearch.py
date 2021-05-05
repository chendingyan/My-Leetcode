def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int(left + (right - left) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1


def binary_search_left(nums, target):
    # 左闭右开 [left, right)
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums)
    while left < right:
        mid = int(left + (right - left) / 2)
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    if left == len(nums):
        return -1
    if nums[left] == target:
        return left
    else:
        return -1


def binary_search_right(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums)

    while left < right:
        mid = int(left + (right - left) / 2)
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    return left - 1


if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5, 6, 7]
    nums = [1, 2, 2, 2, 3, 4, 5]
    # print(binary_search(nums, 2))
    # print(binary_search_left(nums, 2))
    print(binary_search_right(nums, 2))

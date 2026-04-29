def bin_search(arr: List[Tuple[int, int]], 
        target: int, forbidden_index: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        value = arr[mid][1]

        if value == target:
            if arr[mid][0] != forbidden_index:
                return mid

            k = mid - 1
            while k >= 0 and arr[k][1] == target:
                if arr[k][0] != forbidden_index:
                    return k
                k -= 1

            k = mid + 1
            while k < len(arr) and arr[k][1] == target:
                if arr[k][0] != forbidden_index:
                    return k
                k += 1

            return -1

        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_tup = [(i, n) for i, n in enumerate(nums)]
        nums_tup_sorted = sorted(nums_tup, key=lambda t: t[1])

        for i, value in nums_tup_sorted:
            complement = target - value
            j = bin_search(nums_tup_sorted, complement, i)

            if j != -1:
                return sorted([i, nums_tup_sorted[j][0]])

        return []
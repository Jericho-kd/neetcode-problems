# 121. Best Time to Buy and Sell Stock (easy)
def max_profit(prices: list[int]) -> int:
        min_value, profit = float('inf'), 0
        
        for i in prices:
            if i < min_value:
                min_value = i
            if i - min_value > profit:
                profit = i - min_value
        return profit


def max_profit_second(prices: list[int]) -> int:
    left, right = 0, 1
    max_profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        else:
            left = right
        right += 1

    return max_profit


# 239. Sliding Window Maximum (hard)
from collections import deque
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    window, result = deque(), []

    for idx, el in enumerate(nums):
        while window and window[0] <= idx - k:
            window.popleft()

        while window and nums[window[-1]] < nums[idx]:
            window.pop()

        window.append(idx)

        if idx >= k - 1:
            result.append(nums[window[0]])

    return result


# 219. Contains Duplicate II (easy)
def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
        tmp: dict[int, int] = {}
        
        for i, j in enumerate(nums):
            if j in tmp and abs(i - tmp[j]) <= k:
                    return True
            tmp[j] = i
                    
        return False


# 643. Maximum Average Subarray I (easy)
def find_max_average(nums: list[int], k: int) -> float:
    window_sum, window_start = 0, 0
    max_average = float('-inf')

    for idx, el in enumerate(nums):
        window_sum += el
        if idx >= k - 1:
            max_average = max(max_average, window_sum/k)
            window_sum -= nums[window_start]
            window_start += 1
    
    return max_average


# 209. Minimum Size Subarray Sum (medium)
def min_subarray_len(target: int, nums: list[int]) -> int:
    left, right = 0, 0
    min_len = len(nums) + 1
    result = 0

    while right < len(nums):
        result += nums[right]
        right += 1

        while result >= target:
            min_len = min(min_len, right - left)
            result -= nums[left]
            left += 1

    return min_len if min_len < len(nums) + 1 else 0
            
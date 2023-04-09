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

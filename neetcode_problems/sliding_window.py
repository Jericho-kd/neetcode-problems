# 121. Best Time to Buy and Sell Stock
def max_profit(prices: list[int]) -> int:
        min_value, profit = float('inf'), 0
        
        for i in prices:
            if i < min_value:
                min_value = i
            if i - min_value > profit:
                profit = i - min_value
        return profit
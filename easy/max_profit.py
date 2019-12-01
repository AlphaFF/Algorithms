class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        current_pos = 0
        length = len(prices)
        while current_pos < length - 1:
            for i in range(current_pos + 1, length):
                if prices[i] - prices[current_pos] > max_profit:
                    max_profit = prices[i] - prices[current_pos]
            current_pos += 1
        return max_profit

    def maxProfit1(self, prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


if __name__ == '__main__':
    s = Solution()
    # print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))

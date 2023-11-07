class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        start = 0
        basket = {}

        for end in range(len(fruits)):
            basket[fruits[end]] = end
            if len(basket) > 2:
                min_index = min(basket.values())
                del basket[fruits[min_index]]
                start = min_index + 1
            max_fruits = max(max_fruits, end - start + 1)

        return max_fruits

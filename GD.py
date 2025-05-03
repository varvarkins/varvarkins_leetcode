class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        prev = init
        for i in range (iterations):
            x_t = prev - 2 *prev * learning_rate
            prev = x_t
        return round(prev, 5)

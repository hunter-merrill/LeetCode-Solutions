class Solution:
    def climbStairs(self, n: int) -> int:
        wtr = [0, 1, 2] # Ways to reach; base cases: wtr[1] = 1, wtr[2] = 2

        for stair in range(3, n+1):
            wtr.append(wtr[stair - 2] + wtr[stair - 1])

        return wtr[n]
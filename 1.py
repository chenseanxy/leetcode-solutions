class Solution(object):
    def twoSum(self, nums: list, target: int) -> list:
        return self.twoSum_brute_froce(nums, target)

    def twoSum_brute_froce(self, nums: list, target: int) -> list:
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if(nums[i] + nums[j] == target):
                    return [i, j]

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
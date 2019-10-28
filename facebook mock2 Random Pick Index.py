class Solution:

    def __init__(self, nums: List[int]):
        # get dic ={1:[0], 2:[1], 3: [2, 3, 4]}
        self.dic = collections.defaultdict(list)
        for i in range(len(nums)):
            self.dic[nums[i]].append(i)
    def pick(self, target: int) -> int:
        ans = random.choice(self.dic[target])
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
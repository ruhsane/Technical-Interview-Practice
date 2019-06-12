class Solution:
    def twoSum(self, nums, target) :
        for i in nums:
            complement = target - i
            if complement in nums[nums.index(i)+1:]:
                return [nums.index(i), nums.index(complement)]


solution = Solution().twoSum([3,3],6)
# print(solution)

class Haha:
    def is_substring(self, substring, large_string):
        index = 0
        for i in large_string:
            print("we are looking at in large_string:", i)
            print("substring", substring[index])
            if i != substring[index]:
                index = 0
            elif i == substring[index]:
                index +=1 
                print(index)
                if index == len(substring):
                    return True
        return False

print(Haha().is_substring("rin","saririn"))
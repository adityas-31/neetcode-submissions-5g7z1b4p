class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a dict of the number and its index 
        nums_dict = dict()
        for i in range(len(nums)):
            d = target - nums[i]
            if d in nums_dict:
                print(d)
                return sorted([nums_dict[d] , i])
            else:
                nums_dict[nums[i]] = i

        print(nums_dict)
            # print("Index " , i , " of nums")
            # print("Original nums: " , nums)
            # print("New nums for ", nums[i] , ": " , nums_new)
            # print('\n')
        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_prod = 1
        new_nums = []
        for i in range(len(nums)):
            temp_list = [j for j in nums]
            # print("-----------iteration " , i+1 , "-----------")
            # print("temp_list = " , temp_list)
            x = temp_list.pop(i)
            # print("popped " , x)
            # print("temp_list is now " , temp_list )
            # print("nums is now " , nums )
            temp_prod = 1
            for t in temp_list:
                temp_prod *= t
            new_nums.append(temp_prod)

        # print(new_nums)
        return new_nums
            
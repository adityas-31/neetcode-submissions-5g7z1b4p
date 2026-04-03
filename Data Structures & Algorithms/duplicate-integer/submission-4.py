class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        super_dict = dict()
        dup_found = False
        # c = 1
        for i in nums:
            super_dict[i] = 0
        for i in nums:
            # print("iteration " , c)
            # c += 1
            if i not in super_dict:
                super_dict[i] = 1
                # print( i , " : " , super_dict[i])
            elif i in super_dict:
                super_dict[i] += 1
                # print(super_dict)
        for i in super_dict:
            if super_dict[i] > 1:
                dup_found = True
                break
        print(super_dict)
        return dup_found
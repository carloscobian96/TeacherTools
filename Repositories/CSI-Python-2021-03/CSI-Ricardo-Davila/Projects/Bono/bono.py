    def max_end3(nums):
        if nums[0:] > nums[:-1]:
       # this is where I am lost
        return print(nums)
        elif nums[:-1] > nums[0:]:
       # this is where I am lost
        return print(nums)  

max_end3([1, 2, 3])
max_end3([11, 5, 9])
max_end3([2, 11, 3])

def max_end3(nums):
    m = max(nums[0], nums[-1])
    print([m for _ in nums])

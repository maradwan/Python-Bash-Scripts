def max_dist(a,b,c,d):
    nums = [a,b,c,d]
    nums.sort()
    return (nums[3]-nums[0])**2 +  (nums[2]-nums[1])**2
    

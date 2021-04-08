#5-11 ordinals

nums = list(range(1,10))
print(nums)

for num in nums:
    if num == 1:
        print("{}st".format(num))
    elif num == 2:
        print("{}nd".format(num))
    elif num == 3:
        print("{}rd".format(num))
    else:
        print("{}th".format(num))

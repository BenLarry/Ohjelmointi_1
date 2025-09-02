def list_of_nums_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total

def main():
    nums_list = [1,2,3,4,5,6]
    print(list_of_nums_sum(nums_list))

main()
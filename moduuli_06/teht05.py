def list_even_nums(nums):
    even_list = []
    for num in nums:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

def main():
    list_of_nums = [1,2,3,4,5,6,7,8,9,10]
    print(list_even_nums(list_of_nums))


main()
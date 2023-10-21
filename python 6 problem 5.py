def remove_odd_numbers(input_list):
    even_numbers = [x for x in input_list if x % 2 == 0]
    return even_numbers
if __name__ == "__main":
    integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cut_down_list = remove_odd_numbers(integer_list)
    print("Original list:")
    print(integer_list)
    print("Cut-down list (odd numbers removed):")
    print(cut_down_list)
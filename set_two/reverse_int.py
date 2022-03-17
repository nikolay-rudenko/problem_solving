def descending_order(num):
    num_list = list(map(int, list(str(num))))
    num_list.sort(reverse=True)

    print(int(''.join(map(str, num_list))))
    # something



descending_order(455621)

def merge_lists_to_dict(list_1, list_2):
    lists_zip = zip(list_1, list_2)
    lists_dict = dict(lists_zip)
    return lists_dict


goods = ['apple', 'banana', 'strawberry', 'leamon']
price = [15, 49, 99, 26]

print(merge_lists_to_dict(goods, price))

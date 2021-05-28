
def flatten(list_of_lists):
    final_list = []

    if len(list_of_lists) == 0:
        return list_of_lists

    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])

    final_list = list_of_lists[:1] + flatten(list_of_lists[1:])
    final_list = [i for i in final_list if i!=None]

    return final_list

# flatten([0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2])

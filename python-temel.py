# 1. SORU

example_1 = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
flat_list = []


def flatten_list(liste):
    for item in liste:
        if type(item) == list:
            flatten_list(item)
        else:
            flat_list.append(item)


flatten_list(example_1)
print(flat_list)
flat_list.clear()

# 2. SORU

example_2 = [[1, 2], [3, 4], [5, 6, 7]]
flatten_list(example_2)
flat_list.reverse()
print(flat_list)

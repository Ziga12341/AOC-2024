# 101 tiles wide and 103 tiles tall

def xmas_tree(wide, tall):
    tree_coordinates = []
    upper_limit = wide // 2
    lower_limit = wide // 2
    for y in range(tall - 1):
        upper_limit += 1
        lower_limit += -1

        for x in range(wide):
            if x < upper_limit and x > lower_limit:
                tree_coordinates.append((x, y))


    tree_coordinates.append((wide // 2, tall - 1))
    return tree_coordinates



def xmas_tree(wide, tall):
    tree_coordinates = set()
    upper_limit = wide // 2
    lower_limit = wide // 2
    for y in range(tall - 1):
        upper_limit += 1
        lower_limit += -1

        for x in range(wide):
            if x < upper_limit and x > lower_limit:
                tree_coordinates.add((x, y))


    tree_coordinates.add((wide // 2, tall - 1))
    return tree_coordinates


# 11 tiles wide and 7 tiles tall.
print(xmas_tree(11, 7))
print(xmas_tree(101, 103))
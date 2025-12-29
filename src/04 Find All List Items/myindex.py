def index_all(list, item):
    index = []
    for i in range(len(list)):
        if list[i] == item:
            index.append(i)
        elif isinstance(list[i], list):
            for j in index_all(list[i], item):
               index.append ([i] + j)
    return index
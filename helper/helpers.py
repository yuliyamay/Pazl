def count_items(items):
    lst_items = []
    for item in items:
        lst_items.append(item)

    return len(lst_items)


def make_list(items, numbers=False):
    lst_items = []
    for item in items:
        if not numbers:
            lst_items.append(item.text)
        else:
            lst_items.append(float(item.text.replace('$', '')))

    return lst_items
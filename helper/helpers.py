def count_items(items):
    lst_items = []
    for item in items:
        lst_items.append(item)

    return len(lst_items)


def make_list(items, numbers=False, item_name=None):
    lst_items = []
    for item in items:
        try:
            if item_name:
                if item.find(item_name) > -1:
                    return True
            else:
                if not numbers:
                    lst_items.append(item.text)
                else:
                    lst_items.append(float(item.text.replace("$", "")))
        except:
            print("Function needs some work on it.")

    return lst_items

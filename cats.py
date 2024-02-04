import pathlib

data = pathlib.Path("cats.txt")

def get_cats_info(path):
    with open(path, "r", encoding='utf-8') as fh:
        lines = [el.strip() for el in fh.readlines()]
        new_lines = [el.split(',') for el in lines]
        cats_info = []
        for cat in new_lines:
            cats_info.append({"id": cat[0], 'name': cat[1], 'age': cat[2]})

    return cats_info

print(get_cats_info(data))
import pathlib

data = pathlib.Path("salaries.txt")

def total_salary (path):
    with open(path, "r") as fh:
        lines = [el.strip() for el in fh.readlines()]
        new_lines = list(map(lambda x: x.split(',')[1], lines))
        salaries_sum = sum(int(num) for num in new_lines)
        salaries_avarage = salaries_sum / len(new_lines)
    return (salaries_sum, salaries_avarage)    

print(total_salary(data)) 
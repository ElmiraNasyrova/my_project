import json
from csv import DictReader

books_list = []
example_data = []

with open("input/users.json", "r") as f:
    users_list = json.loads(f.read())

with open('input/books.csv', newline='') as f:
    reader = DictReader(f)
    for row in reader:
        books_list.append(row)

for i in range(len(users_list)):
    if len(books_list) > i + 1:
        books_data = [{"title": books_list[i]["Title"],
                       "author": books_list[i]["Author"],
                       "height": books_list[i]["Height"]}]
    else:
        books_data = []

    example_data.append(dict(name=users_list[i]["name"],
                             gender=users_list[i]["gender"],
                             address=users_list[i]["address"],
                             books=books_data))

with open("output/example_books_less_then_users.json", "w") as f:
    s = json.dumps(example_data, indent=4)
    f.write(s)

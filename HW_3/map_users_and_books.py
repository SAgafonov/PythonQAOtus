import json
from csv import DictReader


def read_from_csv() -> list:
    library = []
    with open('test_data/books-39204-271043.csv') as file:
        reader = DictReader(file)

        for row in reader:
            library.append(row)
    return library


def read_from_json() -> list:
    with open('test_data/users.json') as file:
        users = json.loads(file.read())
    return users


def get_values_from_books() -> list:
    """
    Maps "title", "author", "height" to values
    Makes list of dictionaries
    :return: list
    """
    title_author_height = []
    book_keys = ["title", "author", "height"]
    book_library = []
    data_from_csv = read_from_csv()
    for item in data_from_csv:
        title_author_height.append([item["Title"], item["Author"], item["Height"]])

    for item in title_author_height:
        book_library.append(dict(zip(book_keys, item)))
    return book_library


def get_values_from_users() -> list:
    """
    Maps "name", "gender", "address" to values
    Makes list of dictionaries
    :return: list
    """
    name_gender_address = []
    user_keys = ["name", "gender", "address"]
    user_library = []
    data_from_json = read_from_json()
    for item in data_from_json:
        name_gender_address.append([item['name'], item['gender'], item['address']])

    for item in name_gender_address:
        user_library.append(dict(zip(user_keys, item)))
    return user_library


def combine_users_and_books() -> json:
    """
    Distributes books to users and returns json
    :return: json
    """
    books = get_values_from_books()
    users = get_values_from_users()
    books_for_each_person = len(books) // len(users)
    left_books = len(books) % len(users)
    for user in users:
        user.update({"books": []})

    for user in users:
        for i in range(books_for_each_person):
            user["books"].append(books[i])
            books.pop(i)

    if left_books:
        while books:
            i = 0
            users[i]["books"].append(books[i])
            books.pop(i)
            i += 1

    return json.dumps(users, indent=2)

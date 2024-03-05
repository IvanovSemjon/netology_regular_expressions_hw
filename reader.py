import csv # читаем адресную книгу в формате CSV в список contacts_list


def file_read():
    with open("db/phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list

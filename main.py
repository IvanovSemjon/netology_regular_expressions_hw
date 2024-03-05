from config import SEARCH_PHONE_PATTERN, SUB_PHONE_PATTERN
import pandas as pd 
import reader
import re


lines = reader.file_read()


def main(lines):
    new_list = list()
    for line in lines:
        full_list = ' '.join(line[:3]).split(' ')
        result = [
            full_list[0], 
            full_list[1], 
            full_list[2], 
            line[3], 
            line[4], 
            re.sub(SEARCH_PHONE_PATTERN, SUB_PHONE_PATTERN, line[5]).strip(), 
            line[6]
            ]
        new_list.append(result)
    res = new_list

    df = pd.DataFrame(res, columns=['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email'])
    df = df.drop_duplicates(subset=['lastname', 'firstname'])
    res = df.to_csv('db/phonebook.csv', header=False, index=False)
    

if __name__ == '__main__':
    main(lines)
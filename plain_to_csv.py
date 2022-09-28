import re
import csv

def get_col_width(table_head:str) -> list:
    
    col_indices = list()
    
    col_labels = re.findall('[A-Z].*?(?=\s\s)',table_head)
    for label in col_labels:
        col_indices.append( re.search(label, table_head).span()[0] )
    return col_indices

def main() -> None:
    with open('table.txt', 'r') as txt_file:
        head = txt_file.readline()
        get_col_width(head)
    return None

if __name__ == '__main__':
    main()
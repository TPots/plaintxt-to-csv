import re, os, csv

def get_lh_col_indices(table_head:str) -> list:
    
    col_indices = list()
    
    col_labels = re.findall('[A-Z].*?(?=\s\s)',table_head)
    for label in col_labels:
        col_indices.append( re.search(label, table_head).span()[0] )
    col_indices.append(-1)
    return col_indices, col_labels

def plaintxt_to_csv(file_path: str) -> None:
    with open(file_path, 'r') as txt_file:
        col_indcies, col_labels = get_lh_col_indices(txt_file.readline())
        txt_table = txt_file.readlines()
        table = [col_labels]
        for idx, row in enumerate(txt_table):
            table.append([])
            for idx_2, col_index in enumerate(col_indcies[0:-2]):
                cell_text =  re.sub('\n','',str(row[col_indcies[idx_2] : col_indcies[idx_2 + 1]]).strip())
                table[idx + 1].append( cell_text )
    with open(os.path.join(os.getcwd(),re.sub('.txt$','.csv',file_path)), 'w') as _file:
        csv_file = csv.writer(_file, dialect='unix',delimiter=',')
        csv_file.writerows(table)
    return None

def main() -> None:
    plaintxt_to_csv('1000_inputs.txt')
    return

if __name__ == '__main__':
    main()
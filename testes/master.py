import csv
from reconcile_accounts import reconcile_accounts
from last_lines import last_lines
from pathlib import Path
#transactions1 = list(csv.reader(Path('transactions1.csv').open()))
#transactions2 = list(csv.reader(Path('transactions2.csv').open()))
#out1, out2 = reconcile_accounts(transactions1, transactions2)
#
#print("List1 reconciled:")
#for row in out1:
#    print(row)
#
#print("\nList2 reconciled:")
#for row in out2:
#    print(row)


# Exemplo de uso
file_path = 'my_file.txt'
for line in last_lines(file_path):
    print(line, end='')  # Print each line without adding extra newlines
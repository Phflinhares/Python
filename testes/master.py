import csv
from reconcile_accounts import reconcile_accounts
from last_lines import last_lines
from computed_property import computed_property
from pathlib import Path

#Exemplo de uso do Reconcile accounts
transactions1 = list(csv.reader(Path('transactions1.csv').open()))
transactions2 = list(csv.reader(Path('transactions2.csv').open()))
out1, out2 = reconcile_accounts(transactions1, transactions2)

print("Lista1 reconciliada:")
for row in out1:
    print(row)

print("\nLista2 reconciliada:")
for row in out2:
    print(row)
 



#Exemplo de uso do last lines
file_path = 'my_file.txt'
for line in last_lines(file_path):
    print(line, end='')


#Exemplo de uso do computed property
class Exemplo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @computed_property('a', 'b')
    def sum(self):
        print("Computando soma...")
        return self.a + self.b

    @sum.setter
    def sum(self, value):
        raise AttributeError("Não é possivel setar valor")

    @sum.deleter
    def sum(self):
        print("Deletando soma...")
        if hasattr(self, '_cache'):
            del self._cache['sum']
        if hasattr(self, '_dependency_cache'):
            del self._dependency_cache[self.dependencies]


ex = Exemplo(5, 6)
print(ex.sum)  
ex.a = 2
print(ex.sum)
del ex.sum
print(ex.sum)
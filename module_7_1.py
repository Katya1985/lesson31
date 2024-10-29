from fileinput import close


class Product:
    def __init__(self, name, weight, category):
        self.name = name          # Атрибут name - название продукта (строка)
        self.weight = weight      # Атрибут weight - общий вес товара (дробное число)
        self.category = category  # category - категория товара (строка)
    def __str__(self):
        return f'{self.name, self.weight, self.category}'  #возвращает строку в формате '<название>, <вес>,\n
                                            # <категория>'. Все данные в строке разделены запятой с пробелами.


class Shop:


    __file_name = 'products.txt' # Инкапсулированный атрибут __file_name = 'products.txt'


    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products


    def add(self, *products):
        for i in products:
            file = open(self.__file_name, 'r')
            if str(i) in file.read():
                print(f'Продукт {i} уже есть в магазине')
                file.close()
            else:
                file = open(self.__file_name, 'a')
                file.write(str(i) + '\n')
            file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


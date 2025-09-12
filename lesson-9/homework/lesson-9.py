1)import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius
radius = float(input("Doira radiusini kiriting: "))
circle = Circle(radius)
print(f"Maydon: {circle.area():.2f}")
print(f"Perimetr: {circle.perimeter():.2f}")
Maydon: 2123.72
Perimetr: 163.36

2)from datetime import datetime
class Person:
    def __init__(self, ism, mamlakat, tugilgan_sana):
        self.ism = ism
        self.mamlakat = mamlakat
        self.tugilgan_sana = datetime.strptime(tugilgan_sana, "%Y-%m-%d")
    def yosh(self):
        bugun = datetime.today()
        yosh = bugun.year - self.tugilgan_sana.year
        if (bugun.month, bugun.day) < (self.tugilgan_sana.month, self.tugilgan_sana.day):
            yosh -= 1
        return yosh
person = Person("Ali", "O'zbekiston", "1990-05-15")
print(f"{person.ism}ning yoshi: {person.yosh()} yoshda")
Alining yoshi: 35 yoshda

3)class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Xato: 0 ga bo'lib bo'lmaydi!"
        return a / b
calc = Calculator()
print("Qo'shish: 10 + 5 =", calc.add(10, 5))
print("Ayirish: 10 - 5 =", calc.subtract(10, 5))
print("Ko'paytirish: 10 * 5 =", calc.multiply(10, 5))
print("Bo'lish: 10 / 5 =", calc.divide(10, 5))
print("Bo'lish: 10 / 0 =", calc.divide(10, 0))
Qo'shish: 10 + 5 = 15
Ayirish: 10 - 5 = 5
Ko'paytirish: 10 * 5 = 50
Bo'lish: 10 / 5 = 2.0
Bo'lish: 10 / 0 = Xato: 0 ga bo'lib bo'lmaydi!

4)import math
class Shape:
    def area(self):
        raise NotImplementedError("Maydon hisoblash metodi aniqlanmagan.")
    def perimeter(self):
        raise NotImplementedError("Perimetr hisoblash metodi aniqlanmagan.")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
circle = Circle(5)
print("Doira maydoni:", round(circle.area(), 2))
print("Doira perimetri:", round(circle.perimeter(), 2))
square = Square(4)
print("Kvadrat maydoni:", square.area())
print("Kvadrat perimetri:", square.perimeter())
triangle = Triangle(3, 4, 5)
print("Uchburchak maydoni:", round(triangle.area(), 2))
print("Uchburchak perimetri:", triangle.perimeter())
Doira maydoni: 78.54
Doira perimetri: 31.42
Kvadrat maydoni: 16
Kvadrat perimetri: 16
Uchburchak maydoni: 6.0
Uchburchak perimetri: 12

5)class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   
        self.right = None 
class BinarySearchTree:
    def __init__(self):
        self.root = None 
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
        else:
            print(f"{value} allaqachon mavjud (takror).")
    def search(self, value):
        return self._search_recursive(self.root, value)
    def _search_recursive(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)
    def inorder_traversal(self):
        self._inorder_recursive(self.root)
    def _inorder_recursive(self, current):
        if current:
            self._inorder_recursive(current.left)
            print(current.value, end=' ')
            self._inorder_recursive(current.right)
bst = BinarySearchTree()
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)
print("Inorder (tartib bilan) chiqishi:")
bst.inorder_traversal()
print("\n\nQidiruv natijalari:")
print("60 mavjudmi?", bst.search(60))
print("25 mavjudmi?", bst.search(25))
Inorder (tartib bilan) chiqishi:
20 30 40 50 60 70 80 
Qidiruv natijalari:
60 mavjudmi? True
25 mavjudmi? False

6)class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return "Xato: stek bosh!"
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return "Stek bosh"
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print("Eng ustki element:", my_stack.peek())
print("Stek olchami:", my_stack.size())
print("Chiqarilgan element:", my_stack.pop())
print("Yangi ustki element:", my_stack.peek())
print("Stek boshmi?", my_stack.is_empty())
Eng ustki element: 30
Stek olchami: 3
Chiqarilgan element: 30
Yangi ustki element: 20
Stek boshmi? False

7)class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete(self, data):
        current = self.head
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        if current is None:
            print(f"{data} topilmadi.")
            return
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
    def display(self):
        current = self.head
        if not current:
            print("Ro'yxat bo'sh.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_start(5)
ll.insert_at_end(30)
print("Bog'langan ro'yxat:")
ll.display()
ll.delete(20)
print("20 o'chirilgandan keyingi ro'yxat:")
ll.display()
ll.delete(99)
Bog'langan ro'yxat:
5 -> 10 -> 20 -> 30 -> None
20 o'chirilgandan keyingi ro'yxat:
5 -> 10 -> 30 -> None
99 topilmadi.

8)class ShoppingCart:
    def __init__(self):
        self.items = {}
    def add_item(self, name, price, quantity=1):
        if name in self.items:
            old_price, old_qty = self.items[name]
            self.items[name] = (price, old_qty + quantity)
        else:
            self.items[name] = (price, quantity)
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            print(f"{name} savatda topilmadi.")
    def get_total_price(self):
        return sum(price * qty for price, qty in self.items.values())
    def show_cart(self):
        if not self.items:
            print("Savat bo'sh.")
            return
        print("Savatdagilar:")
        for name, (price, qty) in self.items.items():
            print(f"- {name}: {qty} dona x {price} = {qty * price} so'm")
        print(f"Umumiy narx: {self.get_total_price()} so'm")
cart = ShoppingCart()
cart.add_item("Non", 4000, 2)
cart.add_item("Sut", 8000)
cart.add_item("Yog'", 18000, 1)
cart.show_cart()
cart.remove_item("Sut")
print("\nSut o'chirilgandan keyin:")
cart.show_cart()
print("\nJami narx:", cart.get_total_price(), "so'm")
Savatdagilar:
- Non: 2 dona x 4000 = 8000 so'm
- Sut: 1 dona x 8000 = 8000 so'm
- Yog': 1 dona x 18000 = 18000 so'm
Umumiy narx: 34000 so'm
Sut o'chirilgandan keyin:
Savatdagilar:
- Non: 2 dona x 4000 = 8000 so'm
- Yog': 1 dona x 18000 = 18000 so'm
Umumiy narx: 26000 so'm
Jami narx: 26000 so'm

9)class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return "Xato: stek bo‘sh!"
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return "Stek bo‘sh!"
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
    def display(self):
        if self.is_empty():
            print("Stek bo‘sh.")
        else:
            print("Stekdagi elementlar (ustki -> pastki):")
            for item in reversed(self.items):
                print(item)
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.display()
print("Ustki element:", my_stack.peek())
print("Chiqarilgan element:", my_stack.pop())
my_stack.display()
Stekdagi elementlar (ustki -> pastki):
30
20
10
Ustki element: 30
Chiqarilgan element: 30
Stekdagi elementlar (ustki -> pastki):
20
10

10)class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            return "Xato: navbat bo‘sh!"
        return self.items.pop(0)
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if self.is_empty():
            return "Navbat bo‘sh!"
        return self.items[0]
    def size(self):
        return len(self.items)
    def display(self):
        if self.is_empty():
            print("Navbat bo‘sh.")
        else:
            print("Navbatdagi elementlar (birinchi -> oxirgi):")
            for item in self.items:
                print(item)
my_queue = Queue()
my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
my_queue.display()
print("Birinchi element:", my_queue.peek())
print("Chiqarilgan:", my_queue.dequeue())
my_queue.display()                
Navbatdagi elementlar (birinchi -> oxirgi):
A
B
C
Birinchi element: A
Chiqarilgan: A
Navbatdagi elementlar (birinchi -> oxirgi):
B
C

11)class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so'm depozit qilindi.")
        else:
            print("Notogri miqdor.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so'm yechildi.")
        else:
            print("Yetarli mablag' mavjud emas yoki notogri miqdor.")
    def get_balance(self):
        return self.balance
class Bank:
    def __init__(self):
        self.accounts = {}
    def create_account(self, name, initial_balance=0):
        if name in self.accounts:
            print(f"{name} uchun hisob allaqachon mavjud.")
        else:
            self.accounts[name] = Account(name, initial_balance)
            print(f"{name} uchun yangi hisob yaratildi.")
    def deposit_to_account(self, name, amount):
        if name in self.accounts:
            self.accounts[name].deposit(amount)
        else:
            print(f"{name} hisob topilmadi.")
    def withdraw_from_account(self, name, amount):
        if name in self.accounts:
            self.accounts[name].withdraw(amount)
        else:
            print(f"{name} hisob topilmadi.")
    def show_balance(self, name):
        if name in self.accounts:
            balance = self.accounts[name].get_balance()
            print(f"{name} hisobida: {balance} so'm mavjud.")
        else:
            print(f"{name} hisob topilmadi.")
    def show_all_accounts(self):
        if not self.accounts:
            print("Bankda hech qanday hisob mavjud emas.")
            return
        print("Bankdagi barcha hisoblar:")
        for name, acc in self.accounts.items():
            print(f"- {name}: {acc.get_balance()} so'm")
my_bank = Bank()
my_bank.create_account("Ali", 100000)
my_bank.create_account("Vali", 50000)
my_bank.deposit_to_account("Ali", 25000)
my_bank.withdraw_from_account("Vali", 30000)
my_bank.show_balance("Ali")
my_bank.show_balance("Vali")
my_bank.show_all_accounts()
Ali uchun yangi hisob yaratildi.
Vali uchun yangi hisob yaratildi.
25000 so'm depozit qilindi.
30000 so'm yechildi.
Ali hisobida: 125000 so'm mavjud.
Vali hisobida: 20000 so'm mavjud.
Bankdagi barcha hisoblar:
- Ali: 125000 so'm
- Vali: 20000 so'm

  

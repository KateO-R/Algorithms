class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. Nothing to peek.")
            return None

    def search(self, item):
        """Поиск элемента в стеке. Возвращает индекс элемента или -1, если не найден."""
        try:
            return len(self.items) - self.items[::-1].index(item) - 1
        except ValueError:
            return -1

    def display(self):
        """Вывод всех элементов стека."""
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack contains:")
            for item in reversed(self.items):
                print(f"| {item} |")
            print("-----")

# Демонстрация работы стека с различными типами данных
stack = Stack()

# Проверка на пустоту
print("Is stack empty?", stack.is_empty())

# Добавление целых чисел
stack.push(1)
stack.push(2)
stack.push(3)
print("Is stack empty?", stack.is_empty())
print("Top of the stack:", stack.peek())

# Отображение стека
stack.display()

# Добавление строк
stack.push("Hello")
stack.push("World")
stack.display()

# Добавление кортежей
stack.push((4, 5))
stack.push((6, 7))
stack.display()

# Поиск элемента
item_to_search = "Hello"
index = stack.search(item_to_search)
if index != -1:
    print(f"Element '{item_to_search}' found at index {index}.")
else:
    print(f"Element '{item_to_search}' not found in the stack.")

# Извлечение элементов
stack.pop()
stack.display()
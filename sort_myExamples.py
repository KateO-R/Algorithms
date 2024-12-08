# Сортировка выбором (Selection Sort)
words = ['I', 'best', 'do', 'immediately', 'things']

def selection_sort_by_length(arr):
   for i in range(len(arr)):
       min_index = i
       for j in range(i+1, len(arr)):
           if len(arr[j]) < len(arr[min_index]):
               min_index = j
       arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort_by_length(words)
print(words)


# Быстрая сортировка (Quick Sort)
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):  # Сравнение на основе цены
        return self.price < other.price

    def __eq__(self, other):  # Проверка равенства цены
        return self.price == other.price

    def __repr__(self):  # Для удобного вывода объектов
        return f"{self.name} ({self.price})"

items = [Item("Apple", 100), Item("Banana", 50), Item("Cherry", 75)]

def quick_sort(s):
    if len(s) <= 1:
        return s

    element = s[0]
    left = [i for i in s if i < element]      # Использует __lt__
    center = [i for i in s if i == element]  # Использует __eq__
    right = [i for i in s if i > element]    # Использует __lt__ в обратном порядке

    return quick_sort(left) + center + quick_sort(right)

sorted_items = quick_sort(items)
print(sorted_items)
from copy import deepcopy

list1 = [2,1,3,4,5]
print(len(list1), max(list1), min(list1), sum(list1), sorted(list1), sorted(list1, reverse=True), sum(list1)/len(list1))
list2 = ["b","a","c","d","e"]
# print(len(list2), max(list2), min(list2), sum(list2), sorted(list2), sorted(list2, reverse=True), sum(list2)/len(list2))
print([1,2,3]+[4,5])
print(["a","b","c"]*3)
print("a" in ["a","b","c"])
del list1[2]
print(list1)
list2.append("f")
print(list2)
list2.extend(list1)
print(list2)
list2.insert(5, 777)
print(list2)
list2.remove(777)
print(list2)
list2.pop(3)
print(list2)
print(list2.count(2))
print(list2.index(2))
list1.sort()
print(list1)
list2.reverse()
print(list2)
list3 = list2.copy() # поверхностно
deepcopy(list3) # глубокая копия
print(list3)
list3.clear()
print(list3)

list4 = list()
list5 = []
print(list4, list5)

list4 = list([1,2,3,4])
list5 = [1,2,3,4]
print(list4, list5)

print("12345"[2], list("12345"))
iterator = iter(list5)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# list6 = input("Введите целые числа через пробел").split()
# print(list6)
# map применяет функцию int ко всем элементам list6
# list7 = list(map(int, list6))
# print(list7)

numbers = [num for num in range(1, 101)]
print(numbers)
letters = [letter * 3 for letter in 'string' if letter != 'r']
print(letters)
print(letters[1:3])
print(letters[::-1])
print(letters[:2:3])
print(len(letters))
print('sss' in letters)
letters.append('hhh')
print(letters)
letters.extend(['bbb', 'aaa'])
print(letters)
letters.insert(3, 'lll')
print(letters)
print(letters + ['bbb', 'aaa'])
letters.remove('aaa')
print(letters)
print(letters.pop(3))
print(letters.pop())
print(letters)
print(letters.count('iii'))
print(letters.index('ggg'))

print([1,2,3] == [1,2,3])
print([1,2,3] != [1,2,3])
print([10,2,3] > [1,20,3]) # по элементам, первый который удовлетворяет, возвращает True

# кортежи
cake = ('c','a','k','e') # менять нельзя
tpl = tuple([1,2,3,4,4]) # создает кортеж из списка
print(tpl.count('e'))
print(len(tpl), len(cake))
print(any(tpl), any(cake))
print(max(cake))
print(min(cake))
print(sum(tpl))
print(sorted(cake))
# добавление нового элемента возможно только через создание нового кортежа
print(''.join(cake))
letter1, letter2, letter3, letter4 = cake
print(letter1, letter2, letter3, letter4)
print('c' in cake)

# множества
empty_set = set()
numbers_set = {10,20,30,40,50}
numbers_set_2 = {10,20,30,60,80}
numbers_set_3 = {10,20,30}
numbers_set_4 = {70,80,90}
print(empty_set, numbers_set)
print(set(tpl)) # дубли пропали
frozenset(numbers_set)
print(numbers_set, frozenset(numbers_set))
gen_set = {i**2 for i in range(1,20)}
print(gen_set)
print(numbers_set.issubset(numbers_set_2), numbers_set_2.issubset(numbers_set), numbers_set_3.issubset(numbers_set))
print(numbers_set.issuperset(numbers_set_3))
print(numbers_set.isdisjoint(numbers_set_4)) # общие элементы отсутствуют
print(numbers_set == numbers_set, numbers_set == numbers_set_2)
print(numbers_set.union(numbers_set_4))
print(numbers_set.intersection(numbers_set_2))
print(numbers_set.difference(numbers_set_2))
print(numbers_set.symmetric_difference(numbers_set_2))
print(numbers_set.copy())

print('!!!', numbers_set & numbers_set_2)
print(numbers_set | numbers_set_2)
print(numbers_set ^ numbers_set_2)

# меняем множество
numbers_set.update(numbers_set_2)
print(numbers_set)
numbers_set.intersection_update(numbers_set_2)
print(numbers_set)
numbers_set.difference_update(numbers_set_2)
print(numbers_set)
numbers_set.symmetric_difference_update(numbers_set_2)
print(numbers_set)
numbers_set.add(100)
print(numbers_set)
numbers_set.remove(100)
print(numbers_set)
numbers_set.discard(100) # удалить элемент если он в массиве
print(numbers_set)
numbers_set.pop()
print(numbers_set)
numbers_set.clear()
print(numbers_set)

# Словарь
dictionary = {"a": 1, 'b': 2, 'c': 3, 'd': 4}
dictionary_2 = dictionary.copy()
print(dictionary_2)
dictionary_2.clear()
print(dictionary, dictionary_2)
print(dictionary.fromkeys(['a', 'b']))
print(dictionary.setdefault('a'))
print(dictionary.items())
print(dictionary.keys())
print(dictionary.pop('a'), dictionary.popitem(), dictionary)
dictionary.update({'a': 1})
print(dictionary)
print(dictionary.values())
print(dictionary['a'], dictionary.get('a'))
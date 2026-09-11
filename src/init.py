import numpy as np

lst = [11, 22, 33, 44, 55, 66, 77, 88, 99]
mass = np.array(lst, dtype=np.int32)
print(mass)
print(len(mass))
print(sum(mass))
print(mass[2])
print(mass[[4,2,7,0,1]]) # выводит набор по индексам
print(mass[mass > 50])
print(2*mass+10) # применяется ко всем элементам массива
gen_X = np.arange(12)
print(gen_X)
matrix_gen_X = gen_X.reshape(3, 4)
print(matrix_gen_X)
print(matrix_gen_X.tolist()[1][1], matrix_gen_X.tolist())
gen_random = np.random.randint(150, 500, size=(5,5))
print(gen_random)
print(gen_random.min(axis=0)) #по столбцам
print(gen_random.min(axis=1)) #по строкам
print(gen_random.mean(axis=0)) #среднее
a = np.arange(48).reshape(4,3,4)
print(a)
print(a.ndim) # размерность
print(a.shape) # размер
print(a.size)
b = a + 1

print(b, b+a)

a = np.array([[1, 20, 0, 6],
              [5, 4, 7, 8.0],
              [9, 0, 110,0],
              [2, 4, 5, 6]])
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))
print(np.sin(45))
print(np.cos(90))
print(np.tan(45))
a = np.array([[1, 20, 0, 6],
              [5, 4, 7, 8.0],
              [9, 0, 110,0],
              [2, 4, 5, 6]])
print(np.sqrt(a))
print(np.sqrt(25))

a = np.zeros((2, 4), int)
print(a)

a = np.ones((2, 3))
print(a)


a = np.array([[1, 2, 3, 4.0],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
b = np.copy(a)
print(b)
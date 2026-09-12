import pandas as pd #dataframe
import numpy as np #матрицы
import seaborn as sns #визуализация
import gdown as gd #google download

np.random.seed(42)
df = pd.DataFrame({
    'City': ['Moscow', 'SPb', 'Kazan', 'Moscow', 'SPb', 'Kazan'] * 2,
    'Product': ['A', 'B', 'A', 'C', 'B', 'C'] * 2,
    'Sales': np.random.randint(100, 500, 12),
    'Quantity': np.random.randint(1, 10, 12)
})
print(df)

# -------- Простое условие --------
# Обычный способ
filtered1 = df[df['Sales'] > 300]
# Через query
filtered1_q = df.query('Sales > 300')

print("\nПродажи > 300:")
print(filtered1)
print(filtered1_q)

# -------- Несколько условий --------
# Обычный способ (скобки! скобки!)
filtered2 = df[(df['City'] == 'Moscow') & (df['Sales'] > 200)]
# Через query (чистота!)
filtered2_q = df.query('City == "Moscow" and Sales > 200')

print("\nМосква и Sales > 200:")
print(filtered2_q)

# -------- Использование IN --------
cities = ['Moscow', 'Kazan']
filtered3 = df.query('City in @cities')
print("\nТолько Москва и Казань:")
print(filtered3)

# -------- Работа со строками --------
df['Product_name'] = ['Apple', 'Banana', 'Apple', 'Cherry', 'Banana', 'Cherry'] * 2
filtered5 = df.query('Product_name.str.contains("a", case=False)')
print("\nТовары с буквой 'a' в названии:")
display(filtered5)

# python ./src/init.py
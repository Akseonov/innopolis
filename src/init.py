import pandas as pd
import numpy as np
import seaborn as sns
import gdown as gd

print(pd.__version__)

num_list = [1,3,5,np.nan,6,8]
numbers_series = pd.Series(num_list, name = 'numbers')
print(numbers_series)
frame = numbers_series.to_frame(name = 'numbers')
print(frame)

letter_list = ['a', 'b', 'c', 'd', 'e', np.nan]
letter_series = pd.Series(letter_list, name='letters')
print(letter_series)

print(pd.concat([numbers_series, letter_series], axis=1))

df_other = pd.DataFrame({
    'numbers': numbers_series,
    'letters': letter_series
})
print(df_other)

dates = pd.date_range('20260218', periods=450,freq='MS')

numbers_for_df = np.random.randn(450, 4)

df = pd.DataFrame(numbers_for_df, index=dates, columns=['A','B','C','D'])
print(df)

file = pd.read_csv("src/panda_data/5f6ce129fddc4ca0952f5e520e5f5bf8.csv", index_col=0)
print(file)

file_1 = sns.load_dataset('tips')
print(file_1)

file_1.to_csv("src/panda_data/test.csv", index=False)

url = "https://drive.google.com/uc?id=1SA_V8uaKydrWJVaqUk3EJL1wjQD6CEvb"
gd.download(url, 'src/panda_data/user_data.csv', quiet=True)

# file_1.columns = [1,2,3,4,5,6,7] # переименовать колонки
print(file_1)
print(file_1.head(3))
# print(file_1[2])

print(file_1.T)
file_1.sort_index(axis=0, ascending=False) # по умолчанию axis=0, т.е. сортировка по строкам
file_1.sort_values(by=['total_bill'], ascending=False) # по умолчанию сортировка по индексу, выбрали столбцы
print(file_1.sort_values(by=['total_bill'], ascending=False))
# python ./src/init.py
import pandas as pd
import numpy as np


#data 
numbers = [20,30,40,50]
letters = ["a","b","c","d"]
scalar = 5
dict =  {"a":10,"b":20,"c":30,"d":40}
random_numbers = np.random.randint(1,100,6)
# veri analizi yapar
#seri oluşturma pd series
pandas_series = pd.Series(numbers)
pandas_series =  pd.Series(letters)
pandas_series = pd.Series(5,[0,1,2,3])
pandas_series = pd.Series(numbers,["a","b","c","d"])
pandas_series = pd.Series(dict)
pandas_series = pd.Series(random_numbers)
pandas_series = pd.Series([20,30,40,50],["a","b","c","d"])
#indeksler
result = numbers[0]
result = numbers[-1]
result = numbers[:2]
result = pandas_series["a"]
result = pandas_series["d"]
result = pandas_series[["a","c"]]
#boyut
result = pandas_series.ndim
#type
result = pandas_series.dtype
#shape kaç boyutlu
result = pandas_series.shape
#elemanları toplama
result = pandas_series.sum()
#minimum
result = pandas_series.min()
# maximum
result = pandas_series.max()
#liste elemanlarını toplama
result = pandas_series+pandas_series
#liste elemanları + n
result = pandas_series+50
#liste elemanlarının karekök'ü 
result = np.sqrt(pandas_series)
#n' den büyükmü
result = pandas_series>=50
# n'nin mod 2 si
result = pandas_series %2 == 0
opel2018 = pd.Series([20,30,40,10],["ASTRA","CORSA","MOKKA","INSIGNIA"])
opel2019 = pd.Series([40,30,20,10],["ASTRA","CORSA","GRANDLAND","INSIGNIA"])
total = opel2018+opel2019
print(total)
print(total["ASTRA"])
print(pandas_series)
print(result)

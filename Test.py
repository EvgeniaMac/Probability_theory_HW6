import numpy as np
import scipy.stats as stats
import math

# Известно, что генеральная совокупность распределена нормально
# со средним квадратическим отклонением, равным 16.
# Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95,
# если выборочная средняя M = 80, а объем выборки n = 256.
# n=256
# srednee=80
# sigma=16
# z=1.96
# print([(srednee-z*sigma/np.sqrt(n)), (srednee+z*sigma/np.sqrt(n))])


# В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью,
# получены опытные данные:
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
# оценить истинное значение величины X при помощи доверительного интервала, покрывающего это
# значение с доверительной вероятностью 0,95.
# a=np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
# n=len(a)-1
# i=0.05
# t=stats.t.ppf(q=0.1-i/2, df=n)
# srednee=np.mean(a)
# dispersia=np.var(a, ddof=1)
# print([(srednee-t*np.sqrt(dispersia/n)), (srednee+t*np.sqrt(dispersia/n))])


# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.
a=np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
b=np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
n_a=len(a)
n_b=len(b)
n=n_a+n_b-2
i=0.05
t=stats.t.ppf(q=1-i, df=n)
print(t)
srednee_a=np.mean(a)
srednee_b=np.mean(b)
delta=srednee_a-srednee_b
d_a=np.var(a, ddof=1)
d_b=np.var(b, ddof=1)
d=(d_a+d_b)/2
se=np.sqrt(d/n_a+d/n_b)
print([(delta-t*se),(delta+t*se)])

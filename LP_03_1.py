# -*- coding: utf-8 -*-
bors = 2.97
things_bors = 100 // bors # Результат целое число без дроби и остатков
tips_bors = 100 % 2.97 # Результат остаток от деления
tips_bors = round(tips_bors, 2) # Округление числа до двух знаков
print ("Количество порций борща", things_bors)
print ("Чаевые с первого заказа", tips_bors)

pelmeni = 2.19
things_pelmeni = 100 // pelmeni
tips_pelmeni = 100 % pelmeni
tips_pelmeni = round(tips_pelmeni, 2)
print("Количество порций пельмений", things_pelmeni)
print("чаевые с пельмений", tips_pelmeni)

compote = 1.24
things_compote = 100 // compote
tips_compote = 100 % compote
tips_compote = round(tips_compote, 2)
print("Количество порций компота", things_compote)
print("чаевые с пельмений", tips_compote)
print("ЧАЕВЫЕ", tips_bors + tips_pelmeni + tips_compote)


# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:55:15 2024

@author: Aleksandr
"""
import json
import pandas as pd

# Работа с первым датасетом
with open('case_2_data_for_members.json', 'r', encoding='utf-8') as file:
    data_1 = json.load(file, )
#общий датасет с инфой по вакансиям и пользователям
print('общий датасет с инфой по вакансиям и пользователям')
data1 = pd.json_normalize(data_1,max_level=2)
print(data1.info())
"""
Проблемные колонки:
    failed_resumes
    confirmed_resumes
    vacancy.keywords - бред какойто
    vacancy.description, vacancy.comment - дохера текста
"""
# Обработка confirmed_resumes
print('Обработка confirmed_resumes')
data1_conf=pd.json_normalize(data_1[1]['confirmed_resumes'])
print(data1_conf.info())
print('Количество пользователей в группе confirmed_resumes:', len(data_1[1]['confirmed_resumes']))

# Выделение датасета с инфой по работе
print('Выделение датасета с инфой по работе')
data1_conf_exp=pd.json_normalize(data_1[1]['confirmed_resumes'][1]['experienceItem'])
print(data1_conf_exp.info())

# Выделение датасета с инфой по учебе

print('Выделение датасета с инфой по учебе')
data1_conf_exp=pd.json_normalize(data_1[1]['confirmed_resumes'][1]['educationItem'])
print(data1_conf_exp.info())

data1.to_csv("./data/raw_data.csv", index=False)


#-----------------------------------------------------
"""
with open('case_2_reference_without_resume_sorted.json', 'r', encoding='utf-8') as file:
    data_2 = json.load(file, )
data2=pd.json_normalize(data_2,max_level=2)
#print(data2.head())
#print(data2.info())
"""
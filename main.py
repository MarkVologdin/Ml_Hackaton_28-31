import json
import pandas as pd


# Загрузите JSON данные
with open('case_2_data_for_members.json', 'r', encoding='utf-8') as file:
    data = json.load(file, )

data1 = pd.json_normalize(data,max_level=2)
# Преобразуйте в Pandas DataFrame
specific_row = data1.iloc[1]
print(specific_row)

# Списки для хранения датафреймов
vacancy_dfs = []
failed_resumes_dfs = []
confirmed_resumes_dfs = []

# Обработка каждой вакансии в цикле
for vacancy_data in data:
    # Создание датафрейма для вакансии
    vacancy_df = pd.DataFrame(vacancy_data['vacancy'], index=[0])

    # Создание датафрейма для failed_resumes
    failed_resumes_df = pd.DataFrame(vacancy_data['failed_resumes'])
    failed_resumes_df['vacancy_id'] = vacancy_data['vacancy']['uuid']

    # Создание датафрейма для confirmed_resumes
    confirmed_resumes_df = pd.DataFrame(vacancy_data['confirmed_resumes'])
    confirmed_resumes_df['vacancy_id'] = vacancy_data['vacancy']['uuid']

    # Добавление датафреймов в списки
    vacancy_dfs.append(vacancy_df)
    failed_resumes_dfs.append(failed_resumes_df)
    confirmed_resumes_dfs.append(confirmed_resumes_df)

# Объединение всех датафреймов
all_vacancies_df = pd.concat(vacancy_dfs, ignore_index=True)
all_failed_resumes_df = pd.concat(failed_resumes_dfs, ignore_index=True)
all_confirmed_resumes_df = pd.concat(confirmed_resumes_dfs, ignore_index=True)

# Объединение confirmed и failed резюме
all_resumes_df = pd.concat([all_confirmed_resumes_df, all_failed_resumes_df], ignore_index=True)

# Вывод результатов
print("Данные о всех вакансиях:")
print(all_vacancies_df.head(1))
print("\nОбъединенные данные о резюме (confirmed и failed):")
for row in all_resumes_df:
    print(row)
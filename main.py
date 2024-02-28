import json
import pandas as pd

# Загрузите JSON данные
with open('case_2_data_for_members.json', 'r', encoding='utf-8') as file:
    data = json.load(file, )

data1 = pd.json_normalize(data,max_level=2)
# Преобразуйте в Pandas DataFrame
specific_row = data1.iloc[1]
print(specific_row)
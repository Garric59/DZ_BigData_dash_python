import pandas as pd
import numpy as np
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

data = pd.read_excel(DATA_PATH.joinpath("data.xlsx"))
# Создадим списки для фильтров
# ТБ
allTb = data['ТБ'].unique()
# Зоны простоя
typeUs = data['Тип УС'].unique()


# Формула расчета:
# Простои = (ОБСЛУЖИВАНИЕ УС + ОТМ + FLM + SLM + Средства + АДМ + ИТ)
# ФРВ – общий фонд работы устройства.
# Доступность сети = Простои/ФРВ в процентах

# Расчет ФРВ для конкретного банка
def frvTimeСalculation(tb=allTb):
    frvTime=[]
    for i in tb:
        frvTime.append(sum(data.loc[data['ТБ'].isin(tb)]['ФРВ']))
    return frvTime


# Рсчет простоев по всей сети или отделбному банку по всем зонам или отделбной зоне простоя
def downTimeСalculation(tb=allTb, typeUs=typeUs):
    downTime = []
    # downTime = data.loc[(data['ТБ'].isin(tb)) & (data['Тип УС'].isin(typeUs))]['Простой']
    for i in tb:
        downTime.append(sum(data.loc[(data['ТБ'].isin(tb)) & (data['Тип УС'].isin(typeUs))]['Простой']))
    return downTime


# Расчет доступности сети
def availabilityTimeСalculation(tb=allTb, typeUs=typeUs):
    availabilityTime = np.around([(1 - a/b)*100 for a, b in zip(downTimeСalculation(tb, typeUs), frvTimeСalculation(tb))], decimals=2)
    return availabilityTime

print(len(allTb))
print(len(frvTimeСalculation()))
print(len(downTimeСalculation()))

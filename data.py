import pandas as pd
import numpy as np

data = pd.read_excel("data/data.xlsx")
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
    frvTime = sum(data.loc[data['ТБ'].isin(tb)]['ФРВ'])
    return frvTime


# Рсчет простоев по всей сети или отделбному банку по всем зонам или отделбной зоне простоя
def downTimeСalculation(tb=allTb, typeUs=typeUs):
    downTime = data.loc[(data['ТБ'].isin(tb)) & (data['Тип УС'].isin(typeUs))]['Простой']
    return downTime


# Расчет доступности сети
def availabilityTimeСalculation(tb=allTb, typeUs=typeUs):
    availabilityTime = np.around((1 - downTimeСalculation(tb, typeUs) / frvTimeСalculation(tb)) * 100, decimals=2)
    return availabilityTime


print(downTimeСalculation())
#print(downTimeСalculation(['Красный банк'], ['RATM NAUTILUS']))

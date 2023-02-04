import copy
import time
import pandas as pd

from Train import Train
from generation import generate
from My_sortes import quick_sort
from My_sortes import merge_sort
from My_sortes import insert_sort

nums = [100, 250, 500, 750, 1000, 1250, 1500]

with pd.ExcelWriter("./trains.xlsx") as writer:
    for i in nums:
        pd.DataFrame(generate(i)).to_excel(writer, sheet_name=f"{i}", index=False)

trains = {}
for i in nums:
    curr = pd.read_excel('./trains.xlsx', sheet_name=f'{i}').to_dict('records')
    curr_trains = []
    for train in curr:
        curr_trains.append(
            Train(train['Дата отправления'], train['Время отправления'], train['Время в пути'], train['Номер поезда'],
                  train['Тип поезда'])
        )
    trains[i] = curr_trains

time_spend_insert = []
time_spend_quick = []
time_spend_merge = []

for j in nums:
    sorted_arrays = []

    sorted_arr_insert = copy.deepcopy(trains[j])
    start = time.time()
    insert_sort(sorted_arr_insert)
    end = time.time() - start
    time_spend_insert.append(end)
    sorted_arrays.append(sorted_arr_insert)

    sorted_arr_quick = copy.deepcopy(trains[j])
    start = time.time()
    quick_sort(sorted_arr_quick, 0, len(sorted_arr_quick) - 1)
    end = time.time() - start
    time_spend_quick.append(end)
    sorted_arrays.append(sorted_arr_quick)

    sorted_arr_merge = copy.deepcopy(trains[j])
    start = time.time()
    merge_sort(sorted_arr_merge, 0, len(sorted_arr_merge) - 1)
    end = time.time() - start
    time_spend_merge.append(end)
    sorted_arrays.append(sorted_arr_merge)

    for i in range(len(sorted_arrays)):
        final_dict = {}
        dates = []
        dep_time = []
        trav_time = []
        num = []
        type_ = []

        for t in sorted_arrays[i]:
            dates.append(t.date.strftime("%m/%d/%Y"))
            dep_time.append(t.dep_time)
            trav_time.append(t.trav_time)
            num.append(t.num)
            type_.append(t.type)
        final_dict['Дата отправления'] = dates
        final_dict['Время отправления'] = dep_time
        final_dict['Время в пути'] = trav_time
        final_dict['Номер поезда'] = num
        final_dict['Тип поезда'] = type_

        if i == 0:
            file_name = "./trains_sorted_insert.xlsx"
        elif i == 1:
            file_name = "./trains_sorted_quick.xlsx"
        else:
            file_name = "./trains_sorted_merge.xlsx"

        if j == 100:
            mode = 'w'
        else:
            mode = 'a'
        with pd.ExcelWriter(file_name, engine="openpyxl", mode=mode) as writer:
            pd.DataFrame(final_dict).to_excel(writer, sheet_name=f"{j}", index=False)

print(f'merge_time = {time_spend_merge}')
print(f'insert_time = {time_spend_insert}')
print(f'quick_time = {time_spend_quick}')

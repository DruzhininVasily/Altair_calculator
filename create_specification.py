from openpyxl import Workbook
from openpyxl.styles import PatternFill


def create_exel(data, static):
    exel_head = ['№', 'Наименование', 'Производитель', 'Артикул', 'Параметр', 'Количество', 'Цена шт.', 'Сумма']
    wb = Workbook()
    ws = wb.active
    ws.title = "Specification"
    ws.append(exel_head)
    for item in range(1, ws.max_column + 1):
        ws.cell(row=1, column=item).fill = PatternFill(fgColor="006CCDEC", fill_type='solid')
    ws.column_dimensions['A'].width = 4.22
    ws.column_dimensions['B'].width = 33
    ws.column_dimensions['C'].width = 13.11
    ws.column_dimensions['D'].width = 24.78
    ws.column_dimensions['E'].width = 12.56
    ws.column_dimensions['F'].width = 10.33
    ws.column_dimensions['G'].width = 10.33
    ws.column_dimensions['H'].width = 10.33
    data_set = set(data)
    data = list(data)
    out_data = []
    for j, i in enumerate(data_set):
        i = list(i)
        i.insert(-1, data.count(tuple(i)))
        i.insert(0, j+1)
        i.append(i[-2] * i[-1])
        out_data.append(i)
    index = out_data[-1][0]
    temp = [e.copy() for e in static]
    for i in range(len(temp)):
        index += 1
        temp[i].insert(0, index)
    out_data.extend(temp)
    print(out_data)
    for row in out_data:
        ws.append(row)
    wb.save('specification.xlsx')

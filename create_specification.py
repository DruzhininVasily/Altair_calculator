from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Side, Border
from openpyxl.drawing.image import Image
from datetime import date


def data_processing(data, static):
    data_set = set(data)
    out_data = []
    # Подсчет количества элементов
    for j, i in enumerate(data_set):
        i = list(i)
        i.insert(-1, data.count(tuple(i)))
        i.insert(0, j + 1)
        i.append(i[-2] * i[-1])
        out_data.append(i)
    # Добавление статических элементов
    index = out_data[-1][0]
    temp = [e.copy() for e in static]
    for i in range(len(temp)):
        index += 1
        temp[i].insert(0, index)
    out_data.extend(temp)
    # Разбитие элементов на группы
    panel_list = []
    kip_list = []
    for i in out_data:
        if 'Panel' in i:
            i.remove('Panel')
            panel_list.append(i)
        elif 'Kip' in i:
            i.remove('Kip')
            kip_list.append(i)
    return panel_list, kip_list


def create_ws(ws, title):
    exel_head = ['№', 'Наименование', 'Производитель', 'Артикул', 'Параметр', 'Количество', 'Цена шт.', 'Сумма']
    ws.title = title
    ws.append(exel_head)
    for item in range(1, ws.max_column + 1):
        ws.cell(row=1, column=item).fill = PatternFill(fgColor="006CCDEC", fill_type='solid')
    ws.column_dimensions['A'].width = 4.22
    ws.column_dimensions['B'].width = 33
    ws.column_dimensions['C'].width = 15.11
    ws.column_dimensions['D'].width = 24.78
    ws.column_dimensions['E'].width = 12.90
    ws.column_dimensions['F'].width = 10.33
    ws.column_dimensions['G'].width = 10.33
    ws.column_dimensions['H'].width = 10.33
    return ws


def add_sum(ws, target_sum):
    cell = ws.cell(column=ws.max_column, row=ws.max_row + 3)
    cell.value = target_sum
    cell = ws.cell(column=ws.max_column - 1, row=ws.max_row)
    cell.value = 'Сумма: '


def create_tcp(sheet, sum_elements, kip_list, panel_price):
    exel_head = ['Наименование', 'Артикул', 'Ед.изм', 'Стоимость за ед.', 'Количество', 'Итого']
    image = Image('static/image/Tcp_head.png')
    image.height = 150
    image.width = 325
    sheet.add_image(image, 'A1')
    font_1 = Font(size=12, bold=True, italic=True, name='Arial')
    font_2 = Font(size=11, italic=True, name='Arial')
    font_3 = Font(size=11, bold=True, italic=True, name='Arial')
    thins = Side(border_style="thin", color="000000")
    sheet.column_dimensions['A'].width = 79
    sheet.column_dimensions['B'].width = 25
    sheet.column_dimensions['C'].width = 8.5
    sheet.column_dimensions['D'].width = 21.1
    sheet.column_dimensions['E'].width = 14.3
    sheet.column_dimensions['F'].width = 12.9
    sheet.column_dimensions['G'].width = 36.5
    sheet['A10'].value = 'Проект: '
    sheet['A10'].font = font_1
    sheet['A11'].value = 'Исполнитель: '
    sheet['A11'].font = font_1
    sheet['A14'].value = 'Коммерческое предложение на автоматику от ' + str(date.today())
    sheet['A14'].font = font_1
    sheet['E12'].value = 'Итого: '
    sheet['E12'].font = font_1
    sheet['F12'].value = sum_elements
    sheet['F12'].font = font_1
    sheet['G18'].value = 'Примечание'
    sheet['G18'].font = font_3
    for i, j in enumerate(exel_head):
        sheet[18][i].value = j
        sheet[18][i].font = font_3
    for i, j in enumerate(kip_list):
        sheet[19 + i][0].value = j[1]
        sheet[19 + i][0].font = font_2
        sheet[19 + i][1].value = j[3]
        sheet[19 + i][1].font = font_2
        sheet[19 + i][2].value = 'шт'
        sheet[19 + i][2].font = font_2
        sheet[19 + i][3].value = j[6]
        sheet[19 + i][3].font = font_2
        sheet[19 + i][4].value = j[5]
        sheet[19 + i][4].font = font_2
        sheet[19 + i][5].value = j[7]
        sheet[19 + i][5].font = font_2
    sheet[sheet.max_row + 1][0].value = 'Шкаф управления автоматикой с ПЛК'
    sheet[sheet.max_row][0].font = font_2
    sheet[sheet.max_row][2].value = 'шт'
    sheet[sheet.max_row][2].font = font_2
    sheet[sheet.max_row][3].value = panel_price
    sheet[sheet.max_row][3].font = font_2
    sheet[sheet.max_row][4].value = 1
    sheet[sheet.max_row][4].font = font_2
    sheet[sheet.max_row][5].value = panel_price
    sheet[sheet.max_row][5].font = font_2
    for row in range(18, sheet.max_row + 1):
        for col in range(0, sheet.max_column):
            sheet[row][col].border = Border(top=thins, bottom=thins, left=thins, right=thins)


def create_exel(data, static):
    wb = Workbook()
    panel_list, kip_list = data_processing(data, static)
    # Запись элементов на в файл
    ws = wb.active
    create_ws(ws, 'Шкаф')
    sum_panel = 0
    kip_sum = 0
    for row in panel_list:
        sum_panel += float(row[-1])
        ws.append(row)
    add_sum(ws, sum_panel)
    if len(kip_list) > 0:
        ws1 = wb.create_sheet()
        create_ws(ws1, 'КИПиА')
        for row in kip_list:
            kip_sum += float(row[-1])
            ws1.append(row)
        add_sum(ws1, kip_sum)
    wb.save('specification.xlsx')
    wb1 = Workbook()
    sheet = wb1.active
    create_tcp(sheet, (sum_panel+kip_sum), kip_list, sum_panel)
    wb1.save('TCP.xlsx')

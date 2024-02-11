from openpyxl import Workbook


def create_exel(data):
    try:
        wb = Workbook()
        ws = wb.active
        ws.title = "Specification"
        for row in data:
            ws.append(row)
        wb.save('specification.xlsx')
    except Exception:
        pass

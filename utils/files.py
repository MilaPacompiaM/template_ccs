import os

from django.conf import settings

from openpyxl import load_workbook

from constants import example_file


class ExcelManager:

    @staticmethod
    def read_values(xls, datamap):
        """
        file = load_workbook(
            filename=os.path.join(
                settings.BASE_DIR, 'Ejemplo.xlsx'))
        """
        file = load_workbook('Ejemplo.xlsx')
        # sheet = file.worksheets[0]
        for field in datamap:
            print('1', field)
            sheet_num, row, col = field.get('position')
            sheet = file.worksheets[sheet_num - 1]
            value = sheet.cell(row - 1, col - 1).value
            print(field.get('name'), field.get('position'), 'value =', value)




if __name__ == '__main__':
    ExcelManager.read_values(None, example_file)
    # print("Table status:", movie_table.table_status)
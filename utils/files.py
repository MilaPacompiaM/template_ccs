from openpyxl import load_workbook, Workbook


class ExcelManager:

    @staticmethod
    def read_values(xls, datamap):
        """
        Reads cells specified in `datamap` from `xls`

        :param xls: binary Excel file
        :param datamap: list of fields to be read

        :return: dict
        """

        file = load_workbook(xls)
        valueset = {}
        for field in datamap:
            row, col = field.get('position')
            sheet = file.get_sheet_by_name(field.get('sheet'))
            value = sheet.cell(row, col).value
            valueset[field.get('name')] = value
        return valueset

    @staticmethod
    def write(values, datamap):
        """
        Writes static and dynamic data structured in `datamap`

        :param values: dict with dynamic or variable data
        :param datamap: dict with structure of data

        :return: Workbook
        """
        wb = Workbook()
        for field in datamap:
            key = field.get('key', None)
            value = values.get(key, None) if key else field.get('value', None)
            row, col = field.get('position')
            main_sheet = wb.worksheets[0]
            main_sheet.cell(row=row, column=col).value = value
        return wb

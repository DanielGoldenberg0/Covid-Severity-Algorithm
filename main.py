import xlrd
import xlwt

PATH = "test.xlsx"

workbook = xlrd.open_workbook(PATH)
worksheet = workbook.sheet_by_index(0)

patients = [
    {
        "id": {
            "symptoms": ["", "", ""],
            "age": "",
            "mild_signs": [],
            "intubated": "",
            "moderate_signs": [],
            "severe_signs": []
        }
    }
]


def read_data():
    for row in range(worksheet.nrows):
        if worksheet.cell_value(row, 0) != "ID":
            pass

    for val in ids:
        for col in range(worksheet.ncols):
            pass


def write_result():
    pass


def mild_severity():
    return False


def mild_with_risk_severity():
    return False


def moderate_severity():
    return False


def severe_severity():
    return False

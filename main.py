import xlrd
import xlwt

from patient import Patient

PATH = "test.xlsx"

wb = xlrd.open_workbook(PATH)
worksheet = wb.sheet_by_index(0)


patients: Patient = []


def read_data():
    for row in range(worksheet.nrows):
        if worksheet.cell_value(row, 0) != "Pt's #":
            patient = Patient()
            patients.append(patient)
            for col in range(worksheet.ncols):
                if "Symptom" in worksheet.cell_value(0, col) and worksheet.cell_value(row, col) != "na":
                    patients[row-1].symptoms.append(worksheet.cell_value(row, col))
                elif "Age" in worksheet.cell_value(0, col):
                    patients[row-1].age = int(worksheet.cell_value(row, col))
                elif ("CAD" in worksheet.cell_value(0, col)
                    or "DM" in worksheet.cell_value(0, col)
                    or "HTN" in worksheet.cell_value(0, col)
                    or "Transplant" in worksheet.cell_value(0, col)
                    or "Immunosuppresion" in worksheet.cell_value(0, col)):
                    patients[row-1].mild_signs.append(worksheet.cell_value(row, col))
                elif "Intubated" in worksheet.cell_value(0, col):
                    if worksheet.cell_value(row, col).lower() == "yes":
                        patients[row-1].intubated = True

def write_result():
    pass


def mild_severity(patient: Patient) -> bool:
    return False


def mild_with_risk_severity(patient: Patient) -> bool:
    return False


def moderate_severity(patient: Patient) -> bool:
    return False


def severe_severity(patient: Patient) -> bool:
    return False


read_data()
for patient in patients:
    patient: Patient
    print(patient.symptoms)
    print(patient.age)
    print(patient.mild_signs)
    print(patient.intubated)
    print("-----------------------------------------------")

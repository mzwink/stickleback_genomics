from xlrd import open_workbook
import os
def create_text_files():#excel_workbook):
    excel_workbook = input("Enter directory and filename of excel workbook: ")

    if excel_workbook.endswith(".xlsx") == False:
        excel_workbook = excel_workbook + ".xlsx"

    if os.path.isfile(excel_workbook):
        excel_workbook = open_workbook(excel_workbook)

    else:
        print("Error: File does not exist.")
    sheet_names = excel_workbook.sheet_names()

    for i in range(len(sheet_names)):
        sh = excel_workbook.sheets()[i]
        sh_name = sh.name #excel_workbook.sheet_by_name(sheet_names[i])

        output = open(sh_name + ".txt", 'w')

        num_rows = sh.nrows
        num_columns = sh.ncols

        for i in range(0, num_rows):
            for j in range(0, num_columns):
                if j == num_columns -1:
                    output.write(str(sh.cell_value(rowx=i, colx=j)) + "\n")
                else:
                    output.write(str(sh.cell_value(rowx=i, colx=j)) + "\t")
    print("Workbook converted to text files.")

create_text_files()

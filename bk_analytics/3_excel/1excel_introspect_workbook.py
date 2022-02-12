#!/usr/bin/env python3
import sys
from xlrd import open_workbook

input_file = "bk_analytics/3_excel/input/sales_2013.xls"

workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)

for worksheet in workbook.sheets():
    print("Worksheet name:", worksheet.name, "\tRows:",
          worksheet.nrows, "\tColumns:", worksheet.ncols)

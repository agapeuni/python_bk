#!/usr/bin/env python3
import pandas as pd

input_file = "bk_analytics/3_excel/input/sales_2013.xls"
output_file = "bk_analytics/3_excel/output/5output_pandas.xls"

important_dates = ['01/24/2013','01/31/2013']

df = pd.read_excel(input_file, 'january_2013', index_col=None)
df_set = df[df['Purchase Date'].isin(important_dates)]

writer = pd.ExcelWriter(output_file)
df_set.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
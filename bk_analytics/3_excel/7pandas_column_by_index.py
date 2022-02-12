#!/usr/bin/env python3
import pandas as pd

input_file = "bk_analytics/3_excel/input/sales_2013.xls"
output_file = "bk_analytics/3_excel/output/7output_pandas.xls"

df = pd.read_excel(input_file, 'january_2013', index_col=None)
df_index = df.iloc[:, [1, 4]]

writer = pd.ExcelWriter(output_file)
df_index.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
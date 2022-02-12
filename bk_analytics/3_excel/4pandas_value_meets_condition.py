#!/usr/bin/env python3
import pandas as pd

input_file = "bk_analytics/3_excel/input/sales_2013.xls"
output_file = "bk_analytics/3_excel/output/4output_pandas.xls"

df = pd.read_excel(input_file, 'january_2013', index_col=None)
df_condition = df[df['Sale Amount'].astype(float) > 1400.0]

writer = pd.ExcelWriter(output_file)
df_condition.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()

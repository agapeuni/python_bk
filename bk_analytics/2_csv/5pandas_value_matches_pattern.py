#!/usr/bin/env python3
import pandas as pd

input_file = "bk_analytics/2_csv/supplier_data.csv"
output_file = "bk_analytics/2_csv/5pandas_file.csv"

df = pd.read_csv(input_file)
df_pattern = df.loc[df['Invoice Number'].str.startswith("001-"), :]
df_pattern.to_csv(output_file, index=False)

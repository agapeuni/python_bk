#!/usr/bin/env python3
import pandas as pd

input_file = "bk_analytics/2_csv/supplier_data_unnecessary_header_footer.csv"
output_file = "bk_analytics/2_csv/11pandas_file.csv"

data_frame = pd.read_csv(input_file, header=None)

data_frame = data_frame.drop([0, 1, 2, 16, 17, 18])
data_frame.columns = data_frame.iloc[0]
data_frame = data_frame.reindex(data_frame.index.drop(3))

data_frame.to_csv(output_file, index=False)

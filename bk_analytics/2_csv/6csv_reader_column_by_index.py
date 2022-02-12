#!/usr/bin/env python3
import csv

input_file = "bk_analytics/2_csv/supplier_data.csv"
output_file = "bk_analytics/2_csv/6output_file.csv"

my_columns = [0, 3]

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		for row_list in filereader:
			row_list_output = [ ]
			for index_value in my_columns:
				row_list_output.append(row_list[index_value])
			filewriter.writerow(row_list_output)
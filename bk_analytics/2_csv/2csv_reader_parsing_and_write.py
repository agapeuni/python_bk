#!/usr/bin/env python3
import csv
import sys

input_file = "bk_analytics/2_csv/supplier_data.csv"
output_file = "bk_analytics/2_csv/2output_file.csv"

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')
        for row_list in filereader:
            print(row_list)
            filewriter.writerow(row_list)

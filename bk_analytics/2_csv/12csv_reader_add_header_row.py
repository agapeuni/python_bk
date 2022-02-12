#!/usr/bin/env python3
import csv

input_file = "bk_analytics/2_csv/supplier_data_no_header_row.csv"
output_file = "bk_analytics/2_csv/12output_file.csv"

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header_list = ['Supplier Name', 'Invoice Number',
                       'Part Number', 'Cost', 'Purchase Date']
        filewriter.writerow(header_list)
        for row in filereader:
            filewriter.writerow(row)

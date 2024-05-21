# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"C392600","system":"readv2"},{"code":"C390A00","system":"readv2"},{"code":"C395.00","system":"readv2"},{"code":"C391200","system":"readv2"},{"code":"C392700","system":"readv2"},{"code":"C391211","system":"readv2"},{"code":"C391.00","system":"readv2"},{"code":"C391012","system":"readv2"},{"code":"65617.0","system":"readv2"},{"code":"48293.0","system":"readv2"},{"code":"21975.0","system":"readv2"},{"code":"35682.0","system":"readv2"},{"code":"69184.0","system":"readv2"},{"code":"31322.0","system":"readv2"},{"code":"69854.0","system":"readv2"},{"code":"39800.0","system":"readv2"},{"code":"43653.0","system":"readv2"},{"code":"54203.0","system":"readv2"},{"code":"56108.0","system":"readv2"},{"code":"66073.0","system":"readv2"},{"code":"62598.0","system":"readv2"},{"code":"93936.0","system":"readv2"},{"code":"93892.0","system":"readv2"},{"code":"72804.0","system":"readv2"},{"code":"54904.0","system":"readv2"},{"code":"106788.0","system":"readv2"},{"code":"73131.0","system":"readv2"},{"code":"62328.0","system":"readv2"},{"code":"50526.0","system":"readv2"},{"code":"42439.0","system":"readv2"},{"code":"31541.0","system":"readv2"},{"code":"48307.0","system":"readv2"},{"code":"8548.0","system":"readv2"},{"code":"15137.0","system":"readv2"},{"code":"60758.0","system":"readv2"},{"code":"69373.0","system":"readv2"},{"code":"16295.0","system":"readv2"},{"code":"65603.0","system":"readv2"},{"code":"68440.0","system":"readv2"},{"code":"66386.0","system":"readv2"},{"code":"62236.0","system":"readv2"},{"code":"92569.0","system":"readv2"},{"code":"18701.0","system":"readv2"},{"code":"57161.0","system":"readv2"},{"code":"94120.0","system":"readv2"},{"code":"3129.0","system":"readv2"},{"code":"57322.0","system":"readv2"},{"code":"18700.0","system":"readv2"},{"code":"60026.0","system":"readv2"},{"code":"49542.0","system":"readv2"},{"code":"44147.0","system":"readv2"},{"code":"60880.0","system":"readv2"},{"code":"103977.0","system":"readv2"},{"code":"50665.0","system":"readv2"},{"code":"48035.0","system":"readv2"},{"code":"66857.0","system":"readv2"},{"code":"10955.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('immunodeficiencies-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["immunodeficiencies---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["immunodeficiencies---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["immunodeficiencies---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

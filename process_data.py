import csv
import numpy as np
import pandas as pd


def process_results (file,column_index):
    with open('files/'+file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        list_of_office_names = []
        list_of_candidate_names = []
        # open the csv and read the first and second rows to store as office and candidate names
        for i, row in enumerate(csv_reader):
            if i == 0:
                list_of_office_names.append(row)
            elif i == 1:
                list_of_candidate_names.append(row)


    df = pd.read_csv ('files/'+file)
    # remove the first column
    df = df.tail(-1)
    # create blank precinct and output lists
    precinct_list = []
    output_list = []
    # save the second row (first of the new df as the precinct list)
    for index in range(df.shape[1]):
        columnSeriesObj = df.iloc[:, index]
        if index == 1:
            precinct_list=list(columnSeriesObj.values)

    # I dumbly store these lists as lists in a blank list, so unpacking
    list_of_candidate_names=list_of_candidate_names[0]
    list_of_office_names=list_of_office_names[0]

    # looping through each column in the dataframe
    for index in range(df.shape[1]):
        columnSeriesObj = df.iloc[:, index]
        # start with the fifth column (where candidate results start)
        if index>column_index:
            # combine the precinct list with the votes cast values of the column
            combined_row = list(zip(precinct_list,list(columnSeriesObj.values)))
            for x in combined_row:
                # add in candidate and office for each row, then append the list to the output list
                final_row = list(x+(list_of_office_names[index],list_of_candidate_names[index]))
                output_list.append(final_row)

    #print(output_list)
    # convert the output list to a dataframe and output to csv
    df = pd.DataFrame(output_list,columns=['precinct','votes','office','candidate'])
    df.to_csv('processed/processed_'+file, index=False)


process_results('johnson_hd.csv',3)
process_results('sedgwick_hd.csv',1)
process_results('shawnee_hd.csv',1)
process_results('wyandotte_hd.csv',1)

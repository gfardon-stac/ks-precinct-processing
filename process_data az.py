import csv
import pandas as pd


def process_results (file,column_index):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        list_of_office_names_first = []
        #list_of_candidate_names = []
        # open the csv and read the first and second rows to store as office and candidate names
        for i, row in enumerate(csv_reader):
            if i == 0:
                list_of_office_names_first.append(row)
            #elif i == 1:
            #    list_of_candidate_names.append(row)
    
   

    df = pd.read_csv(file, low_memory=False)
    ## remove the first column
    ##df = df.tail(-1)
    ## create blank precinct and output lists
    county_list = []
    precinct_list = []
    output_list = []
    # # save the first column as the precinct list)
    for index in range(df.shape[1]):
        columnSeriesObj = df.iloc[0:, index]
        if index == 0:
            county_list=list(columnSeriesObj.values)
    ## save the second column as the county list)
    for index in range(df.shape[1]):
        columnSeriesObj = df.iloc[0:, index]
        if index == 1:
            precinct_list=list(columnSeriesObj.values)
    ## I dumbly store these lists as lists in a blank list, so unpacking
    #list_of_candidate_names=list_of_candidate_names[0]
    list_of_office_names=list_of_office_names_first[0]
    #previous_office = '' 
    #for office in list_of_office_names_raw:
    #    
    #    if office:
    #        previous_office = office.strip().replace("\n", " - ")
    #        list_of_office_names.append(office.strip().replace("\n", " - "))
    #    if not office:
    #        list_of_office_names.append(previous_office)
    #print (list_of_office_names)

    ## looping through each column in the dataframe
    for index in range(df.shape[1]):
        columnSeriesObj = df.iloc[0:, index]
        #print(columnSeriesObj)
        # start with the column_index column (where candidate results start)
        if index>column_index:
            # combine the precinct list with the votes cast values of the column
            combined_row = list(zip(county_list,precinct_list,list(columnSeriesObj.values)))
            #print(combined_row[0])
            for x in combined_row:
                # add in candidate and office for each row, then append the list to the output list
                #print(list_of_office_names[index])
                final_row = list(x)
                final_row.append(list_of_office_names[index].strip())
                #print(final_row)
                output_list.append(final_row)
#
    ##print(output_list)
    ## convert the output list to a dataframe and output to csv
    df = pd.DataFrame(output_list,columns=['county','precinct','votes','office'])
    print(df.iloc[:5])
    df.to_csv('processed_'+file, index=False)
#
#
process_results('2022_statewide.csv',1)

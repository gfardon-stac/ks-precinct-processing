import csv
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
    #df = df.tail(-1)
    # create blank precinct and output lists
    county_list = []
    precinct_list = []
    output_list = []
     # save the first column (first of the new df as the precinct list)
    for index in range(df.shape[1]):
        columnSeriesObj = df.iloc[:, index]
        if index == 0:
            county_list=list(columnSeriesObj.values)
    # save the second column (first of the new df as the precinct list)
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
            combined_row = list(zip(county_list,precinct_list,list(columnSeriesObj.values)))
            for x in combined_row:
                # add in candidate and office for each row, then append the list to the output list
                final_row = list(x+(list_of_office_names[index],list_of_candidate_names[index]))
                output_list.append(final_row)

    #print(output_list)
    # convert the output list to a dataframe and output to csv
    df = pd.DataFrame(output_list,columns=['county','precinct','votes','office','candidate'])
    df.to_csv('processed/processed_'+file, index=False)


process_results('beaver.csv',1)
process_results('box_elder.csv',1)
process_results('cache.csv',1)
process_results('carbon.csv',1)
process_results('daggett.csv',1)
process_results('davis.csv',1)
process_results('duchesne.csv',1)
process_results('emery.csv',1)
process_results('garfield.csv',1)
process_results('grand.csv',1)
process_results('iron.csv',1)
process_results('juab.csv',1)
process_results('kane.csv',1)
process_results('millard.csv',1)
process_results('morgan.csv',1)
process_results('piute.csv',1)
process_results('rich.csv',1)
process_results('salt lake.csv',1)
process_results('san juan.csv',1)
process_results('sanpete.csv',1)
process_results('sevier.csv',1)
process_results('summit.csv',1)
process_results('tooele.csv',1)
process_results('uintah.csv',1)
process_results('utah.csv',1)
process_results('wasatch.csv',1)
process_results('washington.csv',1)
process_results('wayne.csv',1)
process_results('weber.csv',1)


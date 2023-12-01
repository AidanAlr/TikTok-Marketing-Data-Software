import csv
import json


def csv_to_json(csv_file_path, json_file_path='output json'):
    # create a dictionary
    data_dict = {}

    # Step 2
    # open a csv file handler
    with open(csv_file_path, encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)

        # convert each row into a dictionary
        # and add the converted data to the data_variable

        for rows in csv_reader:
            # assuming a column named 'index'
            # to be the primary key
            key = rows['index']
            data_dict[key] = rows

    # open a json file handler and use json.dumps
    # method to dump the data
    # Step 3
    return data_dict


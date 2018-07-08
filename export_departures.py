import requests
import json
import sys
import datetime
import csv

def filter_departures(filter_category=None, filter_date=None):
    """calls the api on /departures, receives the data of all departures, and
    filters them according to category (set by the filter_category argument)
    and start_date (set by the filter_date argument).

    Returns the filtered list.
    """


    all_departures = []

    resp = requests.get('http://localhost:8000/departures')

    # go through the data of the first page, then keep calling the remaining pages
    while 1:
        if resp.status_code != 200:
            raise requests.ConnectionError('Received status {}'.format(resp.status_code))

        departures_page = resp.json()

        all_departures.extend(departures_page['results'])

        # call the url of the next page of departures and breaks if not found
        if not departures_page['next']:
            break
        else:
            resp = requests.get(departures_page['next'])

    category = filter_category

    #set the start_date by the given string, and report error in case of exception
    try:
        start_date = datetime.datetime.strptime(filter_date,'%Y-%m-%d').date()
    except ValueError as e:
        errno, strerror = e.args
        print("Value error({0}): {1}".format(errno,strerror))


    # list comprehension of the result list, where the data is filtered by category and start date
    selected_departures = [d for d in all_departures if d['category']==category and
                           datetime.datetime.strptime(d['start_date'],'%Y-%m-%d').date()>start_date]

    return selected_departures


def export_to_csv(filter_category='Adventurous', filter_date='2018-06-01',
                  file_name='departures.csv'):
    """ calls filter_departures, sending it the arguments, and receives the resulting data,
    then exports it to a csv file.

    The category defaults to 'Adventurous' unless spicified
    The start_date defaults to '2018-06-01' unless spicified
    The output file name defaults to 'departures.csv' unless spicified
    """

    departures = filter_departures(filter_category, filter_date)

    try:
        with open(file_name,'w',newline='') as out_file:
            writer = csv.writer(out_file)
            # write the titles row, in title-case, and with underscores replaced with spaces
            headers = [k.title().replace('_',' ') for k in departures[0].keys()]
            writer.writerow(headers)

            #write the remaining data
            for departure in departures:
                writer.writerow(departure.values())

    except IOError as e:
        errno, strerror = e.args
        print("I/O error({0}): {1}".format(errno,strerror))


if __name__=='__main__':
    export_to_csv()


















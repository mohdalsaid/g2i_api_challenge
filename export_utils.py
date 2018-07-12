import csv

import response_processing


def export_to_csv(filter_category='Adventurous', filter_date='2018-06-01',
                  file_name='departures.csv'):
    """ calls filter_departures, sending it the arguments, and receives the resulting data,
    then exports it to a csv file.

    The category defaults to 'Adventurous' unless spicified
    The start_date defaults to '2018-06-01' unless spicified
    The output file name defaults to 'departures.csv' unless spicified
    """

    departures = response_processing.filter_departures(filter_category, filter_date)

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

export_to_csv()

if __name__=='__main__':
    export_to_csv()


















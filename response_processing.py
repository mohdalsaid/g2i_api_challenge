import json
import datetime

import api_services

def filter_departures(filter_category=None, filter_date=None):
    """calls the get_departures function , receives the data of all departures,
    and filters them according to category (set by the filter_category argument)
    and start_date (set by the filter_date argument).

    Returns the filtered list.
    """


    all_departures = []

    resp = api_services.get_departures('http://localhost:8000/departures')

    # go through the data of the first page, then keep calling the remaining pages
    while 1:
        if not resp:
            raise requests.ConnectionError('Received status {}'.format(resp.status_code))
            break

        departures_page = resp.json()
        if not departures_page:
            return []

        all_departures.extend(departures_page['results'])

        # call the url of the next page of departures and breaks if not found
        if not departures_page['next']:
            break
        else:
            resp = api_services.get_departures(departures_page['next'])

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

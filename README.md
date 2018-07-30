# trips_api

A module to consume the departures API response data, filter the results, and export the final results to a csv file.

There are two functions in the module:

filter_departures(filter_category=None, filter_date=None)

Which calls the API, receives the response, and filters the results based on the category and start date, and returns the result as a list.

and

export_to_csv(filter_category=None, filter_date=None, file_name=None)

Which calls filter_departures(), receives the filtered departures list, and exports the data to a csv file.

TODO:
- Currently the order of the columns in the csv file is random, as this is how the dictionary keys in Python 3 operate, currently thinking of a way to change this without changing the PYTHONHASHSEED environment variable (since this is discouraged in production due to security concerns)


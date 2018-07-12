import json
import unittest
from unittest.mock import Mock, patch

from response_processing import filter_departures

class ProcessingTest(unittest.TestCase):

    def test_response_processing(self):

        response = [
            {"name": "New Zealand Safari", "start_date": "2018-04-03",
             "finish_date": "2018-04-13", "category": "Marine"},

            {"name": "New Zealand Encompassed", "start_date": "2018-08-31",
             "finish_date": "2018-09-10", "category": "Adventurous"},

            {"name": "Bali Overland", "start_date": "2018-04-03",
             "finish_date": "2018-04-13", "category": "Classic"},

            {"name": "Galapagos Overland", "start_date": "2018-08-31",
             "finish_date": "2018-09-10", "category": "Marine"}
        ]

        expected_marine_january = [
                {"name": "New Zealand Safari", "start_date": "2018-04-03",
             "finish_date": "2018-04-13", "category": "Marine"},

                {"name": "Galapagos Overland", "start_date": "2018-08-31",
             "finish_date": "2018-09-10", "category": "Marine"}
            ]

        expected_marine_june = [
            {"name": "Galapagos Overland", "start_date": "2018-08-31",
         "finish_date": "2018-09-10", "category": "Marine"}
        ]

        expected_marine_april_4 = [
            {"name": "Galapagos Overland", "start_date": "2018-08-31",
         "finish_date": "2018-09-10", "category": "Marine"}
        ]

        expected_classic_no_date = []

        expected_classic_march = [
            {"name": "Bali Overland", "start_date": "2018-04-03",
         "finish_date": "2018-04-13", "category": "Classic"},
        ]

        expected_no_args = [
            {"name": "Galapagos Overland", "start_date": "2018-08-31",
         "finish_date": "2018-09-10", "category": "Marine"}
        ]

        with patch('api_services.get_departures') as mock_get_dep:

            mock_get_dep.json.return_value = response

            self.assertListEqual(expected_marine_january, filter_departures(filter_category ='Marine',
                                                                                 filter_date = '2018-01-01'))

            self.assertListEqual(expected_marine_june, filter_departures(filter_category ='Marine',
                                                                              filter_date = '2018-06-01'))

            self.assertListEqual(expected_marine_april_4, filter_departures(filter_category ='Marine',
                                                                                 filter_date = '2018-04-04'))

            self.assertListEqual(expected_classic_no_date, filter_departures(filter_category ='Classic'))

            self.assertListEqual(expected_classic_march, filter_departures(filter_category = 'Classic',
                                                                                filter_date = '2018-03-01'))

            self.assertListEqual(expected_no_args, filter_departures())


if __name__ == "__main__":
    unittest.main()

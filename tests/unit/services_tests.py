import unittest
from unittest.mock import Mock, patch

from api_services import get_departures


class ServicesTest(unittest.TestCase):

    def test_get_departures(self):
        with patch('api_services.requests.get') as mock_get:
            # Configure the mock to return a response with an OK status code.
            mock_get.return_value.status_code = 200

            # Call the service, which will send a request to the server.
            response = get_departures('')

            self.assertEqual(response.status_code,200)


if __name__ == "__main__":
    unittest.main()

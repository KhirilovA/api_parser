import unittest
from api_parser import api_parse


class UnitTests(unittest.TestCase):
    def test_arrangement(self):
        actual = api_parse('https://jsonplaceholder.typicode.com/todos/1')
        expected = {
                  "userId": 1,
                  "id": 1,
                  "title": "delectus aut autem",
                  "completed": False
                }
        self.assertEqual(actual, expected,
                         'Expected different output when calling "api_parse()" \
                         with https://jsonplaceholder.typicode.com/todos/1')

        actual = api_parse('https://jsonplaceholder.typicode.com/users/1')
        expected = {
                  "id": 1,
                  "name": "Leanne Graham",
                  "username": "Bret",
                  "email": "Sincere@april.biz",
                  "address": {
                    "street": "Kulas Light",
                    "suite": "Apt. 556",
                    "city": "Gwenborough",
                    "zipcode": "92998-3874",
                    "geo": {
                      "lat": "-37.3159",
                      "lng": "81.1496"
                    }
                  },
                  "phone": "1-770-736-8031 x56442",
                  "website": "hildegard.org",
                  "company": {
                    "name": "Romaguera-Crona",
                    "catchPhrase": "Multi-layered client-server neural-net",
                    "bs": "harness real-time e-markets"
                  }
                }
        self.assertEqual(actual, expected,
                         'Expected different output when calling "api_parse()"\
                          with https://jsonplaceholder.typicode.com/users/1')


if __name__ == "__main__":
    unittest.main()

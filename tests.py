import unittest
import requests
import consts

SERVER = f'http://{consts.SERVER_ROUTE["url"]}:{consts.SERVER_ROUTE["port"]}'

DATA_TEST = [
    {
        "sold_at": "2026-01-02 00:00:00",
        "customer": {
            "document": "0000000000",
            "name": "JOSE DA SILVA",
        },
        "total": "100.00",
        "products": [
            {
                "type": "A",
                "value": "50.00",
                "qty": 1,
            },
            {
                "type": "B",
                "value": "50.00",
                "qty": 1
            }
        ]
    },
    {
        "sold_at": "2026-01-02 00:00:00",
        "customer": {
            "document": "53824051079",
            "name": "CARLOS SANTOS",
        },
        "total": "100.00",
        "products": [
            {
                "type": "A",
                "value": "50.00",
                "qty": 1,
            },
            {
                "type": "B",
                "value": "50.00",
                "qty": 1
            }
        ] 
    },
    {
        "sold_at": "2026-01-02 00:00:00",
        "customer": {
            "document": "53824051079",
            "name": "ANDRE MAIA",
        },
        "total": "100.00",
        "products": [
            {
                "type": "A",
                "value": "50.00",
                "qty": 1,
            },
            {
                "type": "B",
                "value": "50.00",
                "qty": 1
            }
        ]    
    },
    {
        "sold_at": "2026-01-02 00:00:00",
        "customer": {
            "document": "53824051079",
            "name": "PEDRO PERES",
        },
        "total": "100.00",
        "products": [
            {
                "type": "A",
                "value": "50.00",
                "qty": 1,
            },
            {
                "type": "B",
                "value": "50.00",
                "qty": 1
            }
        ]
    }
]


class TestStringMethods(unittest.TestCase):
    def test_get(self):
        response = requests.get(f'{SERVER}/api/cashback')
        self.assertEqual(response.status_code, 405)
    
    def test_post_no_body(self):
        response = requests.post(f'{SERVER}/api/cashback')
        self.assertEqual(response.status_code, 400)
        
    def test_cpf_error(self):
        response = requests.post(f'{SERVER}/api/cashback', json=DATA_TEST[1])
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.content, b'{"status":"Date invalid"}')
    
    
if __name__ == '__main__':
    unittest.main()
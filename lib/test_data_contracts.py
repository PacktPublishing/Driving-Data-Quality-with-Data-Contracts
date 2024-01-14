import unittest

from data_contracts import DataContract


class TestDataContracts(unittest.TestCase):
    maxDiff = None

    def test_invalid_contract(self):
        with self.assertRaises(ValueError):
            DataContract("../contracts/Customer-invalid.yaml")

    def test_name(self):
        data_contract = DataContract("../contracts/Customer.yaml")
        self.assertEqual(data_contract.name(), 'Customer')

    def test_bigquery_schema(self):
        data_contract = DataContract("../contracts/Customer.yaml")

        expected = """[
  {
    "name": "id",
    "type": "STRING",
    "description": "The unique identifier for the customer.",
    "mode": "REQUIRED"
  },
  {
    "name": "name",
    "type": "STRING",
    "description": "The name of the customer.",
    "mode": "REQUIRED"
  },
  {
    "name": "email",
    "type": "STRING",
    "description": "The email address of the customer.",
    "mode": "REQUIRED"
  },
  {
    "name": "language",
    "type": "STRING",
    "description": "The language preference of the customer."
  }
]"""
        actual = data_contract.bigquery_schema()
        self.assertEqual(actual, expected)

    def test_json_schema(self):
        data_contract = DataContract("../contracts/Customer.yaml")

        expected = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "Customer",
            "description": "A customer of our e-commerce website.",
            "type": "object",
            "properties": {
                "id": {
                    "description": "The unique identifier for the customer.",
                    "type": "string"
                },
                "name": {
                    "description": "The name of the customer.",
                    "type": "string"
                },
                "email": {
                    "description": "The email address of the customer.",
                    "type": "string",
                    "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                },
                "language": {
                    "description": "The language preference of the customer.",
                    "type": "string",
                    "enum": [
                        "en",
                        "fr",
                        "es"
                    ]
                }
            },
            "required": [
                "id",
                "name",
                "email"
            ],
            "additionalProperties": True
        }
        actual = data_contract.json_schema()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

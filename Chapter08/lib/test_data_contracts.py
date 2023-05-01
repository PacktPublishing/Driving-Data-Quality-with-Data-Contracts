import unittest

from data_contracts import DataContract


class TestDataContracts(unittest.TestCase):
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
        actual = data_contract.bigquerySchema()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

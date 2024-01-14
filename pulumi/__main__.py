import sys
sys.path.append("../lib/")

from data_contracts import DataContract

import pulumi
from pulumi_gcp import bigquery

data_contract = DataContract("../contracts/Customer.yaml")

dataset = bigquery.Dataset(
    "dataProductsDataset",
    dataset_id="data_products",
    friendly_name="Data Products",
    description="A dataset to hold our teams data products.",
)

customer_table = bigquery.Table("customerTable",
    dataset_id=dataset.dataset_id,
    table_id=data_contract.name(),
    deletion_protection=False,
    schema=data_contract.bigquery_schema())

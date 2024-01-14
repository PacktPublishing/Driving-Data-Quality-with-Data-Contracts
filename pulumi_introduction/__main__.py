import pulumi
from pulumi_gcp import bigquery

default_dataset = bigquery.Dataset(
    "defaultDataset",
    dataset_id="pulumi_introduction",
    friendly_name="Pulumi Introduction",
    description="This is an example description",
)
default_table = bigquery.Table(
    "defaultTable",
    dataset_id=default_dataset.dataset_id,
    table_id="my_table",
    deletion_protection=False,
    schema="""[
  {
    "name": "id",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "The ID"
  },
  {
    "name": "state",
    "type": "STRING",
    "description": "State where the head office is located"
  }
]
""")

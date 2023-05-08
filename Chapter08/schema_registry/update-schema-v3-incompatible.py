#!/usr/bin/env python

# This script uses the Confluent Python libraries to attempt to register our
# `Customer-v3-incompatible.yaml` schema to our schema registry. It will fail
# due to the compatibility checks performed by the schema registry and throw an
# exception.

import sys
sys.path.append("../lib/")

from data_contracts import DataContract
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.schema_registry_client import Schema
import json

data_contract = DataContract("../contracts/Customer-v3-incompatible.yaml")

client = SchemaRegistryClient({"url": "http://localhost:8081"})
schema = Schema(json.dumps(data_contract.json_schema()), schema_type='JSON')
result = client.register_schema(data_contract.name(), schema)

print(f"Updated schema `{data_contract.name()}` with ID of {result}")

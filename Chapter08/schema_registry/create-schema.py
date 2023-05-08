#!/usr/bin/env python

# This script uses the Confluent Python libraries to register our
# `Customer.yaml` schema to our schema registry.

import sys
sys.path.append("../lib/")

from data_contracts import DataContract
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.schema_registry_client import Schema
import json

data_contract = DataContract("../contracts/Customer.yaml")

client = SchemaRegistryClient({"url": "http://localhost:8081"})
schema = Schema(json.dumps(data_contract.json_schema()), schema_type='JSON')
result = client.register_schema(data_contract.name(), schema)

print(f"Registered schema `{data_contract.name()}` with ID of {result}")

#!/usr/bin/env python

import sys
sys.path.append("lib/")

import json
from data_contracts import DataContract

data_contract = DataContract("contracts/Customer.yaml")

output_file = 'customer.schema.json'
with open(output_file, 'w') as writer:
    writer.write(json.dumps(data_contract.json_schema(), indent=2))
    print(f'Written JSON Schema of `{data_contract.name()}` data contract to `{output_file}`')

#!/usr/bin/env python

import yaml

with open("contracts/Customer-invalid.yaml", "r") as stream:
    contract = yaml.safe_load(stream)

if 'owner' not in contract:
    raise ValueError(f'`{contract["name"]}` contract does not have an owner')

print(
    f'Successfully parsed the `{contract["name"]}` contract, which is owned by `{contract["owner"]}`.')

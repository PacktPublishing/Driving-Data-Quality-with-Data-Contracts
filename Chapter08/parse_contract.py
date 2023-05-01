#!/usr/bin/env python

import yaml

with open("contracts/Customer.yaml", "r") as stream:
    contract = yaml.safe_load(stream)

print(
    f'Successfully parsed the `{contract["name"]}` contract, which is owned by `{contract["owner"]}`.')

#!/usr/bin/env python

import sys
sys.path.append("lib/")

from data_contracts import DataContract
from jsonschema import validate
from jsonschema.exceptions import ValidationError

events = [
    # Valid events
    {"id": "DC12", "name" : "Andrew", "email" : "andrew@data-contracts.com", "language": "en"},
    {"id": "DC13", "name" : "Deborah", "email" : "deborah@data-contracts.com"},
    # Missing email, which is a required field
    {"id": "DC14", "name" : "Bukayo", "language": "en"},
    # Email does not pass regex validation
    {"id": "DC15", "name" : "Bukayo", "email" : "bukayo", "language": "en"},
    # `nl` is not a valid language code
    {"id": "DC16", "name" : "Vivianne", "email" : "vivianne@data-contracts.com", "language": "nl"},
]

data_contract = DataContract("contracts/Customer.yaml")

for event in events:
    try:
        validate(event, data_contract.json_schema())
        print(f"✅ Successfully validated event {event}")
    except ValidationError as e:
        print(f"❗ Error validating event {event}\n{e}")

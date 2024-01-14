#!/usr/bin/env python

import sys
sys.path.append("lib/")

from data_contracts import DataContract

# Anonymize the event based on the rules specified in the data contract
def anonymize(event: dict, data_contract: DataContract):
    anonymized = event.copy()
    for name, metadata in data_contract.fields().items():
        if 'anonymization_strategy' in metadata:
            if metadata['anonymization_strategy'] == 'email':
                anonymized[name] = f"anonymized+{event['id']}@data-contracts.com"
            if metadata['anonymization_strategy'] == 'hex':
                anonymized[name] = event[name].encode("utf-8").hex()

    return anonymized

events = [
    {"id": "DC12", "name" : "Andrew", "email" : "andrew@data-contracts.com", "language": "en"},
    {"id": "DC13", "name" : "Deborah", "email" : "deborah@data-contracts.com"},
    {"id": "DC14", "name" : "Bukayo", "email" : "bukayo@data-contracts.com", "language": "en"},
]

data_contract = DataContract("contracts/Customer.yaml")

for event in events:
    anonymized = anonymize(event, data_contract)
    print(f"Anonymizing:\t{event}\n\t\t{anonymized}")

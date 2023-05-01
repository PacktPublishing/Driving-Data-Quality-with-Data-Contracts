import yaml
import json


class DataContract:
    '''
    An object containing a data contract.

    Args:
        path (str): The path to the data contract YAML file
    '''
    def __init__(self, path: str):
        with open(path, "r") as stream:
            self.contract = yaml.safe_load(stream)

    def name(self) -> str:
        '''
        Returns:
            The name of the data contract.
        '''
        return self.contract['name']

    def bigquerySchema(self) -> str:
        '''
        Generate a BigQuery schema from the data contract.

        Returns:
            The BigQuery schema as JSON
        '''
        bq_schema = []
        for name, metadata in self.contract['fields'].items():
            schema = {
                'name': name,
                'type': metadata['type'].upper(),
                'description': metadata['description']
            }
            if 'required' in metadata and metadata['required'] is True:
                schema['mode'] = 'REQUIRED'
            bq_schema.append(schema)

        return json.dumps(bq_schema, indent=2)

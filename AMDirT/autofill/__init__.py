from AMDirT.validate.domain import DatasetValidator
from AMDirT.core import get_json_path
import json


def autofill(project_accession, table_name=None, schema=None, dataset=None):

    if schema is None and dataset is None:
        json_conf = get_json_path()
        with open(json_conf) as c:
            tables = json.load(c)
            samples = tables["samples"]
            samples_schema = tables["samples_schema"]
            libraries = tables["libraries"]
            libraries_schema = tables["libraries_schema"]
        if table_name not in samples:
            raise Exception("Table name not found in AncientMetagenomeDir file")
    else:


    

    sample = DatasetValidator(
        schema=samples_schema[table_name], dataset=samples[table_name]
    )
    libraries = DatasetValidator(
        schema=libraries_schema[table_name], dataset=libraries[table_name]
    )

    libraries.to_rich()

    sample_df = sample.dataset.iloc[:0, :].copy()
    libraries_df = libraries.dataset
    print(libraries)


if __name__ == "__main__":
    autofill("ancientmetagenome-hostassociated", "PRJNA791766")

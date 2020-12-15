import pkg_resources
import numpy as np
import pandas as pd


def load_food_metadata():
    """
    Return: a dataframe containing Global FoodOmics ontology and metadata.
    """
    stream = pkg_resources.resource_stream(__name__, 'data/foodomics_multiproject_metadata.txt')
    gfop_metadata = pd.read_csv(stream, sep='\t')
    # Remove trailing whitespace
    gfop_metadata = gfop_metadata.apply(lambda col: col.str.strip()
                                        if col.dtype == 'object' else col)
    return gfop_metadata


def get_sample_types(simple_complex=None):
    """
    Return:
        Global FoodOmics ontology containing only simple, only complex, or all foods.
    Args:
        simple_complex (string): one of 'simple', 'complex', or 'None'.
                                Simple foods are single ingredients while complex foods contain multiple ingredients.
                                'None' will return both simple and complex foods.
    """
    gfop_metadata = load_food_metadata()
    if simple_complex is not None:
        gfop_metadata = gfop_metadata[gfop_metadata['simple_complex'] == simple_complex]
    col_sample_types = [f'sample_type_group{i}' for i in range(1, 7)]
    return (gfop_metadata[['filename', *col_sample_types]]
            .set_index('filename'))

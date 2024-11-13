import json
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

def convert_to_dict(dict_str):
    """
    Convert a string representation of a dictionary to a dictionary object.
    Args:
        dict_str (str): String representation of a dictionary.
        
    Returns:
        dict (dict): A dictionnary.
    """
    if not isinstance(dict_str, str):
        return dict_str
    
    dict_str = dict_str.replace("'", '"')
    try:
        return json.loads(dict_str)
    except json.JSONDecodeError as e:
        return {} 
    
def create_ethnicity_list(data_str):
    if not data_str:
        return []
    new = data_str\
        .replace('ans', 'an')\
        .replace('people', '')\
        .replace('peoples', '')\
        .replace('names', '')\
        .replace('culture', '')\
        .replace(' of', '')\
        .replace(' the', '')\
        .replace(' and', '')\
        .replace(' in', '')\
        .replace(' to', '')\
        .replace('United States', 'United_States')\
        .replace('United Kingdom', 'United_Kingdom')\
        .replace('Puerto Rican', 'Puerto_Rican')\
        .replace('Afro', 'African')\
        .replace('Afro-', 'African ')\
        .replace('South African', 'South_African')
    return new.split()
        

    
def categorize_release_season(date):
    """
    Categorize a release date into one of the following categories: Spring, Summer, Holiday, or Other.
    Args:
        date (datetime): The release date of a movie.
        
    Returns:
        str: The category of the release date.
    """
    if date.month in [6, 7, 8]:  # Summer months
        return 'Summer'
    elif date.month in [1, 12]:  # Winter holiday
        return 'Holiday'
    else:
        return 'Other'
    
def categorize_age_group(age):
    """
    Categorize a release date into one of the following categories: Spring, Summer, Holiday, or Other.
    Args:
        date (datetime): The release date of a movie.
        
    Returns:
        str: The category of the release date.
    """
    if age is None:
        return None
    if 0 <= age < 13:
        return 'child'
    elif age < 18:
        return 'teen'
    elif age < 35:
        return 'young_adult'
    elif age < 65:
        return 'adult'
    else:
        return 'senior'
    
def get_name_from_freebase_id(freebase_id):
    if not freebase_id:
        return None
    
    sparql = SPARQLWrapper("https://query.wikidata.org/bigdata/namespace/wdq/sparql", agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11")

    
    sparql.setQuery(f"""
        SELECT ?item ?itemLabel WHERE {{
        ?item wdt:P646 "{freebase_id}".
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
        }}
    """)
    
    sparql.setReturnFormat(JSON)
    
    try:
        results = sparql.query().convert()
        # results_df = pd.io.json.json_normalize(results['results']['bindings'])
        # print(results_df[['item.value', 'itemLabel.value']].head(1))
        if results["results"]["bindings"]:
            item_name = results["results"]["bindings"][0]["itemLabel"]["value"]
            return item_name
        else:
            return None
    except Exception as e:
        print(f"Error while consulting Freebase ID {freebase_id}: {e}")
        return None
import json
from textblob import TextBlob
from SPARQLWrapper import SPARQLWrapper, JSON

def get_day(date_str):
    """
    Get the day from a date string.
    Args:
        date_str (str): A date string in the format 'YYYY-MM-DD'.
        
    Returns:
        int: The day of the date.
    """
    if not isinstance(date_str, str):
        return date_str
    
    date = date_str.split('-')
    if len(date) < 3:
        return None
    return int(date[2])

def get_month(date_str):
    """
    Get the month from a date string.
    Args:
        date_str (str): A date string in the format 'YYYY-MM-DD'.
        
    Returns:
        int: The month of the date.
    """
    if not isinstance(date_str, str):
        return date_str
    
    date = date_str.split('-')
    if len(date) < 2:
        return None
    return int(date[1])

def get_year(date_str):
    """
    Get the year from a date string.
    Args:
        date_str (str): A date string in the format 'YYYY-MM-DD'.
        
    Returns:
        int: The year of the date.
    """
    if not isinstance(date_str, str):
        return date_str
    
    date = date_str.split('-')
    if len(date) < 1:
        return None
    return int(date[0])

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
    
def convert_to_list(dict_str):
    data = convert_to_dict(dict_str)
    if not isinstance(data, dict):
        return data
    
    return list(data.values())
    
    
def get_name_from_freebase_id(freebase_id):
    if not freebase_id:
        return None
    
    # Create a SPARQL wrapper object
    sparql = SPARQLWrapper("https://query.wikidata.org/bigdata/namespace/wdq/sparql", agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11")

    # Set the query
    sparql.setQuery(f"""
        SELECT ?item ?itemLabel WHERE {{
        ?item wdt:P646 "{freebase_id}".
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
        }}
    """)
    
    # Set the return format
    sparql.setReturnFormat(JSON)
    
    try:
        # Execute the query and parse the results
        results = sparql.query().convert()
        if results["results"]["bindings"]:
            item_name = results["results"]["bindings"][0]["itemLabel"]["value"]
            # Return the name of the item
            return item_name
        else:
            return None
    except Exception as e:
        print(f"Error while consulting Freebase ID {freebase_id}: {e}")
        return None
    
    
def create_genre_list(data):

    new_data = []
    
    for genre in data:
        # Clean genre names
        genre = genre.lower()\
            .replace('romantic', 'romance')\
            .replace('sci-fi', 'science-fiction')\
            .replace('science fiction', 'science-fiction')\
            .replace('comedy-drama', 'comedy drama')\
            .replace('period piece', 'period_piece')\
            .replace('computer animation', 'computer_animation')\
            .replace('glamorized spy', 'glamorized_spy')\
            .replace('time travel', 'time_travel')\
            .replace(' of ', '_of_')\
            .replace(' and ', '_and_')\
            .replace(' cinema', '')\
            .replace(' films', '')\
            .replace(' film', '')\
            .replace('film ', '')\
            .replace(' movies', '')\
            .replace(' movie', '')\
            .replace('/', ' ')
        new_genre = genre.split()

        new_data += new_genre

    # Remove duplicates
    new_data = list(set(new_data))

    return new_data

    
def create_ethnicity_list(data_str):
    if not data_str:
        return []

    # Clean ethnicity names
    new = data_str.lower()\
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
        .replace('united states', 'united_states')\
        .replace('united kingdom', 'united_kingdom')\
        .replace('puerto rican', 'puerto_rican')\
        .replace('afro', 'african')\
        .replace('afro-', 'african ')\
        .replace('south african', 'south_african')\
        .replace('african-american', 'african american')
    
    # Split the string into a list of ethnicity names
    return new.split()
        
    
def categorize_release_season(month):
    """
    Categorize a release date into one of the following categories: Spring, Summer, Holiday, or Other.
    Args:
        date: The release date of a movie.
        
    Returns:
        str: The category of the release date.
    """
    if not isinstance(month, float):
        return month

    elif month in [6, 7, 8]:  # Summer months
        return 'Summer'
    elif month in [1, 12]:  # Winter holiday
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
    if not isinstance(age, float):
        return age
    
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

def get_textblob_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment
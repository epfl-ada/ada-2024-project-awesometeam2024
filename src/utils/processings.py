import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import src.utils.data_utils as utils
from collections import Counter

CMU_DATA_PREPROCESSED_PATH = 'data/preprocessed/'

def process_plot_summaries(df_plots):
    assert df_plots['summary'].isnull().sum() == 0, "Missing values found in 'summary' column"
    assert df_plots['movie_id'].isnull().sum() == 0, "Missing values found in 'movie_id' column"

    # Average plot summary length
    df_plots['summary_length'] = df_plots['summary'].apply(len)
    print(df_plots['summary_length'].describe())

    df_plots.to_csv(CMU_DATA_PREPROCESSED_PATH + 'plot_summaries.csv', index=False)

    # summary lengths distribution
    plt.figure(figsize=(10,6))
    sns.histplot(df_plots['summary_length'], bins=50)
    plt.title('Distribution of Plot Summary Lengths')
    plt.xlabel('Summary Length (characters)')
    plt.ylabel('Frequency')
    plt.show()

    print(df_plots.sample(5))

def process_movie_metadata(df_movies):
    df_movies = df_movies.copy()

    # Removing freebase (deprecated)
    if 'freebase_movie_id' in df_movies.columns:
        df_movies.drop(columns=['freebase_movie_id'], inplace=True)

    df_movies = df_movies.dropna(subset=['box_office_revenue'])

    assert df_movies['box_office_revenue'].isnull().sum() == 0

    df_movies['languages'] = df_movies['languages'].apply(utils.convert_to_dict)
    df_movies['countries'] = df_movies['countries'].apply(utils.convert_to_dict)

    df_movies['release_month'] = df_movies['release_date'].apply(utils.get_month)
    df_movies['release_year'] = df_movies['release_date'].apply(utils.get_year)
    df_movies.drop(columns=['release_date'], inplace=True)

    df_movies = df_movies[df_movies['release_year'] >= 1900]

    df_movies['genres'] = df_movies['genres'].apply(utils.convert_to_list)
    print("Genres :", df_movies['genres'].explode(), "\n")

    # create_genre_list will convert the string to a list of genres. For a genre like "Action/Adventure", it will return ['Action', 'Adventure']
    df_movies['genres'] = df_movies['genres'].apply(utils.create_genre_list)

    df_movies.to_csv(CMU_DATA_PREPROCESSED_PATH + 'movie.metadata.csv', index=False)

    print("\n", df_movies.sample(5))

    return df_movies

def process_character_metadata(df_characters, df_movies):
    # Merge the character dataframe with the movie dataframe
    df_actors_revenues = df_characters.merge(df_movies[['wikipedia_movie_id', 'box_office_revenue']], how='inner')

    df_actors_revenues = df_actors_revenues[['wikipedia_movie_id', 'box_office_revenue', 'actor_gender', 'actor_ethnicity', 'actor_name', 'actor_age']]

    ethnicities = {}
    print("Ethnicities:")
    for ethnicity in df_actors_revenues['actor_ethnicity'].unique():
        # get_name_from_freebase_id will return the name of the ethnicity
        freebase_name = utils.get_name_from_freebase_id(ethnicity)

        if freebase_name:
            print(freebase_name)
            # create_ethnicity_list will split if multiple (i.e 'Asian American' -> ['Asian', 'American'])
            ethnicities[ethnicity] = utils.create_ethnicity_list(freebase_name)

    # Map the freebase ids to the actual names
    df_actors_revenues['actor_ethnicity'] = df_actors_revenues['actor_ethnicity'].map(ethnicities)

    df_actors_revenues.to_csv(CMU_DATA_PREPROCESSED_PATH + 'character.metadata.csv', index=False)

    print("\n", df_actors_revenues.sample(5))

    return df_actors_revenues
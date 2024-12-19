
# ADA to break the movie industry

## Abstract
Since the very beginning, the movie industry is continuously evolving to meet consumer demands and remain profitable. Key film attributes - such as genre, release date, and runtime — significantly influence box office revenue.
This study aims to investigate these factors to understand their influence on box office revenue, identifying the most common predictors of a film’s financial success.
Using the [CMU Movie Summary Corpus Dataset](https://www.cs.cmu.edu/~ark/personas/), we are first going to preprocess the data to extract and measure the quality of the data. Secondly, a first per-feature analysis will allow us to answer some basic questions to understand their impact separately. Then, we will investigate the correlation between these variables. Finally, this analysis will use ML models in order to create a predictive model for box office success based on historical data.
This approach helps pinpoint key factors driving financial success, providing insights into the elements that most impact a movie's performance.

## Data Story
The data story was made available with github pages and can be found [here](https://epfl-ada.github.io/ada-2024-project-awesometeam2024/).

## Research Questions

The questions are organized as milestones to guide our analysis, helping us systematically examine the factors that contribute to high box office revenue for a successful project outcome.

**Questions : understanding individual features and find correlation**
1. Release Season
    - How does **_release season_** correlate with box office revenue? Do films realeased in a specific season (e.g., summer, winter holiday, other) tend to perform better?
2. Genre
    - Which **_film genres_** have the highest average box office revenue? Are there genres that perform better than others?
3. Runtime
    - How does **_film runtime_** correlate with box office revenue? Do longer or shorter films tend to perform better?
4. Languages
    - How does **_film languages_** impact the box office revenue? Which languages have the highest average box office revenue?
5. Actors
    - Which **_actors_** appear in the films with the highest box office revenue? Does the presence of a specific actor influence box office revenue?

    1. Actors Age
        - What is the average box office revenue by **_actors' age group_** (child, teen, young adult, adult and senior)?
    2. Actors Gender
        - Does the **_gender distribution of actors_** in a film influence its average box office revenue?
        - What is the average box office revenue based on the **_gender predominance_** in the movie cast?
    3. Actors Ethnicity
        - What is the average box office revenue based on the **_ethnic diversity_** in the movie cast?
        - Does the **_ethnicity of the actors_** impact average box office revenue? Which ethnicities have the highest average box office revenue?
6. Evolution over time
    - How did **box office revenue** evolved over time? How was it for each **_genre_**?
    - How has **_runtime_** changed along the years and how it correlates with revenue?
7. Sentimental analysis
    - Are there specific schemes regarding the sentiment(s) present in the summary of success movies ? 
    - Is the dominant balance of feelings of a plot summary influence its success ?

**Output model** \
Gathering answers from the previous questions, this helps us choose one model for predicting the film success (on box office revenue). Nevertheless, we still have to choose the best one.
- Can we predict a new film’s success based on its genre, language, runtime, and cast?
- Which model is the best ?


Comparing the actual and predicted success results, it could provide insight into the key factors that influence financial success in the film industry

## Proposed Additional Datasets

To improve the models' predictive accuracy, we propose incorporating additional datasets. One such dataset is:

1. **Kaggle's Movie Financials Dataset**  
   - **Source**: [Kaggle - Movie Franchises Financial Data](https://www.kaggle.com/)  
   - **Details**: This dataset includes financial and technical data for movies, such as budgets, lifetime gross, release dates, ratings, runtimes, and user votes.  
   - **Purpose**: By integrating budget data, we refined our classification threshold for high-revenue movies, allowing us to differentiate between successful and underperforming movies more accurately.

## Methods

Our ultimate goal is to predict the success (on box office revenue) of a movie based on the correlation of multiple features. Here is a summary of techniques that we have used along the way :
- **Data preprocessing** : clean missing / inconsistent data
    - Movie metadata : 
        - remove irrelevant columns (e.g., freebase_movie_id)
        - remove films with box office revenue missing; 
        - separate date into year, month, day
        - drop outliers
        - separate genres into a list of genres (Action/Adventure -> [Action, Adventure])
    - Character metadata :
        - append the box office revenue of the correspondent movie
        - remove irrelevant columns (e.g., freebase_movie_id)
        - substitute Actor ethnicity Freebase ID by the corresponding name (e.g., /m/0x67 -> African Americans)
        - separate ethnicity into a list of ethnicities (African Americans -> [African, American])

- **Data visualization** : histogram, barplot, line plot to help catch trends and distribution of the data for the following features :
    - Release Season
    - Genre
    - Runtime
    - Languages
    - Actors
        - Age
        - Gender
        - Ethnicity
    - Evolution over time
    - Sentimental analysis

- **Data description** :
   - use confidence intervals to quantify uncertainty in our EDA
   - use Pearson's correlation to look for correlated variables

- **Modeling** :
    - Predict the box office revenue: Random Forest and Gradient Boosting
    - Predict the success of a movie (high revenue or low revenue): Logistic Regression and SVM
    - Features: runtime, release_year, is_holiday_release, num_actors, num_male_actors,num_female_actors, avg_actor_age

## Proposed timeline
This timeline defines milestones for our project but is not rigid. Often, we had to go back to the previous step when our findings revealed that we had to change our methods.

#### Step 1 : Define objectives
The goal here was to clearly state which questions we wanted to answer with this analysis and the outcome that we are looking for.

#### Step 2 : Data collection preprocessing
This step involved understanding and manipulating the data in order to be able to further analyze it. We came back multiple times to this step in order to improve our preprocessing pipeline.

#### Step 3 : Exploratory Data Analysis
We answered the first series of questions regarding the dataset in order to separately understand the influence of genre, runtime, actors gender and ethnicity on box office revenue.

#### Step 4 : Analysis of correlations between variables
After understanding how each feature independently affects the revenue, we must understand if a certain combination of these specific features can drastically improve the final outcome of the movie.

#### Step 5 : Define, apply and upgrade model for predictive analysis
Upon gathering all the knowledge from the previous step, we have to look for the best model for our ultimate goal. This involves testing its/their accuracy and try to improve it.

#### Step 6 : Communicate results
An important aspect of a data analysis project is to communicate the findings and synthesize the results for external people.

#### Step 7 : Find areas of improvements
We made choices during this analysis, either because of the time or because of what we thought was true at some point. The goal of this part is to come back on this choice in order to derive improvements on the current pipeline and model.

#### Step 8 : Define and select the information that we want to convey in our data story along with the plots
The extensive analysis allowed us to have a wide view of the context. In order to keep our data story the most interesting and complete, we have to choose which parts of the analysis are going to be included, in which order and with which plot.

#### Step 9 : Set up the website with github pages and Write our data story
The goal here is to step up the environnement to develop our data story the easiest way possible.

#### Step 10 : Integrate the interactive plots
This step is quite challenging since it requires the transposition of the initial matplotlib plots into nice dynamic plotly interactive plots.

#### Step 11 : Improve the notebook organization, add the sentimental analysis and improve the readme
The final step was the overall review of the content we have produced until now. Our goal is to organize well or work to maximize the information convey by our project. 

## Organization within the team

We organize ourselves with one leader for each task/step of the project and all other teammates also contribute and review. Here is a summary of the organization :

- **Nicolas** : Step 1 and 2 (Defining objectives and Data collection) + Step 8 and 9 + sentimental analysis
- **Andrea** : Step 3 (Exploratory Data Analysis) + Step 10 + organization within the team
- **Vasco** : Step 4 (Analysis of correlations between variables) + Step 11
- **Ahmed** : Step 5 (Define, apply and upgrade model for predictive analysis) + Step 10
- **Ines** : Step 6 and 7 (Communicate results and Find areas of improvements) + Step 11

For the data story we all contribute, increasing (and correcting potential mistakes) the work of the colleague who previously submitted.

## Quickstart

```bash
# clone project
git clone <project link>
cd <project repo>

# install requirements
pip install -r pip_requirements.txt

# open jupyter notebook results.ipynb in a code editor and run the cells
```

## Project Structure

The directory structure of new project looks like this:

```
├── data                        <- Project data files
│   ├── initial                         <- Initial data directory (CMU Movie Summary Corpus)
│   ├── new_data                        <- Additional data directory (Kaggle's Movie Financials)
│   ├── preprocessed                    <- Preprocessed data directory
│
├── src                         <- Source code
│   ├── data                            <- Data directory
│   ├── models                          <- Model directory
│   ├── utils                           <- Utility directory
│   ├── scripts                         <- Shell scripts
│
├── results.ipynb               <- a well-structured notebook showing the results
│
├── .gitignore                  <- List of files ignored by git
├── pip_requirements.txt        <- File for installing python dependencies
└── README.md                   <- Project description
```
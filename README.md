
# Your project name

## Abstract
Since the very beginning, the movies industry is continuously evolving to meet consumer demands and remain profitable. While every year bring its own technical improvements, key film attributes—such as genre, release date, and runtime—still significantly influence box office revenue.
This study aims to investigate these factors to understand their influence on box office revenue, identifying the most common predictors of a film’s financial success.
Using the [CMU Movie Summary Corpus Dataset](https://www.cs.cmu.edu/~ark/personas/), we are first going to preprocess the data to extract and measure the quality of the data. Secondly, a first per-feature analysis will allow us to answer some basic questions to understand the impact of each feature seperatly. In the 3rd part, we will investigate the correlation between these variables. Finally, this analysis will use ML models (eg. linear regression) in order to create a predictive model for box office success based on historical data. 
This approach helps pinpoint key factors driving financial success, providing insights into the elements that most impact a movie's performance.
- add key results
- add conclusion


<span style="color:blue">"You can make this approach broader to answer more questions beyond only training a predictive a model". 
Ideas: attribute recomendations? Like, given the genre and some other attributes, recommend a season for example</span>.

## Research Questions

The questions are organized as milestones to guide our analysis, helping us systematically examine the factors that contribute to high box office revenue for a successful project outcome.

**Questions : understanding individual features**
- What types of films generate the most revenue?
- Does a film’s runtime have an impact on its financial performance? 
- What periode is better for a movie release ? (eg. summer, holiday, others)
- Does ethnicity, age or gender of leading actors influences box office revenue ?
- How runtime affects revenue ?

**Questions : find correlation**
- Does the film language influences revenue in a specific country 
- Does some sountries prefer a specific genre ?
- How does these features have evolved over time ?
- TODO find more

**Output model** \
Gathering answers from the previous question, this helps us choosing one model for predicting box office revenue. Neverthe less, we still have to choose the best one.
- Can we predict a new film’s box office revenue based on its genre, language, runtime, and cast?
- Which model is the best ? 


Comparing the actual and predicted box office results, it could provide insight into the key factors that influence financial success in the film industry

## Proposed additional datasets

Our datasets after seems to be a bit short in order to feed our predictive model, we searched for other datasets such as [Movie Dataset: Budgets, Genres, Insights](https://www.kaggle.com/datasets/utkarshx27/movies-dataset/suggestions?status=pending&yourSuggestions=true) or [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/code).
After analyse these, we decide not to include them into the analysis because the fit was not interesting.

## Methods

Our ultimate goal is to predict the box office revenue of a movie based on the correlation of multiple features. For this purpose, we need to deeply understand the data and correlation between features. Here is a summary of techniques that we have used along the way :
- **Data preprocessing** : clean missing / inconsistent data
- **Data visualization** : histogram, barplot, lineplot to help catch trends and distribution of the data
- **Data description** : 
    - use confidence intervals to quantify uncertainty in our EDA
    - use Pearson's correlation to look for correlated variables
- 

## Proposed timeline
This timeline defines milestones for our project but is not rigid. Often, we had to go back to previous step when our findings revealed that we had to change our methods.

#### Step 1 : Define objectives
The goal here was to clearly state which questions we wnated to answer with this analysis and the outcome that we are looking for.

#### Step 2 : Data collection preprocessing
This step involved understanding and manipulate the data in order to be able to further analyse it. We came back multiple time to this step in order to improve our preprocessing pipeline.

#### Step 3 : Exploratory Data Analysis
We answered the first series of questions regarding the dataset in order to separatly understand the influence of genre, runtime, actors ethnicity on box office revenue.

#### Step 4 : Analysis of correlations between variables
After understanding how each feature independently affect the revenue, we must understand if a certain combination of these specific features can drastically improve the final outcome of the movie. For that, we should first try to find the correlation between : movie country and genres, movie language and countries. And then, see of it affect revenue.

#### Step 5 : Define, apply and upgrade model for predictive analysis
Upon gathering all the knowledge from the previous step, we have to look for the best model for our ultimate goal. This involve testing its/their accuracy and try to improve it.

#### Step 6 : Communicate results
An important aspect of a data analysis project is to communicate the findings and synthesize the results for external people.

#### Step 7 : Find areas of improvements
We made choices during this analysis, either because of the time or because of we we thought was true at some point. The goal of this part is to came back on this choice in order to derive improvements on the current pipeline and model. 

## Organization within the team

We organized oursleves with one leader for each task/step of the project and at least 3 teammates to review. Here is a summary of the organization :

- **Andrea** : Step 3
- **Ines** : Step 6 and 7
- **Vasco** : Step 4
- **Amed** : Step 5
- **Nicolas** : Step 1 and 2

## Quickstart

```bash
# clone project
git clone <project link>
cd <project repo>

# [OPTIONAL] create conda environment
conda create -n <env_name> python=3.11 or ...
conda activate <env_name>


# install requirements
pip install -r pip_requirements.txt
```

### How to use the library
Tell us how the code is arranged, any explanations goes here.

## Project Structure

The directory structure of new project looks like this:

```
├── data                        <- Project data files
│
├── src                         <- Source code
│   ├── data                            <- Data directory
│   ├── models                          <- Model directory
│   ├── utils                           <- Utility directory
│   ├── scripts                         <- Shell scripts
│
├── tests                       <- Tests of any kind
│
├── results.ipynb               <- a well-structured notebook showing the results
│
├── .gitignore                  <- List of files ignored by git
├── pip_requirements.txt        <- File for installing python dependencies
└── README.md
```


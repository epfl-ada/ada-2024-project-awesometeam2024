
# Your project name

## Abstract
This study aims to investigate factors such as genre, runtime, release date, and language to understand their influence on box office revenue, thus identifying the most common predictors of a film’s financial success: Do action films generate more revenue than dramas? Does a film’s runtime have an impact on its financial performance? Do films released in the summer or during holidays outperform films released at any other time? 
This analysis uses machine learning models, such as linear regression, in order to create a predictive model for box office success based on historical data. This allows to discover the correlation between the film attributes (e.g. genre) and the revenue. It also enables the prediction of new film’s box office revenue based on the attributes. By comparing this prediction with the actual box office outcome, one can find out the the key factors that influence financial success in the film industry.

<span style="color:yellow">"You can make this approach broader to answer more questions beyond only training a predictive a model". 
Ideas: attribute recomendations? Like, given the genre and some other attributes, recommend a season for example</span>.

## Research Questions

## Proposed additional datasets
<span style="color:yellow">Explore each one better</span>
[https://www.kaggle.com/datasets/utkarshx27/movies-dataset/suggestions?status=pending&yourSuggestions=true]
[https://www.boxofficemojo.com/release/rl3290006273/?ref_=bo_hm_rd]
[https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/code]


## Methods

## Proposed timeline

## Organization within the team

## Quickstart

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


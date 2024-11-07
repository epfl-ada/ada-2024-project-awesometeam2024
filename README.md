
# Your project name

## Abstract
Since the very beginning, the movies industry is continuously evolving to match the consummer's behavior in order to keep being lucrative and profitable. While every year bring its own technical improvements, it seems that some very intrinsic features of a movie (genre, release date, etc..) are still impacting the box office revenue in a substantial manner.
This study aims to investigate factors such as genre, runtime, release date, and language to understand their influence on box office revenue, thus identifying the most common predictors of a film’s financial success.
Using the [CMU Movie Summary Corpus Dataset](https://www.cs.cmu.edu/~ark/personas/), we are first going to preprocess the data to extract and measure the quality of the data. Secondly, a first per-feature analysis will allow us to answer some basic questions (eg. Do action films generate more revenue than dramas? Does a film’s runtime have an impact on its financial performance?) that will help us understand the impact of each feature seperatly. In the 3rd part, we will investigate the correlation between these values to understand how they could be linked together. Finally, this analysis will use machine learning models, such as linear regression, in order to create a predictive model for box office success based on historical data. This allows to discover the correlation between the film attributes (e.g. genre) and the revenue. It also enables the prediction of new film’s box office revenue based on the attributes. By comparing this prediction with the actual box office outcome, one can find out the the key factors that influence financial success in the film industry.

- add key results
- add conclusion


<span style="color:yellow">"You can make this approach broader to answer more questions beyond only training a predictive a model". 
Ideas: attribute recomendations? Like, given the genre and some other attributes, recommend a season for example</span>.

## Research Questions

We can investigate whether factors like movie genre, runtime, release date, or language influence box office revenue. 

**Basics questions**
- Do action films generate more revenue than dramas? 
- Does a film’s runtime have an impact on its financial performance? 
- Do movies released in the summer or during winter holiday seasons perform better than those released at other times of the year. 

**Correlation questions**
- Is there a correlation between certain genres and higher revenue? 
- What are the most common predictors of a film’s financial success? 

**Output model** \
By using machine learning models like linear regression, we can create a predictive model for box office success based on historical data. 
- Can we predict a new film’s box office revenue based on its genre, language, runtime, and cast? 


Comparing the actual and predicted box office results, it could provide insight into the key factors that influence financial success in the film industry

## Proposed additional datasets
<span style="color:yellow">Explore each one better</span>
[https://www.kaggle.com/datasets/utkarshx27/movies-dataset/suggestions?status=pending&yourSuggestions=true]
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


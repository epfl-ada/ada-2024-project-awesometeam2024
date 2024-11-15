
# ADA to break the movie industry

## Abstract
Since the very beginning, the movie industry is continuously evolving to meet consumer demands and remain profitable. Key film attributes - such as genre, release date, and runtime — significantly influence box office revenue.
This study aims to investigate these factors to understand their influence on box office revenue, identifying the most common predictors of a film’s financial success.
Using the [CMU Movie Summary Corpus Dataset](https://www.cs.cmu.edu/~ark/personas/), we are first going to preprocess the data to extract and measure the quality of the data. Secondly, a first per-feature analysis will allow us to answer some basic questions to understand their impact separately. Then, we will investigate the correlation between these variables. Finally, this analysis will use ML models in order to create a predictive model for box office success based on historical data.
This approach helps pinpoint key factors driving financial success, providing insights into the elements that most impact a movie's performance.

## Research Questions

The questions are organized as milestones to guide our analysis, helping us systematically examine the factors that contribute to high box office revenue for a successful project outcome.

**Questions : understanding individual features and find correlation**
- How does film runtime correlate with box office revenue? Do longer or shorter films tend to perform better?
- Which 10 languages have the highest average box office revenue?
- Which 10 actors have the highest average box office revenue?
- What is the average box office revenue by actors' age group?
- Does the gender distribution of actors in a film influence its average box office revenue?
- What is the average box office revenue based on the gender predominance in the movie cast?
- What is the average box office revenue based on the ethnic diversity in the movie cast?
- Which 10 ethnicities have the highest average box office revenue?
- How did box office evolved over time? How was it for each genre?
- How has runtime changed along the years?
- How have these features evolve over time?

**Output model** \
Gathering answers from the previous questions, this helps us choose one model for predicting box office revenue. Nevertheless, we still have to choose the best one.
- Can we predict a new film’s box office revenue based on its genre, language, runtime, and cast?
- Which model is the best ?


Comparing the actual and predicted box office results, it could provide insight into the key factors that influence financial success in the film industry

## Proposed Additional Datasets

To improve the models' predictive accuracy, we propose incorporating additional datasets. One such dataset is:

1. **Kaggle's Movie Financials Dataset**  
   - **Source**: [Kaggle - Movie Franchises Financial Data](https://www.kaggle.com/)  
   - **Details**: This dataset includes financial and technical data for movies, such as budgets, lifetime gross, release dates, ratings, runtimes, and user votes.  
   - **Purpose**: By integrating budget data, we refined our classification threshold for high-revenue movies, allowing us to differentiate between successful and underperforming movies more accurately.

## Methods

Our ultimate goal is to predict the box office revenue of a movie based on the correlation of multiple features. Here is a summary of techniques that we have used along the way :
- **Data preprocessing** : clean missing / inconsistent data
- **Data visualization** : histogram, barplot, line plot to help catch trends and distribution of the data
- **Data description** :
   - use confidence intervals to quantify uncertainty in our EDA
   - use Pearson's correlation to look for correlated variables

## Proposed timeline
This timeline defines milestones for our project but is not rigid. Often, we had to go back to the previous step when our findings revealed that we had to change our methods.

#### Step 1 : Define objectives
The goal here was to clearly state which questions we wanted to answer with this analysis and the outcome that we are looking for.

#### Step 2 : Data collection preprocessing
This step involved understanding and manipulating the data in order to be able to further analyze it. We came back multiple times to this step in order to improve our preprocessing pipeline.

#### Step 3 : Exploratory Data Analysis
We answered the first series of questions regarding the dataset in order to separately understand the influence of genre, runtime, actors ethnicity on box office revenue.

#### Step 4 : Analysis of correlations between variables
After understanding how each feature independently affects the revenue, we must understand if a certain combination of these specific features can drastically improve the final outcome of the movie.

#### Step 5 : Define, apply and upgrade model for predictive analysis
Upon gathering all the knowledge from the previous step, we have to look for the best model for our ultimate goal. This involves testing its/their accuracy and try to improve it.

#### Step 6 : Communicate results
An important aspect of a data analysis project is to communicate the findings and synthesize the results for external people.

#### Step 7 : Find areas of improvements
We made choices during this analysis, either because of the time or because of what we thought was true at some point. The goal of this part is to come back on this choice in order to derive improvements on the current pipeline and model.

## Organization within the team

We organize ourselves with one leader for each task/step of the project and at least 3 teammates to review. Here is a summary of the organization :

- **Nicolas** : Step 1 and 2
- **Andrea** : Step 3
- **Vasco** : Step 4
- **Ahmed** : Step 5
- **Ines** : Step 6 and 7

## Quickstart

```bash
# clone project
git clone <project link>
cd <project repo>

# install requirements
pip install -r pip_requirements.txt
```

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
├── results.ipynb               <- a well-structured notebook showing the results
│
├── .gitignore                  <- List of files ignored by git
├── pip_requirements.txt        <- File for installing python dependencies
└── README.md
```
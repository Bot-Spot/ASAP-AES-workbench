# ASAP-AES: word2vec and more

This repo presents a solution for a Kaggle-hosted competition on automatic essay 
scoring: https://www.kaggle.com/c/asap-aes

The 'Performance testing log' section below documents the progress of this project.

## Set up

Tested only on Python 3.6.  Install python packages as per environment.yml. 
Also manually install [when_will_it_end](https://github.com/zkurtz/when_will_it_end).

Download data as follows (the project code assumes this exact directory structure): 

```bash
# Download the data from kaggle
pip install kaggle
kaggle competitions download -c asap-aes

# Organize the data directory
cd ~/.kaggle/competitions/asap-aes
mkdir engineered_features
```

## Model preparation, building, testing

```bash
# Feature engineering on the training set
python featurize_training_data.py

# Fit the model: choose between one of two kinds:
#   - cross_val: estimate the out-of-sample performance
#   - build_final: build a model using all of the training data
python performance_crossval.py
TODO python build_final_classifier.py

# Compute the engineered features on the test set and test the classifier
TODO python featurize_testing_data.py
TODO python performance_final.py
```

## Performance testing log

This log tracks the progress in terms of improvements of prediction accuracy
over time, including notes about which changes in methodology appeared to have
led to improvements.

Model development (including feature engineering, hyperparameter tuning, etc) relies on
cross-validation and excludes use of the test data (`test_set.tsv`) data.

In rare occasions in which we've reached accuracy milestones that we can't resist 
bragging about, take the final step of computing the performance score on the test 
set. Each use of the test data (`test_set.tsv`) contaminates the training procedure by 
leaking information about the test set. That is, repeatedly tweaking the model
to maximize the test set score will lead to the model overfitting to the test set.
Thus we perform a 'final' evaluation as rarely as possible. 

### Cross-validation

- 2018.06.09: 0.047 LightGBM on # of words, # of characters. Definitely coder error is at fault considering that the analogous benchmark scored better than 0.5 on the kaggle leaderboard.

### Final evaluation

- ... TODO
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from statsmodels.discrete.discrete_model import Logit
from statsmodels
from sklearn.model_selection import train_test_split


# Body length
# sale_duration
# users_age
def load_json_local(filename):
    return pd.read_json(filename)

def feature_eng():
    df['fraud'] = df['acct_type'].apply(lambda x: True  if 'fraud' in str(x) else False)
    df['twitter_presence'] = df['org_twitter'].apply(lambda x: 1 if x > 5 else 0)
    df['facebook_presence'] = df['org_facebook'].apply(lambda x: 1 if x > 5 else 0)
    df['within_US'] = df['venue_country'].apply(lambda x: 1 if x == 'US' else 0)
    df['have_previous_payouts'] = df['previous_payouts'].apply(lambda x: 1 if len(x) != 0 else 0)
    df['highly_suspect_state'] = df['venue_state'].apply(lambda x: 1 if x in ['MT', 'Mt', 'AK', 'FL', 'NEW SOUTH WALES', 'Florida'] else 0)
    return df

def fit_logit(y, X):
    logit = Logit(y_train, X_train)
    model = logit.fit()
    return model


if __name__ == '__main__':
    df = load_json_local('files/data.json')
    y = df['fraud']
    X = df[['body_length', 'sale_duration2', 'user_age', 'twitter_presence']]
    X = add_constant(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    fit_logit(y_train, X_train)
    model.summary()

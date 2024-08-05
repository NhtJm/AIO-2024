# 1. Basic Probability
# Question 1
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def compute_mean(x):
    return np.mean(x)


X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
print("Mean : ", compute_mean(X))

# Question 2


def compute_median(x):
    size = len(x)
    x = np.sort(x)
    print(x)
    if (size % 2 == 0):
        return (x[size//2] + x[size//2 - 1]) / 2
    else:
        return x[size//2]


X = [1, 5, 4, 4, 9, 13]
print("Median: ", compute_median(X))

# Question 3


def compute_std(X):
    mean = compute_mean(X)
    variance = 0
    for x in X:
        variance += (x - mean)**2
    variance /= len(X)
    return np.sqrt(variance)


X = [171, 176, 155, 167, 169, 182]
print(compute_std(X))

# Question 4


def compute_correlation_cofficient(X, Y):
    N = len(X)
    numerator = 0
    denominator = 0
    mean_X = compute_mean(X)
    mean_Y = compute_mean(Y)
    std_X = compute_std(X)
    std_Y = compute_std(Y)
    for i in range(N):
        numerator += (X[i] - mean_X) * (Y[i] - mean_Y)
    denominator = N * std_X * std_Y
    return np.round(numerator / denominator, 2)


X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
print("Correlation: ", compute_correlation_cofficient(X, Y))

# 2.Tabular Data Analysis

# Question 5

data = pd.read_csv(
    "/Users/nhatnguyen/Documents/GIT/AIO2024/module2/week4/advertising.csv")


def correlation(x, y):
    mean_x = x.mean()
    mean_y = y.mean()
    std_x = x.std()
    std_y = y.std()
    N = len(x)
    numerator = 0
    for i in range(N):
        numerator += (x[i] - mean_x) * (y[i] - mean_y)
    denominator = N * std_x * std_y
    return numerator / denominator


x = data['TV']
y = data['Radio']
corr_xy = correlation(x, y)
print(f"Correlation between TV and Sales: {round(corr_xy, 2)}")

# Question 6

features = ['TV', 'Radio', 'Newspaper']
for feature_1 in features:
    for feature_2 in features:
        correlation_value = correlation(data[feature_1], data[feature_2])
        print(f"Correlation between {feature_1} and {feature_2}: {round(
              correlation_value, 2)}")

# Question 7
x = data['Radio']
y = data['Newspaper']
result = np.corrcoef(x, y)
print(result)

# Question 8
print(data.corr())

# Question 9

plt.figure(figsize=(10, 8))
data_corr = data.corr()
sns.heatmap(data_corr, annot=True, fmt='.2f', linewidths=.5)

# plt.show()

# 3. Text Retrieval
# Question 10

vi_data_df = pd.read_csv(
    "/Users/nhatnguyen/Documents/GIT/AIO2024/module2/week4/vi_text_retrieval - vi_text_retrieval.csv")
context = vi_data_df['text']
context = [doc.lower() for doc in context]
tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)
print(context_embedded.toarray()[7][0])

# Question 11


def tfidf_search(question, tfidf_vectorizer, top_d=5):
    # lowercasing before encoding
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    cosine_scores = cosine_similarity(
        query_embedded, context_embedded).flatten()
    # Get top k cosine score and index its
    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            'id': idx,
            'cosine_score': cosine_scores[idx]
        }
        results.append(doc_score)
    return results


question = vi_data_df.iloc[0]['question']
results = tfidf_search(question, tfidf_vectorizer, top_d=5)
print(results[0]['cosine_score'])

# Question 12


def corr_search(question, tfidf_vectorizer, top_d=5):
    # lowercasing before encoding
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    # correration between query and context
    corr_scores = np.corrcoef(query_embedded.toarray(),
                              context_embedded.toarray())
    corr_scores = corr_scores[0][1:]
    # Get top k correlation score and index its
    results = []
    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'corr_score': corr_scores[idx]
        }
        results.append(doc)
    return results


question = vi_data_df.iloc[0]['question']
results = corr_search(question, tfidf_vectorizer, top_d=5)
print(results[1]['corr_score'])

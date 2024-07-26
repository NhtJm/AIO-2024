import numpy as np


def create_train_data_iris():
    data = np.loadtxt(
        '/Users/nhatnguyen/Documents/GIT/AIO2024/module2/week3/iris.data.txt', delimiter=',', dtype=str)
    return data


def compute_prior_probability_iris(train_data):
    y_unique = np.unique(train_data[:, -1])
    prior_probability = np.zeros(len(y_unique))
    for num in range(0, len(y_unique)):
        prior_probability[num] = np.sum(
            train_data[:, -1] == y_unique[num]) / len(train_data)
    return prior_probability


def compute_conditional_probability_iris(train_data):
    y_unique = np.unique(train_data[:, -1])
    x_feature = len(train_data[1, :]) - 1
    conditional_probability = []
    for rows in range(0, x_feature):
        x_conditional_probability = np.zeros((len(y_unique), 2))
        for cols in range(0, len(y_unique)):
            mean = np.mean(
                train_data[:, rows][train_data[:, -1] == y_unique[cols]].astype(float))
            sigma = np.std(
                train_data[:, rows][train_data[:, -1] == y_unique[cols]].astype(float))
            sigma = sigma ** 2
            x_conditional_probability[cols] = [mean, sigma]

        conditional_probability.append(x_conditional_probability)
    return conditional_probability


def dist(x, mean, std):
    return 1/(np.sqrt(2*np.pi)*std)*np.exp(-0.5*((x-mean)/std)**2)


def train_gaussian_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probability_iris(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability = compute_conditional_probability_iris(train_data)

    return prior_probability, conditional_probability

####################
# Prediction
####################


def prediction_iris(x,  prior_probability, conditional_probability):
    y_unique = np.unique(train_data[:, 4])
    posterior = np.zeros(len(y_unique))
    for num in range(0, len(y_unique)):
        posterior[num] = prior_probability[num]
        for i in range(0, len(x)):
            posterior[num] *= dist(x[i], conditional_probability[i]
                                   [num][0], conditional_probability[i][num][1])
    return np.argmax(posterior)


# Testcases
x = [6.3, 3.3, 6.0,  2.5]
train_data = create_train_data_iris()
y_unique = np.unique(train_data[:, 4])
prior_probability, conditional_probability = train_gaussian_naive_bayes(
    train_data)
pred = y_unique[prediction_iris(x, prior_probability, conditional_probability)]
assert pred == "Iris-virginica"

x = [5.0, 2.0, 3.5, 1.0]
train_data = create_train_data_iris()
y_unique = np.unique(train_data[:, 4])
prior_probability, conditional_probability = train_gaussian_naive_bayes(
    train_data)
pred = y_unique[prediction_iris(x, prior_probability, conditional_probability)]
assert pred == "Iris-versicolor"

x = [4.9, 3.1, 1.5, 0.1]
train_data = create_train_data_iris()
y_unique = np.unique(train_data[:, 4])
prior_probability, conditional_probability = train_gaussian_naive_bayes(
    train_data)
pred = y_unique[prediction_iris(x, prior_probability, conditional_probability)]
assert pred == "Iris-setosa"

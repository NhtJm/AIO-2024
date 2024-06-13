#regression loss function

import random
import math


def loss_func(num_samples, loss_name):

    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return
    num_samples = int(num_samples)
    if num_samples <= 0:
        print('Number of samples must be greater than 0')
        return
    
    #random
    predict = [random.uniform(0, 10) for _ in range(num_samples)]
    target = [random.uniform(0, 10) for _ in range(num_samples)]

    if loss_name == 'MAE':
        loss = sum(abs(y - y_hat) for y, y_hat in zip(target, predict)) / num_samples
    elif loss_name == ' MSE':
        loss = sum((y - y_hat) ** 2 for y, y_hat in zip(target, predict)) / num_samples
    elif loss_name == 'RMSE':
        loss = math.sqrt(sum((y - y_hat) ** 2 for y, y_hat in zip(target, predict)) / num_samples)
    else:
        print('loss function must be MAE, MSE, or RMSE')
        return
    
    print('loss name:', loss_name, ', sample:', num_samples, ', red:', predict[0], ', target:', target[0])
    print('loss:', loss)
          
# Example
num_samples = input('Input number of samples: ')
loss_name = input('loss function(MAE, MSE, RMSE): ')
loss_func(num_samples, loss_name)

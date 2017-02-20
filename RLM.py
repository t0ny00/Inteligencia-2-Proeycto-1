import numpy as np
import matplotlib.pyplot as plt

def Normalize(array):
    n = len(array)
    media = np.mean(array,axis=0)
    dev_standar = np.std(array,axis=0)

    #Create normalized array
    new_array = []
    for elem in array:
        temp = np.divide((elem - media) ,dev_standar)
        new_array.append(temp)
    out = np.asarray(new_array)
    # print out
    return out

def gradientDescent(x, y, weights, alpha, numIterations):

    n = x.shape[0] # Number of data entries
    cost_function_plot_data = [] # Array with the value of the cost function for each iteration

    for i in range(0, numIterations):

        # Calculate the product of the weights with each entry
        hypothesis = []
        for instance in x:
            sum = 0
            for j in range(instance.size):
                sum += instance[j]*weights[j]
            hypothesis = np.append(hypothesis,sum)

        delta = hypothesis - y

        # Calculate the cost function value
        cost = np.sum(delta ** 2) / (2 * n)
        # Store the iteration number and the cost function value into an array
        cost_function_plot_data = np.append(cost_function_plot_data, [i, cost], axis=0)

        # Calculate the gradient value
        gradient = np.dot(x.transpose(), delta) / n

        weights = weights - alpha * gradient


    cost_function_plot_data = cost_function_plot_data.reshape(numIterations, 2)
    return weights, cost_function_plot_data


def costFunctionPlot(data, numberIterations, alpha):
    x = data[:, 0]
    y = data[:, 1]
    plt.plot(x, y)
    plt.title(r'Convergence Curve for $\alpha=$' + str(alpha) + ' and ' + str(numberIterations) + ' iterations')
    plt.ylabel('Cost Function Value')
    plt.xlabel('Number of Iterations')
    plt.show()


def scatterPlot(x, y, weights):
    temp = np.dot(x,weights)
    # temp = temp.reshape(temp,x.shape()[0],x.shape()[1])
    print temp
    line_point1 = np.dot(x[0], weights)
    line_point2 = np.dot(x[-1], weights)
    plt.title('Scatter Plot with Adjusted Curve')
    plt.ylabel('Y Values')
    plt.xlabel('X Values')
    plt.plot(x[:, 1], y, 'o')
    plt.plot(x,temp, 'r-', lw=3)
    plt.show()

def biasMetric(weights,x,y):
    print x
    print weights
    predicted_result = np.dot(x, weights)
    delta = predicted_result - y
    return np.average(delta)

def maximumDeviationMetric(weights,x,y):
    predicted_result = np.dot(x,weights)
    delta= np.absolute(predicted_result-y)
    return np.max(delta)

def meanMaximumDeviationMetric(weights,x,y):
    predicted_result = np.dot(x,weights)
    delta= np.absolute(predicted_result-y)
    return np.average(delta)

def meanSquareErrorMetric(weights,x,y):
    predicted_result = np.dot(x,weights)
    delta = np.power(predicted_result - y,2)
    return np.average(delta)

if __name__ == '__main__':
    data = np.loadtxt("AmesHousing-training_set2.txt")
    numberIterations = 30   
    alpha = 0.1
    numberRows = data.shape[0]
    numberColumns = data.shape[1]
    weights = np.zeros(numberColumns - 1)
    y = data[:, numberColumns - 1]
    x = data[:, 1:numberColumns - 1]
    x = Normalize(x)
    y = Normalize(y)
    # Add for every entry the x0=1
    x = np.insert(x,0,1,axis=1)

    data_test = np.loadtxt("AmesHousing-test_set2.txt")
    numberRows2 = data_test.shape[0]
    numberColumns2 = data_test.shape[1]
    y2 = data_test[:, numberColumns2 - 1]
    x2 = data_test[:, 1:numberColumns2 - 1]
    x2 = Normalize(x2)
    y2 = Normalize(y2)
    # Add for every entry the x0=1
    x2 = np.insert(x2,0,1,axis=1)

    weights, cost_function_data = gradientDescent(x, y, weights, alpha, numberIterations)

    print biasMetric(weights,x,y)
    print maximumDeviationMetric(weights, x, y)
    print meanMaximumDeviationMetric(weights,x,y)
    print meanSquareErrorMetric(weights,x,y)

    print 'Using data_test'
    print biasMetric(weights,x2,y2)
    print maximumDeviationMetric(weights, x2, y2)
    print meanMaximumDeviationMetric(weights,x2,y2)
    print meanSquareErrorMetric(weights,x2,y2)

    # np.savetxt('Parte1/x01-costFunct-30Iter-' + str(alpha)+'.txt', cost_function_data, delimiter='\t')
    # np.savetxt('Parte1/x01-weights-30Iter.txt', weights.reshape(1,2), delimiter='\t')
    # temp = np.append(x,y.reshape(numRows,1),1)
    # np.savetxt('Parte1/x01-data-30Iter.txt', temp, delimiter='\t')
    # # print a
    # # costFunctionPlot(cost_function_data, numberIterations, alpha)
    # scatterPlot(x, y, weights)

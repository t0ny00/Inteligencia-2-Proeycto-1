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
    n = x.shape[0]
    cost_function_plot_data = []
    for i in range(0, numIterations):
        temp = np.dot(x, weights)
        delta = temp - y

        cost = np.sum(delta ** 2) / (2 * n)
        cost_function_plot_data = np.append(cost_function_plot_data, [i, cost], axis=0)

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


if __name__ == '__main__':
    data = np.loadtxt("x01.txt")
    numberIterations = 30
    alpha = 0.1
    numRows = data.shape[0]
    numColumns = data.shape[1]
    weights = np.zeros(numColumns-1)
    y = data[:, numColumns - 1]
    x = data[:, 1:numColumns - 1]
    x = Normalize(x)
    y = Normalize(y)
    x = np.insert(x,0,1,axis=1)
    # print (x)
    weights, cost_function_data = gradientDescent(x, y, weights, alpha, numberIterations)
    np.savetxt('Parte1/x01-costFunct-30Iter-' + str(alpha)+'.txt', cost_function_data, delimiter='\t')
    np.savetxt('Parte1/x01-weights-30Iter.txt', weights.reshape(1,2), delimiter='\t')
    temp = np.append(x,y.reshape(numRows,1),1)
    np.savetxt('Parte1/x01-data-30Iter.txt', temp, delimiter='\t')
    # print a
    # costFunctionPlot(cost_function_data, numberIterations, alpha)
    scatterPlot(x, y, weights)

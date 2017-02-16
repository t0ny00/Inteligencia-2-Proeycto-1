import numpy as np



def GradientDescent(alpha, weights,y,x,n,numIterations):
    xTrans = x.transpose()
    for i in range (0,numIterations):

        temp = np.dot(x,weights)
        delta = temp - y

        cost = np.sum(delta ** 2) / (2 * n)

        gradient = np.dot(xTrans, delta) / n

        weights = weights - alpha * gradient
    return weights


if __name__ == '__main__':

    data = np.loadtxt("x01.txt")
    numRows = data.shape[0]
    numColumns = data.shape[1]
    weights = np.zeros(numColumns-1)
    y = data[:, numColumns - 1]
    x = data[:, 1:numColumns - 1]
    x = np.insert(x,0,1,axis=1)
    # x = np.ones(shape = (numRows,2))
    # x[:,:1] = data[:, 1:numColumns - 1]
    # x = np.concatenate((x,data[:, 1:numColumns - 1]),axis=0)
    # print(x)
    # print(weights)
    print(GradientDescent(0.5,weights,y,x,numRows,500))

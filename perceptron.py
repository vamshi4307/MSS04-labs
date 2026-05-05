def H(z):
    """Heaviside step function"""
    return 1 if z >= 0 else 0


def output(x1, x2, w1, w2, b):
    """Compute perceptron output"""
    z = w1 * x1 + w2 * x2 + b
    return H(z)


def p_learn(X, Y, w1, w2, b, eta, epochs=10):
    """Perceptron learning algorithm"""
    for epoch in range(epochs):
        for i in range(len(X)):
            x1, x2 = X[i]
            y = Y[i]

            y_pred = output(x1, x2, w1, w2, b)
            error = y - y_pred

            # update rule
            w1 += eta * error * x1
            w2 += eta * error * x2
            b += eta * error

    return w1, w2, b

# Test OR dataset
X = [[1, 1], [1, 0], [0, 1], [0, 0]]
Y_OR = [1, 1, 1, 0]

w1, w2, b = p_learn(X, Y_OR, 0, 0, 0, eta=0.1)
print("Naive Weights:", w1, w2, b)
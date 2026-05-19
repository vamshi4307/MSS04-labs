# Perceptron
# a) naive

def H(z):
    return 1 if z >= 0 else 0   # define the Heaviside function

def output(x1, x2, w1, w2, b):
    z = w1*x1 + w2*x2 + b       # compute the logit z
    print(z)
    return H(z)

x1 = 1
x2 = 1
w1 = 0.1
w2 = 0.1
b = -0.3

print(output(x1, x2, w1, w2, b))

def perceptron_learning(X, Y, w1, w2, b, eta):
    
    for epoch in range(3):
        print(f"\n{epoch+1}", epoch)

        for i in range(len(X)):   # run through an epoch

            a = output(X[i][0], X[i][1], w1, w2, b)  # compute output of perceptron
            y=Y[1]
            e=y-a
            print(X[i],f"y={y}",f"a={a}",f"e={e}")
            #update weights and bias
            if y==1 and a==0:
                w1 = w1 + eta * X[i][0]
                w2 = w2 + eta * X[i][1]
                b = b + eta

            if y == 0 and a == 1:

                w1 = w1 - eta * X[i][0]
                w2 = w2 - eta * X[i][1]
                b = b - eta

            print(f"updated w1={w1}, w2={w2}, b={b}")
            updated_a = [output(X[i][0], X[i][1], w1, w2, b) for i in range(len(X))]
            print(f"updated_a={updated_a}")
            return w1,w2,b
        x = [[0,0],[0,1],[1,0],[1,1]]
        y=[0,0,0,1]
        w1,w2,b=0.1,0.1,-0.3
        eta=0.1
        w1,w2,b=perceptron_learning(x,y,w1,w2,b,eta)


#b) with numpy
import numpy as np

def H(z):
    return 1 if z >= 0 else 0   # define the Heaviside function
def output(X,w,b):
    z=np.dot(X,w)+b
    print(z)
    return H(z)
def perceptron_learning(X, Y, w, b, eta):
    
    for epoch in range(3):
        print(f"\n{epoch+1}", epoch)

        for i in range(len(X)):   # run through an epoch

            a = output(X[i], w, b)  # compute output of perceptron
            y=Y[1]
            e=y-a
            print(X[i],f"y={y}",f"a={a}",f"e={e}")
            #update weights and bias
            if y==1 and a==0:
                w = w + eta * X[i]
                b = b + eta

            if y == 0 and a == 1:

                w = w - eta * X[i]
                b = b - eta

            print(f"updated w={w}, b={b}")
            updated_a = [output(X[i], w, b) for i in range(len(X))]
            print(f"updated_a={updated_a}")
            return w,b
        

# c) OOP Perceptron
 class Perceptron:
    def _init_(self, n_inputs) -> None:
        self.n_inputs = n_inputs
        self.weights = [0] * n_inputs
        self.bias = 0

    def out(self, X):
        z=np.dot(self.weights, X) + self.bias

        return 1 if z=>= 0 else 0   # Heaviside function
    
     def learn(self, data_learn, eta, epochs):
        for _ in range(epochs):
            for x, y in data_learn:
                y_pred = self.out(x)
                error = y - y_pred #compute error 
                if error != 0: #update weights and bias if there is an error
                error+=1
                if Y[1]==1 and y_pred==0:
                   self.weights = [wi + eta * error * xi for wi, xi in zip(self.weights, x)]
                   self.bias += eta * error
                if Y[1] == 0 and y_pred == 1:
                   self.weights = [wi - eta * error * xi for wi, xi in zip(self.weights, x)]
                   self.bias -= eta * error
            err_list.append(error)
            print("End of epoch", "error=", error)
            print("errors per epoch=", err_list)
            print("Final weights:", self.weights, "Final bias:", self.bias)
            print("_"*30)
        return(error_list)




# Test datasets
X_oop = [[1, 1], [1, 0], [0, 1], [0, 0]]

Y_OR = [1, 1, 1, 0]
Y_AND = [1, 0, 0, 0]
Y_NAND = [0, 1, 1, 1]


def plot_decision_boundary(X, Y, weights, bias):
    pass

def test_model(Y, name):
    model = Perceptron(n_inputs=2)
    data = list(zip(X_oop, Y))

    model.learn(data, eta=0.1, epochs=10)

    print(f"\n{name} Weights:", model.weights, "Bias:", model.bias)
    plot_decision_boundary(X_oop, Y, model.weights, model.bias)


# Run tests
test_model(Y_OR, "OR")
test_model(Y_AND, "AND")
test_model(Y_NAND, "NAND")        
        
X=np.array([[0,0],[0,1],[1,0],[1,1]])
print(X[0])
print(X[1])
print(X[2])
print(X[3]) 
Y=np.array([0,0,0,1])
w=np.array([0.1,0.1])   
b=-0.3
def output(X,w,b):
    z=np.dot(X,w)+b
    print(z)
    return H(z)


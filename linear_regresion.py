import matplotlib.pyplot as plt
import numpy as np


class LinearRegression():

    def __init__(self, x, y):
        self.__x = np.array(x)
        self.__y = np.array(y)
        self.__equation, self.__b_0, self.__b_1 = self.__least_squares_equation(
            self.__x, self.__y)
        self.__minimize = self.__minimize_error(
            self.__x, self.__y, self.__b_0, self.__b_1)
        self.__r = self.__correlation_coefficient(self.__x, self.__y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def equation(self):
        return self.__equation

    @property
    def b_0(self):
        return self.__b_0

    @property
    def b_1(self):
        return self.__b_1

    @property
    def minimize(self):
        return self.__minimize

    @property
    def r(self):
        return self.__r

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    def __least_squares_equation(self, x, y):
        n = len(x)
        x_sum = sum(x)
        y_sum = sum(y)
        xy = sum(x*y)
        x_squared = sum(x**2)

        b_1 = (xy - (1/n)*(x_sum*y_sum))/(x_squared - (1/n)*x_sum**2)
        b_0 = (y_sum/n) - b_1*(x_sum/n)

        return ("y = " + str(np.round(b_1, 2)) + "x " + str(np.round(b_0, 2))), b_0, b_1

    def __minimize_error(self, x, y, b_0, b_1):
        minimize = (y - (b_0+b_1*x))**2
        return minimize

    def __correlation_coefficient(self, x, y):
        n = len(x)
        mean_x = sum(x) / len(x)
        mean_y = sum(y) / len(y)

        numerator = sum((x - mean_x)*(y - mean_y))
        denominator = np.sqrt(sum(((x - mean_x)**2) * sum(((y - mean_y)**2))))

        r = numerator / denominator

        return r

    def predict(self, x_predict):
        x_predict = np.array(x_predict)
        y_predict = []
        for value in x_predict:
            y_predict.append(self.__b_0 + self.__b_1 * value)
        return y_predict

    def plot_line(self):
        fig, ax = plt.subplots(figsize=(10, 5), dpi=100)
        ax.set_title('Consumption vs Required Memory Capacity (training set)')
        ax.set_xlabel('Consumption in megabytes')
        ax.set_ylabel('Required Memory Capacity')
        ax = plt.scatter(self.__x, self.__y, s=100)
        ax = plt.plot(self.__x, self.predict(self.__x), color='red')
        plt.show()

    def plot_test(self, x_test, y_test):
        fig, ax = plt.subplots(figsize=(10, 5), dpi=100)
        ax.set_title('Consumption vs Required Memory Capacity (test set)')
        ax.set_xlabel('Consumption in megabytes')
        ax.set_ylabel('Required Memory Capacity')
        ax = plt.scatter(x_test, y_test, s=100)
        ax = plt.plot(x_test, self.predict(x_test), color='red')
        plt.show()

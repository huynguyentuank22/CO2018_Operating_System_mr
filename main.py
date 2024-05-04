from interface import Interface
from memory import Memory
from linear_regresion import LinearRegression


def main():

    option = 0
    interface = Interface
    memory = Memory
    days_history = []
    memory_history = []

    while option != 5:
        try:
            option = interface.menu()

            if option == 1:
                days_history, memory_history = memory.memory_consumption()

            elif option == 2:
                memory.plot(days_history, memory_history, annot=False)

            elif option == 3:
                minimum_memory_value = memory.model()
                print("The minimum amount of memory required to keep growing is: " +
                      str(minimum_memory_value))

            elif option == 4:
                x, y = memory.X_y(50)
                x_test, y_test = memory.X_y(10)
                regression = LinearRegression(x, y)
                regression.plot_line()
                regression.plot_test(x_test, y_test)
                print("Linear equation: " + regression.equation)
                print("Correlation coefficient: " + str(regression.r))

            elif option == 5:
                print("Thank you for using the simulator.")

            else:
                print("Invalid option. Please try again.")

        except:
            print("Make sure you have entered a correct option.")


if __name__ == '__main__':
    main()

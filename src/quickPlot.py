import numpy as np
from matplotlib import pyplot as plt
from math import *

def plot(s):
    f = lambda x : eval(s)
    x = np.linspace(-1000,1000,1000)
    y = np.zeros(1000)

    for ind, val in enumerate(x):
        y[ind] = f(x[ind])

    plt.plot(x,y)
    plt.xlabel = "x"
    plt.ylabel = "y"
    plt.title(f"f(x) = {s}")
    plt.show()



if __name__ == "__main__":
    running = True
    while running:
        try:
            plot(input("Enter python function:\nf(x) = "))
        except:
            print("Something went wrong, try again?")
            if input("[y/N] = ").upper()[0] == "N":
                running = not running




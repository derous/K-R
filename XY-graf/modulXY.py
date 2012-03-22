import matplotlib.pyplot as plt

def frange(start,end,step):
    return map(lambda x: x*step, range(int(start*1./step),int(end*1./step)))

def plot1(functors, start, finish, step):
    ax = plt.subplot(111)
    x_axis = frange(start, finish, step)
    for func in functors:
        ax.plot(x_axis, map(func, x_axis))
    plt.show()

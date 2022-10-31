import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.style.use('Solarize_Light2')

def set_title(ax):
    ax.set_title("平方数", fontsize=24)
    ax.set_xlabel("值", fontsize=10)
    ax.set_ylabel("值的平方", fontsize=10)
    ax.tick_params(axis='both', which='major', labelsize=13)
def drow_01():
    fig, ax = plt.subplots()
    ax.scatter(2, 4, 200)

    set_title(ax)
    plt.show()

# drow_01()

def drow_02():
    fig, ax = plt.subplots()

    x_values = range(1, 1001)
    y_values = [v**2 for v in x_values]

    # ax.scatter(x_values, y_values, c='red', s=1)
    # ax.scatter(x_values, y_values, c=(0, 0, 0), s=1)
    ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
    ax.axis([0, 1100, 0, 1100_000])
    ax.ticklabel_format(style='plain')
    set_title(ax)

    plt.savefig('squares_plot.png', bbox_inches='tight')
    plt.show()
    pass

drow_02()
import matplotlib.pyplot as plt

def picture():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.savefig('images/test.png', format='png')




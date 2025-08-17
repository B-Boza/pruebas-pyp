import matplotlib.pyplot as plt

def generate_pie():
    lab = ['A','B','C']
    val = [200, 35, 120]

    fig, ax = plt.subplots()
    ax.pie(val, labels = lab)
    plt.savefig('pie.png')
    plt.close()
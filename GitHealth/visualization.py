import matplotlib.pyplot as plt

def draw_score_chart(score):
    labels = ["Health Score"]
    values = [score]
    
    plt.figure(figsize=(5, 4))
    plt.bar(labels, values)

    plt.title('Project Health Score')
    plt.ylim(0, 100)
    plt.savefig('health_score.png')
    plt.show()
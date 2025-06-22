import numpy as np
import csv

def load_csv(filename):
    x_data, y_data = [], []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            x_data.append(float(row['x']))
            y_data.append(float(row['y']))
    return np.array(x_data), np.array(y_data)

def train_model(x, y, lr=0.01, epochs=1000):
    w, b = 0.0, 0.0
    n = len(x)

    for _ in range(epochs):
        y_pred = w * x + b
        error = y_pred - y
        w -= lr * (2/n) * np.dot(error, x)
        b -= lr * (2/n) * np.sum(error)

    return w, b

if __name__ == "__main__":
    x, y = load_csv("data.csv")
    w, b = train_model(x, y)
    np.save("model.npy", np.array([w, b]))
    print(f"Model trained: y = {w:.2f}x + {b:.2f}")

import matplotlib.pyplot as plt
x = [1, 3, 7]
y = [2, 6, 14]
w1 = 0
w0 = 0
lr = 0.01
epochs = 100
for epoch in range(1, epochs+1):
    for i in range(len(x)):
        prediction = w1 * x[i] + w0
        w1 += 2 * lr * x[i] * (y[i] - prediction)
        w0 += 2 * lr * (y[i] - prediction)
print('w1 =', w1, 'w0 =', w0)
plt.scatter(x, y, color='pink')
plt.plot([0, 7], [w0, w1 * 7 + w0])
plt.grid()
plt.show()
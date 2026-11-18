"""Ngày 3: Thử tham số tuyến tính bằng tay; chưa tự huấn luyện."""
x = [1, 2, 3, 4]
y = [3, 5, 7, 9]

def predict(x_values, w, b):
    return [w * item + b for item in x_values]

def mse(true_values, predictions):
    return sum((a - b) ** 2 for a, b in zip(true_values, predictions)) / len(true_values)

for w, b in [(1, 1), (2, 1), (2, 0)]:
    yp = predict(x, w, b)
    print(f'w={w}, b={b}, predictions={yp}, MSE={mse(y, yp):.2f}')

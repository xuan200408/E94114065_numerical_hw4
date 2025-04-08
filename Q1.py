import numpy as np

# 定義函數 f(x) = sin(4x) * e^x
def f(x):
    return np.sin(4 * x) * np.exp(x)

# 積分範圍與步長
a = 1
b = 2
h = 0.1
n = int((b - a) / h)

# a. 複合梯形法
x_trap = np.linspace(a, b, n + 1)
y_trap = f(x_trap)
trap_result = (h / 2) * (y_trap[0] + 2 * np.sum(y_trap[1:-1]) + y_trap[-1])

# b. 複合辛普森法
x_simp = np.linspace(a, b, n + 1)
y_simp = f(x_simp)
simpson_result = (h / 3) * (y_simp[0] + 
                            4 * np.sum(y_simp[1:-1:2]) + 
                            2 * np.sum(y_simp[2:-2:2]) + 
                            y_simp[-1])

# c. 複合中點法
x_mid = np.linspace(a + h/2, b - h/2, n)
y_mid = f(x_mid)
mid_result = h * np.sum(y_mid)

print(f"複合梯形法結果：{trap_result:.6f}")
print(f"複合辛普森法結果：{simpson_result:.6f}")
print(f"複合中點法結果：{mid_result:.6f}")

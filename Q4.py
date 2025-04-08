import numpy as np

# 定義第一題的被積分的函數 f(x) = x^(-0.25) * sin(x)
def f_a(x):
    return x**(-0.25) * np.sin(x)

# 定義第二題的被積分的函數 f(t) = sin(1/t) / t^3
def f_b(t):
    return np.sin(1/t) * t**2

# 合成 Simpson 法則
def composite_simpson(f, a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    # 累加奇數位置的項 (x_1, x_3, ..., x_(n-1))
    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
    # 累加偶數位置的項 (x_2, x_4, ..., x_(n-2))
    for i in range(2, n, 2):
        result += 2 * f(a + i * h)
    result *= h / 3
    return result

# 設定第一題的積分範圍和步數 (將起點從0稍微偏移)
a_a = 0.0001
b_a = 1
n_a = 4  # 分割成4個小區間

# 設定第二題的積分範圍和步數
a_b = 0.001
b_b = 1
n_b = 4  # 分割成4個小區間

# 使用合成 Simpson 法則計算第一題積分
result_a = composite_simpson(f_a, a_a, b_a, n_a)
print(f"第一題積分結果: {result_a:.10f}")

# 使用合成 Simpson 法則計算第二題積分
result_b = composite_simpson(f_b, a_b, b_b, n_b)
print(f"第二題積分結果: {result_b:.10f}")

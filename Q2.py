import numpy as np
from scipy.integrate import quad

# 定義函數 f(x)
def f(x):
    return x**2 * np.log(x)

# 積分範圍
a = 1
b = 1.5

def gaussian_quadrature(f, a, b, xi, wi):
    return ((b - a) / 2) * np.sum(wi * f(((b - a) / 2) * xi + (b + a) / 2))

# n = 3 的節點與權重
xi_3 = np.array([-np.sqrt(3/5), 0, np.sqrt(3/5)])
wi_3 = np.array([5/9, 8/9, 5/9])

# n = 4 的節點與權重
xi_4 = np.array([-0.8611363116, -0.3399810436, 0.3399810436, 0.8611363116])
wi_4 = np.array([0.3478548451, 0.6521451549, 0.6521451549, 0.3478548451])

# 計算高斯積分結果
gauss_3 = gaussian_quadrature(f, a, b, xi_3, wi_3)
gauss_4 = gaussian_quadrature(f, a, b, xi_4, wi_4)

# 計算精確值
exact_val, _ = quad(f, a, b)

# 輸出結果
print(f"Gaussian Quadrature n=3: {gauss_3:.6f}")
print(f"Gaussian Quadrature n=4: {gauss_4:.6f}")
print(f"Exact value:             {exact_val:.6f}")
print(f"Error (n=3):             {abs(gauss_3 - exact_val):.6e}")
print(f"Error (n=4):             {abs(gauss_4 - exact_val):.6e}")


import numpy as np
from scipy.integrate import dblquad
from numpy.polynomial.legendre import leggauss

# 積分函數
def f(x, y):
    return 2 * y * np.sin(x) + np.cos(x)**2

# ----------- Simpson's Rule (雙重積分) -------------
def composite_simpson_double(f, a, b, m, n):
    hx = (b - a) / m
    result = 0
    for i in range(m + 1):
        xi = a + i * hx
        cx = 1 if i == 0 or i == m else (4 if i % 2 == 1 else 2)
        y1, y2 = np.sin(xi), np.cos(xi)
        if y1 > y2:
            y1, y2 = y2, y1
        hy = (y2 - y1) / n
        inner = 0
        for j in range(n + 1):
            yj = y1 + j * hy
            cy = 1 if j == 0 or j == n else (4 if j % 2 == 1 else 2)
            inner += cy * f(xi, yj)
        result += cx * (hy / 3) * inner
    return hx / 3 * result

# ----------- Gaussian Quadrature (雙重積分) ----------
def gaussian_quadrature_double(f, a, b, nx, ny):
    x_nodes, x_weights = leggauss(nx)
    y_nodes, y_weights = leggauss(ny)
    xm = (b + a) / 2
    xr = (b - a) / 2
    total = 0
    for i in range(nx):
        xi = xm + xr * x_nodes[i]
        wi = x_weights[i]
        y1, y2 = np.sin(xi), np.cos(xi)
        if y1 > y2:
            y1, y2 = y2, y1
        ym = (y2 + y1) / 2
        yr = (y2 - y1) / 2
        inner = 0
        for j in range(ny):
            yj = ym + yr * y_nodes[j]
            wj = y_weights[j]
            inner += wj * f(xi, yj)
        total += wi * yr * inner
    return xr * total

# ----------- Scipy 精確積分 --------------------------
def scipy_exact_integral():
    def integrand(y, x):
        return 2 * y * np.sin(x) + np.cos(x)**2
    def y_lower(x):
        return min(np.sin(x), np.cos(x))
    def y_upper(x):
        return max(np.sin(x), np.cos(x))
    result, err = dblquad(integrand, 0, 0.25* np.pi, y_lower, y_upper)
    return result, err

# ------------ 計算與顯示結果 ------------------------
a = 0
b = 0.25 * np.pi
simpson_result = composite_simpson_double(f, a, b, 4, 4)
gauss_result = gaussian_quadrature_double(f, a, b, 3, 3)
exact_result, exact_error = scipy_exact_integral()

print(f"{'Method':<25} {'Result':>20} {'Abs. Error':>20}")
print("-" * 65)
print(f"{'Composite Simpson (n=4)':<25} {simpson_result:>20.10f} {abs(simpson_result - exact_result):>20.10f}")
print(f"{'Gaussian Quad (n=3)':<25} {gauss_result:>20.10f} {abs(gauss_result - exact_result):>20.10f}")
print(f"{'Scipy dblquad (Exact)':<25} {exact_result:>20.10f} {'(True Value)':>20}")

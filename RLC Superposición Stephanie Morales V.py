import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")  # Aplica el estilo de Seaborn a las gráficas de Matplotlib
# Parámetros
R, L, C = 10, 0.1, 100e-6
f = 50.0
t = np.linspace(0, 4, 1000)  # Tiempo de 0 a 4 
w = 2 * np.pi * f

XL = w * L
XC = 1 / (w * C)
Z = complex(R, XL - XC)
Zc = complex(0, -XC)
H = Zc / Z

print(f"Z = {Z:.2f} Ω  |Z| = {abs(Z):.2f} Ω  ángulo = {np.degrees(np.angle(Z)):.2f}°")
print(f"H(jw) |H| = {abs(H):.4f}  ángulo = {np.degrees(np.angle(H)):.2f}°")

# Fasores de entrada (referencia coseno): sin(wt) = cos(wt - 90°)
X1 = 1 * np.exp(1j * np.deg2rad(-90))
X2 = 2 * np.exp(1j * np.deg2rad(0))

Y1, Y2 = H * X1, H * X2
y1 = np.abs(Y1) * np.cos(w * t + np.angle(Y1))
y2 = np.abs(Y2) * np.cos(w * t + np.angle(Y2))

x1 = np.sin(w * t)
x2 = 2 * np.cos(w * t)
x_s = x1 + x2

X_s = X1 + X2
Y_s = H * X_s
y_s = np.abs(Y_s) * np.cos(w * t + np.angle(Y_s))
y_sum = y1 + y2

error_max_super = np.max(np.abs(y_s - y_sum))

plt.figure(figsize=(8, 4))
plt.plot(t, x1, label='x1(t) = sin(2π·50t)')
plt.plot(t, x2, label='x2(t) = 2cos(2π·50t)')
plt.plot(t, x_s, '--', label='x_s(t) = x1(t)+x2(t)')
plt.title("Entradas: Individuales y Combinada")
plt.xlabel("Tiempo [s]"); plt.ylabel('Voltaje [V]')
plt.legend(); plt.grid(True)

plt.figure(figsize=(8, 4))
plt.plot(t, y_s, label='y_s(t): salida combinada')
plt.plot(t, y_sum, '--', label='y1(t)+y2(t): suma de salidas')
plt.title("Superposición: Comparación de Salidas en v_C(t)")
plt.xlabel('Tiempo [s]'); plt.ylabel('Voltaje en C [V]')
plt.legend(); plt.grid(True)
plt.show()

print(f"Error máximo absoluto: {error_max_super:.2e}")
print("✔ Se cumple la superposición." if error_max_super < 1e-9 else "✘ No se cumple.")





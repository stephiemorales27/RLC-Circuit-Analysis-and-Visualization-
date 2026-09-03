import numpy as np
import matplotlib.pyplot as plt
# RLC Circuit Simulation Platform
R, L, C = 10, 0.1, 100e-6   # Ohms, Henrios, Faradios
# Parámetros
f = 60.0          # Frecuencia [Hz]
k = 3             # Factor de escala
t = np.linspace(0, 4, 1000)  # Tiempo de 0 a 4 s
w = 2 * np.pi * f

# Función de transferencia H(jw) = Vc/Vin
XL = w * L
XC = 1 / (w * C)
Z = complex(R, XL - XC)
Zc = complex(0, -XC)
H = Zc / Z

print(f"Z = {Z:.2f} Ω  |Z| = {abs(Z):.2f} Ω  ángulo = {np.degrees(np.angle(Z)):.2f}°")
print(f"H(jw) |H| = {abs(H):.4f}  ángulo = {np.degrees(np.angle(H)):.2f}°")

x1 = np.cos(w * t)
y1 = np.abs(H) * np.cos(w * t + np.angle(H))
x1_k = k * x1
y1_k = k * np.abs(H) * np.cos(w * t + np.angle(H))
y1_escalada = k * y1

error_max = np.max(np.abs(y1_k - y1_escalada))

plt.figure(figsize=(8, 4))
plt.plot(t, x1, label='x1(t) = cos(2π·60t)')
plt.plot(t, x1_k, '--', label=f'{k}·x1(t)')
plt.title("Entradas: Original y Escalada")
plt.xlabel("Tiempo [s]"); plt.ylabel("Voltaje [V]")
plt.legend(); plt.grid(True)

plt.figure(figsize=(8, 4))
plt.plot(t, y1_k, label='y_k(t): salida con entrada escalada')
plt.plot(t, y1_escalada, '--', label='k·y(t): salida original escalada')
plt.title("Homogeneidad: Comparación de Salidas en v_C(t)")
plt.xlabel("Tiempo [s]"); plt.ylabel("Voltaje en C [V]")
plt.legend(); plt.grid(True)
plt.show()

print(f"Error máximo absoluto: {error_max:.2e}")
print("✔ Se cumple la homogeneidad." if error_max < 1e-9 else "✘ No se cumple.")

import numpy as np
import matplotlib.pyplot as plt

# Parámetros
f = 60.0          # Frecuencia [Hz]
k = 3             # Factor de escala
t = np.linspace(0, 4, 100)  # Tiempo de 0 a 4 s

# Entrada original y salida (sistema lineal: y = x)
x1 = np.cos(2 * np.pi * f * t)
y1 = x1  # Salida original

# Entrada escalada y su salida
x1_k = k * x1
y1_k = x1_k  # Salida con entrada escalada

# Salida original escalada
y1_escalada = k * y1

# ---------------- Gráficas ----------------

# Gráfica de entradas
plt.figure(figsize=(8, 4))
plt.plot(t, x1, label='x1(t) = cos(2π60t)')
plt.plot(t, x1_k, '--', label=f'{k}·x1(t)')
plt.title("Entradas: Original y Escalada")
plt.xlabel("Tiempo [s]")
plt.ylabel("Voltaje en C [V]")
plt.legend()
plt.grid(True)

# Gráfica de salidas
plt.figure(figsize=(8, 4))
plt.plot(t, y1_k, label='Salida con entrada escalada')
plt.plot(t, y1_escalada, '--', label='Salida original escalada')
plt.title("Homogeneidad: Comparación de Salidas")
plt.xlabel("Tiempo [s]")
plt.ylabel("Voltaje en C [V]")
plt.legend()
plt.grid(True)
plt.show()

# Verificación numérica
error_max = np.max(np.abs(y1_k - y1_escalada))
print(f"Error máximo absoluto: {error_max:.2e}")
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
f = 50.0
t = np.linspace(0, 4, 100)  # Tiempo de 0 a 4 

# 1. Definir entradas
x1 = np.sin(2 * np.pi * f * t)
x2 = 2 * np.cos(2 * np.pi * f * t)

# 2. Salidas individuales (asumimos sistema lineal → salida = entrada)
y1 = x1
y2 = x2

# 3. Entrada combinada
x_s = x1 + x2

# 4. Salida combinada
y_s = x_s

# 5. Suma de salidas individuales
y_sum = y1 + y2

# 6. Error máximo absoluto
error_max_super = np.max(np.abs(y_s - y_sum))

# ------------------ Gráficas ------------------

# Gráfica de entradas
plt.figure(figsize=(8, 4))
plt.plot(t, x1, label='x1(t) = sin(2π·50t)')
plt.plot(t, x2, label='x2(t) = 2cos(2π·50t)')
plt.plot(t, x_s, '--', label='x_s(t) = x1(t)+x2(t)')
plt.title("Entradas: Individuales y Combinada")
plt.xlabel("Tiempo [s]")
plt.ylabel('Voltaje en C [V]')
plt.legend()
plt.grid(True)

# Gráfica de salidas
plt.figure(figsize=(8, 4))
plt.plot(t, y_s, label='y_s(t) salida combinada')
plt.plot(t, y_sum, '--', label='y1(t)+y2(t) suma de salidas')
plt.title(f"Superposición: Comparación de Salidas")
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje en C [V]')
plt.grid(True)
plt.show()


# Error máximo absoluto
error_max_super = np.max(np.abs(y_s - y_sum)) 
print(f"Error máximo absoluto: {error_max:.2e}")

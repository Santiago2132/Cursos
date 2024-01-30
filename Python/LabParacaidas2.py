import numpy as np
import matplotlib.pyplot as plt

def euler(t, y, dt, dydt):# t=time, y=distance 
    return y + dt * dydt(t, y)

def relative_error(y_true, y_pred):
    return (np.abs(y_true - y_pred) / np.abs(y_true)) * 100

def parachutist_motion(t, y, v, m, A, Cd):
    return -9.81 + (1/m)*A*Cd*v**2

def y_analytical(t):
    h0 = 100000 # Initial height in meters
    g = 9.81 # Gravity in m/s^2
    return h0 - (g/2) * t**2 

def solve_problem(dt):
    t = np.arange(0, 20, dt)
    y = np.zeros_like(t)
    v = np.zeros_like(t)
    y[0] = 100000
    v[0] = 0

    for i in range(len(t)-1):
        y[i+1] = euler(t[i], y[i], dt, lambda t, y: v[i])
        v[i+1] = euler(t[i], v[i], dt, lambda t, v: parachutist_motion(t, y[i], v, 80, 0.5, 1.2))

    y_analytical_t = np.array([y_analytical(i) for i in t])
    relative_error_euler = relative_error(y, y_analytical_t)

    return t, y, y_analytical_t, relative_error_euler

dt_values = [0.5, 1, 2]

fig, ax = plt.subplots()

for dt in dt_values:
    t, y, y_analytical_t, relative_error_euler = solve_problem(dt)
    ax.plot(t, y, label=f"dt={dt} s")
    ax.plot(t, y_analytical_t, linestyle='--', label=f"Analytical, dt={dt} s")

ax.set_xlabel("Time (s)")
ax.set_ylabel("Height (m)")
ax.set_title("Parachutist Fall with Air Resistance")
ax.legend()
plt.show()

for dt in dt_values:
    print(f"Error relative for dt={dt} s: {relative_error_euler[-1]:.2f}%")
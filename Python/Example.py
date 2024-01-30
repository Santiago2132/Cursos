import matplotlib.pyplot as plt

# Data
dt = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
E_a = [0, 21.8, 39.7, 54.3, 65.9, 74.9, 81.8, 86.9, 90.4, 92.5, 93.7]
V_a = [0, 468.2, 895.3, 1284.9, 1640.4, 1964.8, 2260.7, 2530.6, 2776.9, 3001.6, 3206.5]
Vn_theoretical = [490, 935.02, 1339.2, 1706.3, 2039.7, 2342.5, 2617.5, 2867.3, 3094.1, 3300.2, 3484.1]

# Calculate relative error
relative_error = [(va - vn) / vn * 100 for va, vn in zip(V_a, Vn_theoretical)]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(dt, E_a, label="Ea", marker='o')
plt.plot(dt, V_a, label="Va", marker='o')
plt.plot(dt, Vn_theoretical, label="Vn (theoretical)", linestyle='--')

for x, y, e in zip(dt, V_a, relative_error):
    plt.text(x+0.02, y+30, f"{e:.2f}%", ha="center")

plt.xlabel("dt (time)")
plt.ylabel("Value")
plt.title("Data points and relative error")
plt.legend()
plt.grid()
plt.show()

# Print relative error
print("Relative error:")
for e in relative_error:
    print(f"{e:.4f}")
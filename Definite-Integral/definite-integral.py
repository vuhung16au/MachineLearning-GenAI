import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x):
    return x**2

a = 0
b = 1
num_frames = 200

# Exact value of the integral ∫x² dx from 0 to 1 is 1/3
EXACT_INTEGRAL = 1/3
ERROR_THRESHOLD = 0.01

fig, ax = plt.subplots()
x = np.linspace(a, b, 500)
ax.plot(x, f(x), 'r', linewidth=2, label='$f(x) = x^2$')
ax.set_xlim(a, b)
ax.set_ylim(0, 1.1)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Riemann Sum Approximation of $\int_{0}^{1} x^2 dx$')
ax.legend()

rects = []
ani = None  # Define ani here so it can be accessed in animate function

def animate(i):
    n = i + 1
    delta_x = (b - a) / n
    x_i = np.linspace(a + delta_x, b, n)
    y_i = f(x_i)

    global rects
    for rect in rects:
        rect.remove()
    rects = []

    for j in range(n):
        rect = ax.bar(x_i[j] - delta_x / 2, y_i[j], width=delta_x, alpha=0.5, edgecolor='black')
        rects.append(rect[0])

    sum_area = np.sum(y_i * delta_x)
    error = abs(sum_area - EXACT_INTEGRAL)
    
    ax.set_title(f'Riemann Sum (n={n}): Area ≈ {sum_area:.4f}, Error: {error:.4f}')
    
    # Stop animation when error is below threshold
    if error < ERROR_THRESHOLD:
        global ani
        if ani is not None:
            ani.event_source.stop()
            ax.set_title(f'Final Riemann Sum (n={n}): Area ≈ {sum_area:.4f}, Error: {error:.4f} < {ERROR_THRESHOLD}')
    
    return rects

ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=False, repeat=True)

plt.show()
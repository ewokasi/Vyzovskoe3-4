import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Nonlinear model definition
def nonlinear_model(t, y, w1, w2):
    # y = [x, dx/dt]
    x, dx = y
    ddx = -w1 * dx + w2(t) * (1 - x**2) * dx - x  # Modified Van der Pol-type dynamics
    return [dx, ddx]

# Parameters
W1_stable = 2.5
W1_unstable = 25
W2 = lambda t: 1 / (2 * t**2 + t + 2)  # Time-dependent W2

# Initial conditions
initial_conditions = [[0.1, 0], [1.5, 0]]  # Stable and unstable

# Time span
time_span = [0, 50]

def simulate_and_plot_subplots(w1, initial_cond_stable, initial_cond_unstable):
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    t_eval = np.linspace(*time_span, 1000)

    # Stable Regime
    solution_stable = solve_ivp(nonlinear_model, time_span, initial_cond_stable, t_eval=t_eval, args=(w1, W2))
    x_stable, dx_stable = solution_stable.y
    t_stable = solution_stable.t
    
    axs[0, 0].plot(x_stable, dx_stable, label="Stable Regime Phase Portrait")
    axs[0, 0].set_title("Stable Regime: Phase Portrait")
    axs[0, 0].set_xlabel("x")
    axs[0, 0].set_ylabel("dx/dt")
    axs[0, 0].grid()
    axs[0, 0].legend()
    
    axs[1, 0].plot(t_stable, x_stable, label="x(t)")
    axs[1, 0].set_title("Stable Regime: Time Series")
    axs[1, 0].set_xlabel("Time")
    axs[1, 0].set_ylabel("x")
    axs[1, 0].grid()
    axs[1, 0].legend()

    # Unstable Regime
    solution_unstable = solve_ivp(nonlinear_model, time_span, initial_cond_unstable, t_eval=t_eval, args=(W1_unstable, W2))
    x_unstable, dx_unstable = solution_unstable.y
    t_unstable = solution_unstable.t
    
    axs[0, 1].plot(x_unstable, dx_unstable, label="Unstable Regime Phase Portrait")
    axs[0, 1].set_title("Unstable Regime: Phase Portrait")
    axs[0, 1].set_xlabel("x")
    axs[0, 1].set_ylabel("dx/dt")
    axs[0, 1].grid()
    axs[0, 1].legend()
    
    axs[1, 1].plot(t_unstable, x_unstable, label="x(t)")
    axs[1, 1].set_title("Unstable Regime: Time Series")
    axs[1, 1].set_xlabel("Time")
    axs[1, 1].set_ylabel("x")
    axs[1, 1].grid()
    axs[1, 1].legend()

    plt.tight_layout()
    plt.show()

# Control Algorithm: Stabilize near stable equilibrium
def controlled_model(t, y, w1, w2, control_gain):
    x, dx = y
    u = -control_gain * (x + dx)  # Simple proportional control
    ddx = -w1 * dx + w2(t) * (1 - x**2) * dx - x + u  # Add control
    return [dx, ddx]

def simulate_controlled_vs_uncontrolled(w1, initial_cond, control_gain):
    t_eval = np.linspace(*time_span, 1000)
    solution_uncontrolled = solve_ivp(nonlinear_model, time_span, initial_cond, t_eval=t_eval, args=(w1, W2))
    solution_controlled = solve_ivp(controlled_model, time_span, initial_cond, t_eval=t_eval, args=(w1, W2, control_gain))
    
    x_uncontrolled, t_uncontrolled = solution_uncontrolled.y[0], solution_uncontrolled.t
    x_controlled, t_controlled = solution_controlled.y[0], solution_controlled.t
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(t_uncontrolled, x_uncontrolled, label="Uncontrolled Model")
    ax.plot(t_controlled, x_controlled, label="Controlled Model")
    ax.set_title("Comparison: Controlled vs Uncontrolled")
    ax.set_xlabel("Time")
    ax.set_ylabel("x")
    ax.grid()
    ax.legend()
    plt.show()

# Run simulations
simulate_and_plot_subplots(W1_stable, initial_conditions[0], initial_conditions[1])
control_gain = 10
simulate_controlled_vs_uncontrolled(W1_unstable, [1.5, 0], control_gain)

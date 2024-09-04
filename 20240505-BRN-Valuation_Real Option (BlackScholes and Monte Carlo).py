# Brazilian Nickel Limited
# Financial Office - FP&A
# Valuation: Real Option using Black-Scholes/Monte Carlo Simulation
# Coded by Andre Simao, CFO
# Date: May 05, 2024
# CONFIDENTIAL: FOR INTERNAL USE ONLY.
#
# Description: Code will simulate 10,000 paths of asset prices, calculate the option price using Monte Carlo
#              simulation, and plot the paths with highlights on those with a positive payoff. This visualization
#              offers insights into how the real option value is influenced by the underlying asset's
#              price movements and volatility.


import numpy as np
import matplotlib.pyplot as plt


def simulate_asset_paths(S0: float, T: float, vol: float, steps: int, num_paths: int, rfr: object) -> object:
    """
    Simulate multiple asset price paths using the Geometric Brownian Motion model.

    :param S0: Float: Initial spot price of the underlying asset
    :param T: Float: Time to maturity in years
    :param vol: Float: Volatility of the underlying asset
    :param steps: Integer: Number of time steps
    :param num_paths: Integer: Number of simulated paths
    :param rfr: Numpy Array object: Array of risk-free rates for each time step


    :return: Numpy Array object: Simulated asset paths
    """
    dt = T / steps
    paths = np.zeros((steps + 1, num_paths))
    paths[0] = S0

    for t in range(1, steps + 1):
        z = np.random.standard_normal(num_paths)
        paths[t] = paths[t - 1] * np.exp((rfr[t - 1] - 0.5 * vol ** 2) * dt + vol * np.sqrt(dt) * z)

    return paths


def monte_carlo_option_pricing(S0: float, K: float, T: float, vol: float, steps: int, num_paths: int, rfr: object) -> object:
    """
    Calculate the real option price using Monte Carlo simulation.

    :param S0: Float: Initial spot price of the underlying asset
    :param K: Float: Strike price (investment cost)
    :param T: Float: Time to maturity in years
    :param vol: Float: Volatility of the underlying asset
    :param steps: Integer: Number of time steps
    :param num_paths: Integer: Number of simulated paths
    :param rfr: Numpy Array object: Array of risk-free rates for each time step

    :return Float: Monte Carlo estimate of the real option price
    """

    # Simulates the asset paths
    paths = simulate_asset_paths(S0, T, vol, steps, num_paths, rfr)

    # Calculates the payoff for each path at maturity
    payoff = np.maximum(paths[-1] - K, 0)

    # Discounts payoff to present value using the average risk-free rate
    discount_factor = np.exp(-np.mean(rfr) * T)
    option_price = np.mean(payoff) * discount_factor

    return paths, payoff, option_price


def plot_paths(paths: object, payoff: object, K: float):
    """
    Plot the simulated asset paths and highlight those with positive payoff.

    :param paths: Numpy Array object: Simulated asset paths
    :param payoff: Numpy Array object: Payoff for each path
    :param K: Float: Strike price (investment cost)

    :return: does not return
    """

    # Creates Matplot lib object
    plt.figure(figsize=(10, 6))

    for i in range(paths.shape[1]):
        if payoff[i] > 0:
            plt.plot(paths[:, i], color='green', alpha=0.3)  # Highlight profitable paths in green
        else:
            plt.plot(paths[:, i], color='red', alpha=0.1)  # Non-profitable paths in red

    # Plots paths
    plt.axhline(K, color='blue', linestyle='--', label='Strike Price (K)')
    plt.title('Simulated Asset Price Paths')
    plt.xlabel('Time Steps')
    plt.ylabel('Asset Price')
    plt.legend()
    plt.show()

# ____________________ DASHBOARD BELOW ________________________________________________________

# Enter  parameters

S0 = 1.4                     # Initial spot price
K = 0.78                     # Strike price (investment cost)
T = 0.7                      # Time to maturity (1 year)
vol = 0.1643                 # Volatility (20%)
steps = 3                    # Number of time steps
num_paths = 1                # Number of Monte Carlo paths

# Varying risk-free rates over time (linear increase)

beg_rfr = 0.0401              # Start risk-free rate
end_rfr = 0.07              # End risk-free rate
rfr = np.linspace(beg_rfr, end_rfr, steps)

# Calculates the real option price using Monte Carlo simulation

paths, payoff, option_price = monte_carlo_option_pricing(S0, K, T, vol, steps, num_paths, rfr)
print(f"The real option price using Monte Carlo simulation is: USD {option_price:.2f}")

# Plots the paths highlighting the fair value paths

plot_paths(paths, payoff, K)

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import os

print("To enter exponents in functions, use the Python friendly syntax. For example y**3 is y cubed and y**(1/3) is the cubed root of y. ")
atc_func_input = input("Enter ATC(y) function (e.g., '2*y**2 + 3*y + 5'): ")
avc_func_input = input("Enter AVC(y) function (e.g., '2*y**2 + 3*y + 5'): ")
afc_func_input = input("Enter AFC(y) function (e.g., '2*y**2 + 3*y + 5'): ")
mc_func_input = input("Enter MC(y)/supply function (e.g., '2*y**2 + 3*y + 5'): ")
inverse_supply_func_input = input("Enter the inverse supply function (e.g., 'P/4'): ")

# Define range for plotting
x_min = float(input("Enter the minimum x-axis value for plotting: "))
x_max = float(input("Enter the maximum x-axis value for plotting: "))
y_min = float(input("Enter the minimum y-axis value for plotting: "))
y_max = float(input("Enter the maximum y-axis value for plotting: "))

# Input the given price
price = float(input("Enter the given price: "))

# The where the graph is drawn
output_file = input("Enter a filename for the png chart image: ")
if not output_file.endswith('.png'):
    output_file += '.png'

# Define the range of 'y' values (excluding zero to avoid division by zero)
y_values = np.linspace(0.1, 20, 100)

# Yield plot values using sympy to parse the functios input by the user
y = sp.symbols('y')

atc = sp.sympify(atc_func_input)
atc_func = sp.lambdify(y, atc, 'numpy')
atc_func_vals = atc_func(y_values)

avc = sp.sympify(avc_func_input)
avc_func = sp.lambdify(y, avc, 'numpy')
avc_func_vals = avc_func(y_values)

afc = sp.sympify(afc_func_input)
afc_func = sp.lambdify(y, afc, 'numpy')
afc_func_vals = afc_func(y_values)

mc = sp.sympify(mc_func_input)
mc_func = sp.lambdify(y, mc, 'numpy')
mc_func_vals = mc_func(y_values)

# Find the profit-maximizing output level where MC = P
y = sp.symbols('y')
P = sp.symbols('P')
inverse_supply_func = sp.sympify(inverse_supply_func_input)
inverse_eqn = sp.Eq(y, inverse_supply_func)
inverse_eqn_with_price = inverse_eqn.subs(P, price)
y_star = sp.solve(inverse_eqn_with_price, y)

# Calculate ATC(s_star) and Total Cost at this quantity
atc_star = float(atc_func(y_star[0]))
tc_star = atc_star * y_star[0]

# Calculate Total Revenue (TR) and Total Profit (π)
tr_star = price * y_star[0]
profit = tr_star - tc_star

# Setup the plot graph size
plt.figure(figsize=(10,8))

# Plot ATC
plt.plot(y_values, atc_func_vals, label=fr'ATC = ${atc_func_input}$', color='blue')

# Plot AVC with a different color
plt.plot(y_values, avc_func_vals, label=fr'AVC = ${avc_func_input}$', color='red', linestyle='--')

# Plot AFC with a third color
plt.plot(y_values, afc_func_vals, label=fr'AFC = ${afc_func_input}$', color='green', linestyle='-.')

# Plot MC with a fourth color representing the supply curve
plt.plot(y_values, mc_func_vals, label=fr'MC = ${mc_func_input}$', color='purple', linestyle=':')

# Plot horizontal line at Price (representing market price)
plt.axhline(y=price, color='black', linestyle='--', label=f'Price = {price}')

# Convert y_star_val to a float so it can be used to fill-in TR, TC, and TP areas on the graph
y_star_val = float(y_star[0])

# Total Revenue rectangle (TR = P * y_star)
plt.fill_between([0, y_star_val], 0, price, color='lightblue', alpha=0.75, label='Total Revenue', hatch='///', edgecolor='darkblue')

# Total Cost rectangle (TC = ATC(y_star) * y_star)
plt.fill_between([0, y_star_val], 0, atc_star, color='lightcoral', alpha=0.75, label='Total Cost')

# Total Profit rectangle (Profit = TR - TC)
plt.fill_between([0, y_star_val], atc_star, price, color='lightgreen', alpha=0.75, label='Total Profit')

# Add labels and grid
plt.title('Cost Curves, Supply Curve, and Profit Maximization')
plt.xlabel('y (Quantity)')
plt.ylabel('$/unit')
plt.grid(True)
plt.legend()

# Set the limits for x-axis and y-axis
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

# Save the plot as an image file
plt.savefig(output_file)
print(f"File saved: {output_file}")

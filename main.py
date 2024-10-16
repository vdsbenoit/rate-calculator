# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import mplcursors

# Constants
hours_per_day = 8
days = np.arange(1, 21)  # 20 days
hours_worked = days * hours_per_day

# Exponential decrease in pricing strategy from 100€/h to 50€/h over 20 days

# Using an exponential decay formula
initial_price = 150
final_price = 62.5
decay_rate = 0.4  # Adjust this for faster or slower exponential decay

# Calculate exponential price per hour
price_per_hour_exponential = final_price + (initial_price - final_price) * np.exp(-decay_rate * days)

# Plotting the exponential pricing model
plt.figure(figsize=(10, 6))
line, = plt.plot(days, price_per_hour_exponential, marker='o', linestyle='-', color='b')
plt.title('Exponential Price Evolution (€/Hour)')
plt.ylabel('Price (€/Hour)')
plt.xlabel('Number of Days Worked')

# Add weekly markers on x-axis (i.e., every 5 days)
plt.xticks(ticks=np.arange(0, 21, 5), labels=["0", "1 week", "2 weeks", "3 weeks", "1 month"])

# Add grid for better readability
plt.grid(True)

# Set y-axis range from 0 to 100
plt.ylim(final_price, initial_price)

# Add interactive cursor
cursor = mplcursors.cursor(line, hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(f'{sel.target[0]:.0f} days: {sel.target[1]:.2f} €/h'))

# Show the plot
plt.show()
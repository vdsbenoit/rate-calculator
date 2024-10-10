# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Constants
hours_per_day = 8
days = np.arange(1, 21)  # 20 days
hours_worked = days * hours_per_day

# Exponential decrease in pricing strategy from 100€/h to 50€/h over 20 days

# Using an exponential decay formula
initial_price = 100
final_price = 50
decay_rate = 0.2  # Adjust this for faster or slower exponential decay

# Calculate exponential price per hour
price_per_hour_exponential = final_price + (initial_price - final_price) * np.exp(-decay_rate * days)

# Plotting the exponential pricing model
plt.figure(figsize=(10, 6))
plt.plot(days, price_per_hour_exponential, marker='o', linestyle='-', color='b')
plt.title('Exponential Price Evolution (€/Hour)')
plt.ylabel('Price (€/Hour)')
plt.xlabel('Number of Days Worked')

# Add weekly markers on x-axis (i.e., every 5 days)
plt.xticks(ticks=np.arange(0, 21, 5), labels=[f'Week {i}' for i in range(5)])

# Add grid for better readability
plt.grid(True)

# Show the plot
plt.show()

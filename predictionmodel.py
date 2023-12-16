import datetime
import random
import matplotlib.pyplot as plt

# Current year for the start of the prediction
current_year = datetime.datetime.now().year

# Function to predict IPv4 exhaustion given a starting pool, annual allocation rate, and annual growth rate of allocation
def predict_ipv4_exhaustion(starting_ipv4_pool, allocation_rate, allocation_growth_rate):
    year_data = []
    remaining_ipv4_data = []
    remaining_ipv4 = starting_ipv4_pool
    year = current_year
    while remaining_ipv4 > 0:
        remaining_ipv4 -= allocation_rate
        allocation_rate *= (1 + allocation_growth_rate)
        year += 1
        if remaining_ipv4 <= 0:
            break
        # Storing data for plotting
        year_data.append(year)
        remaining_ipv4_data.append(remaining_ipv4)
    return year, year_data, remaining_ipv4_data

# Total number of IPv4 addresses
total_ipv4 = 2**32

# Assuming we have already allocated 3.7 billion addresses
current_allocated_ipv4 = 3_700_000_000

# Starting pool of IPv4 addresses for the prediction
starting_ipv4_pool = total_ipv4 - current_allocated_ipv4

# Annual allocation rate of IPv4 addresses
# This number is hypothetical; the actual rate can be determined from historical data or current trends.
allocation_rate = 130_000_000

# Assume an annual growth rate of 5% in the allocation rate
allocation_growth_rate = 0.05

# Predict the year of IPv4 exhaustion
year_of_exhaustion, year_data, remaining_ipv4_data = predict_ipv4_exhaustion(starting_ipv4_pool, allocation_rate, allocation_growth_rate)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(year_data, remaining_ipv4_data, marker='o')
plt.title("IPv4 Address Exhaustion Prediction")
plt.xlabel("Year")
plt.ylabel("Remaining IPv4 Addresses")
plt.grid(True)
plt.show()

year_of_exhaustion


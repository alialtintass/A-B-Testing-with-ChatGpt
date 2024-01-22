from scipy.stats import shapiro
import pandas as pd
import numpy as np
# Set a random seed for reproducibility
np.random.seed(42)

# Generate sample data for Group A (NFC withdrawal amount) with an exponential distribution
data_group_a = {
    'WithDrawalAmount_USD': np.random.exponential(scale=50.000, size=34)
}
df_group_a = pd.DataFrame(data_group_a)
df_group_a.WithDrawalAmount_USD.mean()

# Generate sample data for Group A (NFC withdrawal amount) with an exponential distribution
data_group_b = {
    'WithDrawalAmount_USD': np.random.exponential(scale=60.000, size=34)
}
df_group_b = pd.DataFrame(data_group_b)
df_group_b.WithDrawalAmount_USD.mean()

# Shapiro-Wilk test for normality
stat_group_a, p_value_group_a = shapiro(df_group_a['WithDrawalAmount_USD'])
stat_group_b, p_value_group_b = shapiro(df_group_b['WithDrawalAmount_USD'])

# Display the results
print("Shapiro-Wilk Test for Normality:")
print(f"Group A - W-statistic: {stat_group_a}, p-value: {p_value_group_a}")
print(f"Group B - W-statistic: {stat_group_b}, p-value: {p_value_group_b}")
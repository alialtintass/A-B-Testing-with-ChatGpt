import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set a random seed for reproducibility
np.random.seed(42)

# Generate sample data for Group A (NFC card)
data_group_a = {
    'PurchaseAmount_USD': np.random.normal(loc=50.000, scale=10.000, size=34)
}
df_group_a = pd.DataFrame(data_group_a)

# Generate sample data for Group B (Banking card)
data_group_b = {
    'PurchaseAmount_USD': np.random.normal(loc=45.000, scale=10.000, size=34)
}
df_group_b = pd.DataFrame(data_group_b)

#Levene's Test for checking homogeneity of group variances
from scipy.stats import levene

statistic, p_value = levene(df_group_a['PurchaseAmount_USD'], df_group_b['PurchaseAmount_USD'])

# Display the results
print("Levene's Test for Equality of Variances:")
print(f"Test Statistic: {statistic}")
print(f"P-value: {p_value}")

# Two-sample t-test
from scipy.stats import ttest_ind

t_statistic, p_value = ttest_ind(df_group_a['PurchaseAmount_USD'], df_group_b['PurchaseAmount_USD'])

# Display the results
print("Two-Sample T-Test Results:")
print(f"T-Statistic: {t_statistic}")
print(f"P-value:"'{:.20f}'.format(p_value))

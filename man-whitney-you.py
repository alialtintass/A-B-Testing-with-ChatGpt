from scipy.stats import mannwhitneyu

# Mann-Whitney U test
u_statistic, p_value = mannwhitneyu(df_group_a['PurchaseAmount_USD'], df_group_b['PurchaseAmount_USD'])

# Display the results
print("Mann-Whitney U Test Results:")
print(f"U-Statistic: {u_statistic}")
print(f"P-value: {p_value}")

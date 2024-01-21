from scipy.stats import shapiro

# Shapiro-Wilk test for normality
stat_group_a, p_value_group_a = shapiro(df_group_a['WithDrawalAmount_USD'])
stat_group_b, p_value_group_b = shapiro(df_group_b['WithDrawalAmount_USD'])

# Display the results
print("Shapiro-Wilk Test for Normality:")
print(f"Group A - W-statistic: {stat_group_a}, p-value: {p_value_group_a}")
print(f"Group B - W-statistic: {stat_group_b}, p-value: {p_value_group_b}")

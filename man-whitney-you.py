from scipy.stats import mannwhitneyu

# Mann-Whitney U test
u_statistic, p_value = mannwhitneyu(df_group_a['WithDrawalAmount_USD'], df_group_b['WithDrawalAmount_USD'])

# Display the results
print("Mann-Whitney U Test Results:")
print(f"U-Statistic: {u_statistic}")
print(f"P-value: {p_value}")
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference between the groups.")

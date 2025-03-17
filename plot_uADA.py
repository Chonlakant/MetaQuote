# uADA Price Visualization

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

# Load the CSV data
df = pd.read_csv('uADA_price_1hrs.csv')

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Convert ua_token_amount from string to float (it's in wei format with 18 decimals)
df['ua_token_amount'] = df['ua_token_amount'].astype(float)

# Convert to a more readable format (divide by 10^18 to get the actual token amount)
df['ua_token_amount_readable'] = df['ua_token_amount'] / 1e18

# Sort by timestamp to ensure proper chronological order
df = df.sort_values('timestamp')

# Set up the figure with two subplots (one for each metric)
plt.figure(figsize=(14, 10))

# Plot 1: ua_token_amount over time
plt.subplot(2, 1, 1)
plt.plot(df['timestamp'], df['ua_token_amount_readable'], color='blue', linewidth=2)
plt.title('uADA Token Amount Over Time', fontsize=16)
plt.ylabel('Token Amount', fontsize=14)
plt.grid(True, alpha=0.3)

# Format the x-axis to show nice time labels
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.xticks(rotation=45)

# Plot 2: odos_usdc_return over time
plt.subplot(2, 1, 2)
plt.plot(df['timestamp'], df['odos_usdc_return'], color='green', linewidth=2)
plt.title('USDC Return Value Over Time', fontsize=16)
plt.xlabel('Time', fontsize=14)
plt.ylabel('USDC Value', fontsize=14)
plt.grid(True, alpha=0.3)

# Format the x-axis to show nice time labels
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()
plt.savefig('uada_price_charts.png', dpi=300)
plt.show()

# Enhanced visualization with additional insights
plt.figure(figsize=(16, 12))

# Plot with more detailed formatting
# 1. ua_token_amount with trend line
plt.subplot(2, 1, 1)
plt.plot(df['timestamp'], df['ua_token_amount_readable'], color='blue', linewidth=2, label='Token Amount')

# Add trend line
z = np.polyfit(range(len(df)), df['ua_token_amount_readable'], 1)
p = np.poly1d(z)
plt.plot(df['timestamp'], p(range(len(df))), "r--", linewidth=1, label='Trend Line')

plt.title('uADA Token Amount Over Time', fontsize=16)
plt.ylabel('Token Amount', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()

# Add annotations for min and max values
max_token_idx = df['ua_token_amount_readable'].idxmax()
min_token_idx = df['ua_token_amount_readable'].idxmin()

plt.annotate(f'Max: {df.loc[max_token_idx, "ua_token_amount_readable"]:.2f}',
             xy=(df.loc[max_token_idx, 'timestamp'], df.loc[max_token_idx, 'ua_token_amount_readable']),
             xytext=(10, 10), textcoords='offset points', arrowprops=dict(arrowstyle='->'))

plt.annotate(f'Min: {df.loc[min_token_idx, "ua_token_amount_readable"]:.2f}',
             xy=(df.loc[min_token_idx, 'timestamp'], df.loc[min_token_idx, 'ua_token_amount_readable']),
             xytext=(10, -20), textcoords='offset points', arrowprops=dict(arrowstyle='->'))

# Format the x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.xticks(rotation=45)

# 2. odos_usdc_return with trend line
plt.subplot(2, 1, 2)
plt.plot(df['timestamp'], df['odos_usdc_return'], color='green', linewidth=2, label='USDC Return')

# Add trend line
z = np.polyfit(range(len(df)), df['odos_usdc_return'], 1)
p = np.poly1d(z)
plt.plot(df['timestamp'], p(range(len(df))), "r--", linewidth=1, label='Trend Line')

plt.title('USDC Return Value Over Time', fontsize=16)
plt.xlabel('Time', fontsize=14)
plt.ylabel('USDC Value', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()

# Add annotations for min and max values
max_usdc_idx = df['odos_usdc_return'].idxmax()
min_usdc_idx = df['odos_usdc_return'].idxmin()

plt.annotate(f'Max: {df.loc[max_usdc_idx, "odos_usdc_return"]:.2f}',
             xy=(df.loc[max_usdc_idx, 'timestamp'], df.loc[max_usdc_idx, 'odos_usdc_return']),
             xytext=(10, 10), textcoords='offset points', arrowprops=dict(arrowstyle='->'))

plt.annotate(f'Min: {df.loc[min_usdc_idx, "odos_usdc_return"]:.2f}',
             xy=(df.loc[min_usdc_idx, 'timestamp'], df.loc[min_usdc_idx, 'odos_usdc_return']),
             xytext=(10, -20), textcoords='offset points', arrowprops=dict(arrowstyle='->'))

# Format the x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('uada_price_charts_with_trend.png', dpi=300)
plt.show()

# Correlation analysis
correlation = df['ua_token_amount_readable'].corr(df['odos_usdc_return'])
print(f"Correlation between token amount and USDC return: {correlation:.4f}")

# Display basic statistics
print("\nStatistics for uADA Token Amount:")
print(df['ua_token_amount_readable'].describe())

print("\nStatistics for USDC Return:")
print(df['odos_usdc_return'].describe())

# Plot the relationship between token amount and USDC return
plt.figure(figsize=(10, 6))
plt.scatter(df['ua_token_amount_readable'], df['odos_usdc_return'], alpha=0.5)
plt.title('Relationship Between Token Amount and USDC Return', fontsize=16)
plt.xlabel('Token Amount', fontsize=14)
plt.ylabel('USDC Return', fontsize=14)
plt.grid(True, alpha=0.3)

# Add trend line
z = np.polyfit(df['ua_token_amount_readable'], df['odos_usdc_return'], 1)
p = np.poly1d(z)
plt.plot(df['ua_token_amount_readable'], p(df['ua_token_amount_readable']), "r--")

plt.tight_layout()
plt.savefig('uada_relationship_chart.png', dpi=300)
plt.show()
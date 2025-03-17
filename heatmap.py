import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.colors as mcolors

# Load the data
df = pd.read_csv('uADA_price_1hrs.csv')

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract day and hour
df['day_of_week'] = df['timestamp'].dt.day_name()
df['hour'] = df['timestamp'].dt.hour
df['minute'] = df['timestamp'].dt.minute

# Create time bins (hourly intervals)
df['hour_bin'] = df['hour'].astype(str) + ':00'

# Let's see what we've got first
print(f"Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")
print(f"Days in dataset: {df['day_of_week'].unique()}")
print(f"Hours in dataset: {sorted(df['hour'].unique())}")

# Since we only have one day, let's create a heatmap by hour and 15-minute intervals
# This gives us more granularity
df['minute_bin'] = (df['minute'] // 15) * 15
df['time_bin'] = df['hour'].astype(str) + ':' + df['minute_bin'].astype(str).str.zfill(2)

# Create a pivot table for the heatmap
# For single day data, we'll use minute intervals on y-axis and hours on x-axis
pivot_data = df.pivot_table(
    values='odos_usdc_return',
    index='minute_bin',
    columns='hour',
    aggfunc='mean'
)

# Set up plotting parameters
plt.figure(figsize=(15, 8))

# Define custom colormap - light green to dark green
colors = ['#e5f5e0', '#c7e9c0', '#a1d99b', '#74c476', '#41ab5d', '#238b45', '#006d2c', '#00441b']
cmap = mcolors.LinearSegmentedColormap.from_list('green_gradient', colors)

# Create the heatmap
ax = sns.heatmap(
    pivot_data,
    cmap=cmap,
    annot=True,
    fmt=".2f",
    linewidths=0.5,
    cbar_kws={'label': 'USDC Return Value'}
)

# Set the title and labels
plt.title('USDC Return by Hour and 15-Minute Intervals (Monday, March 17, 2025)', fontsize=16)
plt.xlabel('Hour of Day', fontsize=14)
plt.ylabel('Minute Interval', fontsize=14)

# Adjust colorbar to highlight values close to 1000
max_return = df['odos_usdc_return'].max()
plt.clim(df['odos_usdc_return'].min(), max_return)

# Annotate the highest value
max_value = df['odos_usdc_return'].max()
max_hour = df.loc[df['odos_usdc_return'].idxmax(), 'hour']
max_minute = df.loc[df['odos_usdc_return'].idxmax(), 'minute_bin']
max_time = f"{max_hour}:{max_minute:02d}"
plt.text(0.5, -0.1, f"Highest USDC Return: {max_value:.2f} at {max_time}", 
         horizontalalignment='center', fontsize=12, transform=ax.transAxes)

# Let's also create a line plot showing how return varies over the hours
plt.figure(figsize=(15, 6))

# Group by hour and calculate mean
hourly_avg = df.groupby('hour')['odos_usdc_return'].mean().reset_index()

# Plot
sns.lineplot(x='hour', y='odos_usdc_return', data=hourly_avg, marker='o', linewidth=2)
plt.axhline(y=995, color='r', linestyle='--', label='995 USDC Return Threshold')

# Styling
plt.title('Average USDC Return by Hour (Monday, March 17, 2025)', fontsize=16)
plt.xlabel('Hour of Day', fontsize=14)
plt.ylabel('Average USDC Return', fontsize=14)
plt.grid(True, alpha=0.3)
plt.xticks(range(min(df['hour']), max(df['hour'])+1))
plt.legend()

# Annotate hours with highest returns
top_hours = hourly_avg.nlargest(3, 'odos_usdc_return')
for _, row in top_hours.iterrows():
    plt.annotate(f"{row['odos_usdc_return']:.2f}", 
                 xy=(row['hour'], row['odos_usdc_return']),
                 xytext=(5, 5), textcoords='offset points')

plt.tight_layout()
plt.show()

# Create histogram of returns to see distribution
plt.figure(figsize=(12, 6))
sns.histplot(df['odos_usdc_return'], bins=20, kde=True)
plt.title('Distribution of USDC Return Values', fontsize=16)
plt.xlabel('USDC Return', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.axvline(x=995, color='r', linestyle='--', label='995 USDC Return Threshold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Print statistics for high-value returns (>995)
high_returns = df[df['odos_usdc_return'] > 995]
print(f"\nEntries with USDC return > 995: {len(high_returns)}")
print(f"Percentage of high returns: {(len(high_returns) / len(df) * 100):.2f}%")

if not high_returns.empty:
    print("\nTimes with highest returns:")
    top_returns = high_returns.sort_values('odos_usdc_return', ascending=False).head(10)
    for _, row in top_returns.iterrows():
        print(f"Time: {row['timestamp'].strftime('%H:%M:%S')} - Return: {row['odos_usdc_return']:.2f}")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = "new_runs\position_data_final_deg60_gravity_test_dens019375_98_freq35_PW0_PP1E4_PPS4_PPR3_PWS83_PWroll5_PWAD11E9_smallramp_amplitude_avg.csv"
df = pd.read_csv(file_path)

# Filter for specific particle IDs:
selected_ids =  range(df['# particleId'].min(),df['# particleId'].max()+1)
filtered_df = df[df['id'].isin(selected_ids)]

# Create subplots for position and velocity
fig, axes = plt.subplots(2, 1, figsize=(12, 12))

# Plot pos_x vs time
sns.lineplot(data=filtered_df, x='time', y='dif_x', hue='# particleId', marker='o', ax=axes[0])
axes[0].set_title('Position in X-direction vs Time for Particles')
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Position in X-direction (m)')
axes[0].grid(True)
axes[0].set_xlim(0, 2)  

# Plot vel_x vs time
#sns.lineplot(data=filtered_df, x='time', y='vel_x', hue='id', marker='o', ax=axes[1])
#axes[1].set_title('Velocity in X-direction vs Time for Particles')
#axes[1].set_xlabel('Time (s)')
#axes[1].set_ylabel('Velocity in X-direction (m/s)')
#axes[1].grid(True)
#axes[1].set_xlim(0, 2)  
#plt.tight_layout()
#plt.show()
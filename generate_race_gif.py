# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import json
from pathlib import Path
from datetime import datetime

print("="*80)
print("ANIMATED RACE CHART GIF GENERATOR")
print("="*80)
print()

# Paths
historical_dir = Path(r"C:\Users\Marco.Africani\OneDrive - AVU SA\AVU CPI Campaign\Puzzle_control_Reports\IRON_DATA\historical")
dashboard_dir = Path(r"C:\Users\Marco.Africani\OneDrive - AVU SA\AVU CPI Campaign\Puzzle_control_Reports\IRON_DATA\dashboard")
race_chart_file = historical_dir / "race_chart_data.json"
gif_output = dashboard_dir / "race_chart_animated.gif"

# Load data
print(f"Loading race chart data from: {race_chart_file}")
with open(race_chart_file, 'r', encoding='utf-8') as f:
    race_data = json.load(f)

time_series = race_data['time_series']
print(f"Loaded {len(time_series)} snapshots")
print(f"Date range: {time_series[0]['date']} to {time_series[-1]['date']}")
print()

# Create figure and axis
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor('white')

# Gold color
GOLD_COLOR = '#D4AF37'

def draw_frame(snapshot_index):
    ax.clear()
    snapshot = time_series[snapshot_index]

    # Get top 10 winners
    winners = snapshot['winners'][:10]

    # Sort by value for display
    winners_sorted = sorted(winners, key=lambda x: x['value'], reverse=False)

    # Extract data
    names = [w['name'] for w in winners_sorted]
    values = [w['value'] for w in winners_sorted]

    # Create horizontal bar chart
    bars = ax.barh(names, values, color=GOLD_COLOR, edgecolor='#1A1A1A', linewidth=1.5)

    # Add value labels on bars
    for i, (bar, value) in enumerate(zip(bars, values)):
        width = bar.get_width()
        ax.text(width + 0.01, bar.get_y() + bar.get_height()/2,
                f'{value:.4f}',
                ha='left', va='center', fontsize=11, fontweight='bold', color='#1A1A1A')

    # Styling
    ax.set_xlabel('Weighted Score', fontsize=14, fontweight='bold', color='#1A1A1A')
    ax.set_title(f'Top 10 Wine Campaign Winners - {snapshot["analysis_date"]}',
                 fontsize=16, fontweight='bold', color='#1A1A1A', pad=20)
    ax.set_xlim(0, max(values) * 1.15)
    ax.tick_params(axis='both', labelsize=11, colors='#1A1A1A')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#1A1A1A')
    ax.spines['bottom'].set_color('#1A1A1A')
    ax.grid(axis='x', alpha=0.3, linestyle='--', linewidth=0.5)

    print(f"  Frame {snapshot_index + 1}/{len(time_series)}: {snapshot['date']}")

# Create animated GIF
print("Generating frames...")
writer = PillowWriter(fps=1)  # 1 frame per second = 1000ms per frame

with writer.saving(fig, str(gif_output), dpi=100):
    for i in range(len(time_series)):
        draw_frame(i)
        writer.grab_frame()

plt.close(fig)

# Get file size
file_size_mb = gif_output.stat().st_size / (1024 * 1024)

print()
print("="*80)
print("GIF GENERATION COMPLETE!")
print("="*80)
print(f"Total Frames: {len(time_series)}")
print(f"Date Range: {time_series[0]['date']} to {time_series[-1]['date']}")
print(f"Duration per Frame: 1000ms (1 second)")
print(f"Total Animation Time: {len(time_series)} seconds")
print(f"Color Scheme: Gold bars ({GOLD_COLOR})")
print(f"Winners per Frame: 10")
print(f"File Location: {gif_output}")
print(f"File Size: {file_size_mb:.2f} MB")
print("="*80)

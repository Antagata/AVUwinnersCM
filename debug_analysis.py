# TARGETED DEBUG: Check rows 498-499 in OMT file for CM-25-02472

import pandas as pd
from pathlib import Path
import re

def _norm_cm(s):
    if pd.isna(s): return ""
    s = str(s).strip()
    s = re.sub(r"\.0$", "", s)
    s = re.sub(r"[^A-Za-z0-9]", "", s).upper()
    s = re.sub(r"^CM", "", s)
    return s.lstrip("0")

# Load the OMT data
SNAP_PATH = Path(r"C:\Users\Marco.Africani\OneDrive - AVU SA\AVU CPI Campaign\Puzzle_control_Reports\IRON_DATA\snapshots")
omt_df = pd.read_pickle(SNAP_PATH / "omt_main_offer.pkl")

print("=== TARGETED INVESTIGATION: ROWS 498-499 ===")
print(f"OMT DataFrame shape: {omt_df.shape}")

# Check specific rows 498-499 (Python is 0-indexed, so 497-498)
target_rows = [497, 498]  # 498-499 in 1-indexed becomes 497-498 in 0-indexed

print(f"\n🔍 EXAMINING ROWS 498-499 (indices 497-498):")
for row_idx in target_rows:
    if row_idx < len(omt_df):
        print(f"\n--- ROW {row_idx + 1} (index {row_idx}) ---")
        row_data = omt_df.iloc[row_idx]
        
        # Show all data in this row
        for col_idx, (col_name, value) in enumerate(row_data.items()):
            print(f"  Column {col_idx:2d} ('{col_name}'): {value}")
    else:
        print(f"Row {row_idx + 1} is beyond DataFrame length")

# Look for CM-25-02472 in various formats across all columns
print(f"\n🔍 SEARCHING FOR CM-25-02472 VARIATIONS:")
search_patterns = ["CM-25-02472", "2502472", "25-02472", "CM2502472", "25.02472"]

for pattern in search_patterns:
    print(f"\nSearching for pattern: '{pattern}'")
    found_rows = []
    
    for col_name in omt_df.columns:
        matches = omt_df[omt_df[col_name].astype(str).str.contains(pattern, case=False, na=False)]
        if len(matches) > 0:
            for idx in matches.index:
                if idx not in found_rows:
                    found_rows.append(idx)
                    print(f"  Found in row {idx + 1} (index {idx}), column '{col_name}': '{matches.loc[idx, col_name]}'")

# Check if normalization helps find the campaign
print(f"\n🔍 TESTING NORMALIZATION ON TARGET ROWS:")
for row_idx in target_rows:
    if row_idx < len(omt_df):
        print(f"\nRow {row_idx + 1} normalization test:")
        row_data = omt_df.iloc[row_idx]
        
        for col_name, value in row_data.items():
            normalized = _norm_cm(value)
            if normalized and ("2502472" in normalized or "502472" in normalized):
                print(f"  Column '{col_name}': '{value}' -> normalized: '{normalized}' ✅ MATCH!")

# Check the filtering that might exclude it
print(f"\n🔍 CHECKING SIZE AND MINQTY FILTERS:")
size_col = None
minqty_col = None
campaign_col = None

# Find relevant columns
for i, col in enumerate(omt_df.columns):
    if 'size' in str(col).lower():
        size_col = i
        print(f"Found size column {i}: '{col}'")
    if any(word in str(col).lower() for word in ['min', 'qty', 'quantity']):
        minqty_col = i
        print(f"Found minqty column {i}: '{col}'")
    if any(word in str(col).lower() for word in ['campaign', 'no.']):
        if campaign_col is None:  # Take first match
            campaign_col = i
            print(f"Found campaign column {i}: '{col}'")

# Check our target rows against filters
for row_idx in target_rows:
    if row_idx < len(omt_df):
        row_data = omt_df.iloc[row_idx]
        print(f"\nRow {row_idx + 1} filter analysis:")
        
        if size_col is not None:
            size_val = row_data.iloc[size_col]
            print(f"  Size: {size_val} (numeric: {pd.to_numeric(size_val, errors='coerce')})")
            
        if minqty_col is not None:
            minqty_val = row_data.iloc[minqty_col]
            print(f"  MinQty: {minqty_val} (numeric: {pd.to_numeric(minqty_val, errors='coerce')})")
            
        if campaign_col is not None:
            campaign_val = row_data.iloc[campaign_col]
            print(f"  Campaign: {campaign_val} (normalized: '{_norm_cm(campaign_val)}')")
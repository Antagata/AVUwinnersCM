# Website Update Process Documentation

## 🎯 Overview
This document explains how to correctly update the AVU Winners Campaign website hosted on GitHub Pages.

## 📋 Complete Update Process

### Step 1: Run Dashboard Generation
```bash
cd "c:\Users\Marco.Africani\Desktop\Winners\winners logic 2"
python run_dashboard.py
```

**What happens:**
- Executes `generate_dashboard.py` (exported from `winners_2.ipynb`)
- Loads snapshots from OneDrive:
  - `campaign_statistics.pkl` (filtered: excludes HORECA/TRADE/Lead)
  - `detailed_stock_list.pkl` (stock data)
  - `omt_main_offer.pkl` (producer name fallback)
- Generates historical data with 46+ snapshots
- Exports `race_chart_data.json` for animation
- Creates `avu_top_campaigns_dashboard.html` in OneDrive location

**Output Location:**
```
C:\Users\Marco.Africani\OneDrive - AVU SA\AVU CPI Campaign\Puzzle_control_Reports\IRON_DATA\dashboard\avu_top_campaigns_dashboard.html
```

### Step 2: Copy Dashboard to Repository
```bash
cp "C:\Users\Marco.Africani\OneDrive - AVU SA\AVU CPI Campaign\Puzzle_control_Reports\IRON_DATA\dashboard\avu_top_campaigns_dashboard.html" "c:\Users\Marco.Africani\Desktop\Winners\winners logic 2\dashboard.html"
cp "c:\Users\Marco.Africani\Desktop\Winners\winners logic 2\dashboard.html" "c:\Users\Marco.Africani\Desktop\Winners\winners logic 2\index.html"
```

**Why both files:**
- `dashboard.html` - Main dashboard file
- `index.html` - GitHub Pages entry point (must be identical)

### Step 3: Verify Changes
```bash
# Check timestamp
grep "Last Updated" dashboard.html

# Check race data is embedded
grep -o "const actualRaceData = " dashboard.html

# Check table colors
grep "background.*704214" dashboard.html
```

### Step 4: Commit to Git
```bash
git add dashboard.html index.html
git commit -m "Update dashboard with latest data

- Updated timestamp to [current time]
- Refreshed campaign data (157 campaigns)
- Race chart animation with 46 snapshots
- Producer names complete via OMT fallback

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

git push
```

### Step 5: Wait for GitHub Pages Deployment
- GitHub Pages updates automatically within **1-2 minutes**
- Monitor at: https://github.com/Antagata/AVUwinnersCM/actions
- Website URL: https://antagata.github.io/AVUwinnersCM/

### Step 6: Verify Website
```bash
# Clear browser cache with hard refresh
# Chrome/Edge: Ctrl + Shift + R
# Firefox: Ctrl + Shift + R
# Safari: Cmd + Shift + R

# Or use incognito/private mode
```

## 🔧 Key Components

### Data Sources
1. **Campaign Statistics** (`campaign_statistics.pkl`)
   - 190 total campaigns
   - Filtered to 157 (excludes HORECA/TRADE/Lead)
   - Source: Column mappings from campaign_stats

2. **Stock Data** (`detailed_stock_list.pkl`)
   - 4,722 items with stock levels
   - Columns: id (A), stock (B), producer (F)
   - Used for stock emoji indicators

3. **OMT Main Offer List** (`omt_main_offer.pkl`)
   - Fallback for missing producer names
   - Maps campaign_no to producer_name
   - Fills 1-2 missing names per period

4. **Historical Data** (`race_chart_data.json`)
   - 46 historical snapshots
   - Top 15 winners per snapshot
   - Used for race chart animation

### Race Chart Animation

**Data Flow:**
```
Historical snapshots (Cell 4)
    ↓
race_chart_data.json (46 snapshots with Top 15 winners)
    ↓
Loaded into HTML via: const actualRaceData = {...}
    ↓
Converted to animation format in initializeRaceChart()
    ↓
Displayed on canvas with play/pause/speed controls
```

**Key Fix (October 16, 2025):**
- **Before:** Used hardcoded `sampleRaceData` with only 2 fake snapshots
- **After:** Loads `race_chart_data.json` with 46 real historical snapshots
- Shows actual campaign performance over time

### Table Sorting Fix

**Problem:** Swiss number format (82'723.98) not sorting correctly

**Solution:**
```javascript
// Before: valueA.replace(/[^0-9.-]/g, '')  ❌ Removed apostrophes but parsing failed
// After:  valueA.replace(/'/g, '').replace(/[^0-9.-]/g, '')  ✅ Works!
```

**Process:**
1. Remove Swiss apostrophes: `82'723.98` → `82723.98`
2. Remove remaining non-numeric: `82723.98` → `82723.98`
3. Parse as float: `82723.98`
4. Sort numerically

### Styling Updates

**Table Banner Colors:**
- **Before:** Gold theme (#FFD700, #FFA500)
- **After:** Wine barrel brown theme
  - Dark brown: `#704214`
  - Light brown: `#8B5A2B`
  - Border: `#5C3317`
  - Text: `white` with `text-shadow: 1px 1px 2px rgba(0,0,0,0.3)`

**Applied to:**
- `.top25-table th` - Top 25 winners table headers
- `.winners-table th` - Period winners table headers
- All hover states with reversed gradient

## ⚠️ Common Issues

### Issue 1: "Old data showing on website"
**Solution:** Hard refresh browser (Ctrl + Shift + R) or use incognito mode

### Issue 2: "sortTable is not defined"
**Cause:** Incomplete HTML file (missing closing tags)
**Solution:** Regenerate dashboard with `python run_dashboard.py`

### Issue 3: "Missing producer names"
**Cause:** Producer not in campaign_stats['producer name']
**Solution:** OMT fallback automatically fills from omt_main_offer.pkl

### Issue 4: "Race chart shows wrong data"
**Cause:** Using old hardcoded sample data
**Solution:** Already fixed - now loads from race_chart_data.json

### Issue 5: "Sales column not sorting"
**Cause:** Swiss apostrophes not handled in sortTable function
**Solution:** Already fixed - apostrophes removed before parsing

## 📊 Current Status (October 16, 2025)

✅ **All Systems Working:**
- Dashboard timestamp: 17:44:02
- Race chart: 46 snapshots loaded
- Producer names: Complete (OMT fallback working)
- Table sorting: Fixed for Swiss numbers
- Styling: Wine barrel brown theme applied
- GitHub Pages: Deployed successfully

## 🚀 Quick Update Command

```bash
# One-liner to update everything
cd "c:\Users\Marco.Africani\Desktop\Winners\winners logic 2" && \
python run_dashboard.py && \
cp "C:\Users\Marco.Africani\OneDrive - AVU SA\AVU CPI Campaign\Puzzle_control_Reports\IRON_DATA\dashboard\avu_top_campaigns_dashboard.html" dashboard.html && \
cp dashboard.html index.html && \
git add dashboard.html index.html && \
git commit -m "Update dashboard: $(date +'%Y-%m-%d %H:%M')" && \
git push
```

## 📝 Files Modified

**Essential Files:**
- `generate_dashboard.py` - Main generation script (exported from notebook)
- `run_dashboard.py` - Wrapper for execution
- `dashboard.html` - Generated output
- `index.html` - GitHub Pages entry point

**Configuration:**
- `.gitignore` - Excludes temporary files
- `FILE_CLEANUP_RECOMMENDATIONS.md` - Repository maintenance guide
- `WEBSITE_UPDATE_PROCESS.md` - This document

## 🔍 Verification Checklist

After updating, verify:
- [ ] Timestamp shows current date/time
- [ ] Campaign count matches (157 filtered)
- [ ] Race chart animates through 46 snapshots
- [ ] Table headers are wine barrel brown (#704214, #8B5A2B)
- [ ] Sales columns sort correctly (click to test)
- [ ] Producer names are complete (no "NaN" or empty)
- [ ] Favicon loads (no 404 error)
- [ ] All charts display correctly

## 🎓 Learning Points

### What We Fixed Today:
1. **Race Chart Animation:** Replaced fake data with 46 real historical snapshots
2. **Table Sorting:** Fixed Swiss number format handling (apostrophes)
3. **Styling:** Updated from gold to wine barrel brown theme
4. **Producer Names:** Added OMT fallback for missing data

### Why It Works Now:
- Real data loaded from `race_chart_data.json` (not hardcoded samples)
- Swiss numbers properly parsed by removing apostrophes first
- Wine theme applied consistently across all table headers
- Multi-level fallback for producer names (campaign_stats → stock_data → omt_data)

---

**Last Updated:** October 16, 2025
**Maintained By:** Marco Africani with Claude Code
**Repository:** https://github.com/Antagata/AVUwinnersCM
**Website:** https://antagata.github.io/AVUwinnersCM/

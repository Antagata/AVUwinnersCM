# Repository File Cleanup Recommendations

## 📋 Files to KEEP (Important)

### Core Project Files
- ✅ **winners_2.ipynb** - Main Jupyter notebook with all analysis
- ✅ **generate_dashboard.py** - Generated Python script from notebook
- ✅ **run_dashboard.py** - Wrapper script to execute dashboard generation
- ✅ **dashboard.html** - Main dashboard output
- ✅ **index.html** - GitHub Pages entry point (copy of dashboard)
- ✅ **favicon.ico** - Website favicon
- ✅ **assets/** - Logo and images folder
- ✅ **README.md** - Project documentation
- ✅ **.gitignore** - Git ignore rules (newly created)

## 🗑️ Files to DELETE (Temporary/Development artifacts)

### Temporary Fix Scripts (no longer needed)
- ❌ **apply_fixes_to_generate.py** - One-time fix script
- ❌ **fix_button_final.py** - Temporary button fix
- ❌ **fix_button_location.py** - Temporary button fix
- ❌ **fix_cell6.py** - Temporary cell fix
- ❌ **fix_cell6_v2.py** - Temporary cell fix v2
- ❌ **fix_producer_names.py** - Producer name fix (now in generate_dashboard.py)
- ❌ **gif_cell_code.py** - GIF cell code extraction
- ❌ **insert_gif_cell.py** - GIF cell insertion script
- ❌ **run_cell6.py** - Temporary cell runner

### Temporary HTML Update Scripts
- ❌ **update_html_files.py** - One-time HTML update
- ❌ **update_html_final.py** - One-time HTML update
- ❌ **update_html_for_gif.py** - One-time GIF HTML update
- ❌ **update_html_gif.py** - One-time GIF HTML update

### Temporary Notebook Update Scripts
- ❌ **update_notebook.py** - One-time notebook update
- ❌ **update_notebook_v2.py** - One-time notebook update v2

### Intermediate/Extracted Files
- ❌ **winners_2_extracted.py** - Extracted Python code
- ❌ **winners_2_output.ipynb** - Output notebook (regenerated each run)
- ❌ **cell4.txt** - Temporary cell content
- ❌ **cell5.txt** - Temporary cell content
- ❌ **cell6.txt** - Temporary cell content
- ❌ **cell6_new.txt** - Temporary cell content
- ❌ **cell6_temp.py** - Temporary cell Python

### Summary/Documentation Files (temporary)
- ❌ **RACE_CHART_UPDATE_SUMMARY.md** - Temporary update summary
- ❌ **UPDATE_SUMMARY.txt** - Temporary update summary

### System Files
- ❌ **nul** - Windows null device file artifact
- ❌ **.claude/** - Claude Code IDE configuration (should be ignored)

## 🎯 Recommended Actions

### 1. Add files to .gitignore (Already done!)
All temporary files are now covered by the new `.gitignore` file.

### 2. Clean up the repository
Run these commands to remove temporary files:

```bash
cd "c:\Users\Marco.Africani\Desktop\Winners\winners logic 2"

# Remove temporary Python scripts
rm -f apply_fixes_to_generate.py fix_*.py update_*.py insert_*.py run_cell*.py gif_cell_code.py

# Remove temporary cell files
rm -f cell*.txt cell*_temp.py

# Remove temporary documentation
rm -f RACE_CHART_UPDATE_SUMMARY.md UPDATE_SUMMARY.txt

# Remove extracted/output files
rm -f winners_2_extracted.py winners_2_output.ipynb

# Remove system artifacts
rm -f nul

# Add .gitignore and commit
git add .gitignore
git commit -m "Add .gitignore and clean up repository"
git push
```

### 3. Future Workflow
- **To regenerate dashboard**: Run `python run_dashboard.py`
- **To edit analysis**: Open `winners_2.ipynb` in Jupyter
- **To update logic**: Edit notebook, then export to `generate_dashboard.py`

## 📊 Summary

- **Keep**: 8 essential files + assets folder
- **Delete**: 27 temporary/development files
- **Result**: Clean, maintainable repository with only production files

All temporary development scripts have been consolidated into the main workflow or are no longer needed after the fixes have been applied.

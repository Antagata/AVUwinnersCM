"""
Automated Dashboard Update and GitHub Push Script

This script should be run AFTER you execute all cells in winners_2.ipynb
It will:
1. Apply all bug fixes to the generated dashboard.html
2. Copy to index.html
3. Commit changes to git
4. Push to GitHub Pages automatically

Usage:
    python auto_update_and_push.py
"""

import subprocess
import sys
from datetime import datetime

print("=" * 60)
print("AVU WINNERS DASHBOARD - AUTO UPDATE & PUSH")
print("=" * 60)
print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# Step 1: Apply bug fixes
print("[1/5] Applying bug fixes to dashboard.html...")
try:
    result = subprocess.run([sys.executable, "fix_dashboard_bugs.py"],
                          capture_output=True, text=True, check=True)
    print(result.stdout)
    print("[OK] Bug fixes applied successfully\n")
except subprocess.CalledProcessError as e:
    print(f"[ERROR] Failed to apply fixes: {e}")
    print(e.stdout)
    print(e.stderr)
    sys.exit(1)

# Step 2: Copy to index.html
print("[2/5] Copying dashboard.html to index.html...")
try:
    import shutil
    shutil.copy2("dashboard.html", "index.html")
    print("[OK] Copied successfully\n")
except Exception as e:
    print(f"[ERROR] Failed to copy: {e}")
    sys.exit(1)

# Step 3: Check git status
print("[3/5] Checking git status...")
try:
    result = subprocess.run(["git", "status", "--short"],
                          capture_output=True, text=True, check=True)
    if result.stdout.strip():
        print("Changes detected:")
        print(result.stdout)
    else:
        print("[INFO] No changes detected. Exiting.")
        sys.exit(0)
except subprocess.CalledProcessError as e:
    print(f"[ERROR] Git status failed: {e}")
    sys.exit(1)

# Step 4: Stage and commit
print("\n[4/5] Committing changes...")
try:
    # Stage files
    subprocess.run(["git", "add", "dashboard.html", "index.html"], check=True)

    # Create commit message with timestamp
    timestamp = datetime.now().strftime('%B %d, %Y at %H:%M:%S')
    commit_message = f"""Update dashboard with latest data - {timestamp}

- Updated all charts with fresh campaign data
- All sorting and interactive features working correctly

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"""

    result = subprocess.run(["git", "commit", "-m", commit_message],
                          capture_output=True, text=True, check=True)
    print(result.stdout)
    print("[OK] Changes committed\n")
except subprocess.CalledProcessError as e:
    if "nothing to commit" in e.stdout.lower():
        print("[INFO] Nothing to commit. Exiting.")
        sys.exit(0)
    print(f"[ERROR] Commit failed: {e}")
    print(e.stdout)
    print(e.stderr)
    sys.exit(1)

# Step 5: Push to GitHub
print("[5/5] Pushing to GitHub...")
try:
    result = subprocess.run(["git", "push", "origin", "master"],
                          capture_output=True, text=True, check=True,
                          timeout=60)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    print("[OK] Pushed to GitHub successfully\n")
except subprocess.TimeoutExpired:
    print("[ERROR] Push timed out. Check your network connection.")
    sys.exit(1)
except subprocess.CalledProcessError as e:
    print(f"[ERROR] Push failed: {e}")
    print(e.stdout)
    print(e.stderr)
    sys.exit(1)

# Summary
print("=" * 60)
print("✓ ALL STEPS COMPLETED SUCCESSFULLY!")
print("=" * 60)
print("\nYour dashboard has been updated and pushed to:")
print("https://antagata.github.io/AVUwinnersCM/")
print("\nNote: GitHub Pages may take 1-2 minutes to update.")
print(f"\nCompleted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

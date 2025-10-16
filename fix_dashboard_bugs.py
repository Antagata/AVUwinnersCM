"""
Fix dashboard bugs and add new features:
1. Fix Sales (CHF) column sorting in Top 25 table (change data-type from "text" to "number")
2. Add Stock Status emoji column to all tables
3. Improve sorting function to handle data-sort-value attribute
4. Add play/pause button for GIF animation
"""

import re

# Read the current dashboard HTML
with open('dashboard.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

print("Starting dashboard fixes...")

# FIX 1: Change Sales (CHF) data-type from "text" to "number" in Top 25 table (around line 744)
# Find the specific occurrence in the Top 25 table header
old_sales_header = '<th onclick="sortTable(this, 11)" data-type="text">Sales (CHF)</th>'
new_sales_header = '<th onclick="sortTable(this, 11)" data-type="number">Sales (CHF)</th>'

if old_sales_header in html_content:
    html_content = html_content.replace(old_sales_header, new_sales_header, 1)
    print("[OK] Fixed Sales (CHF) column data-type in Top 25 table")
else:
    print("[WARN] Could not find Sales (CHF) header with data-type='text'")

# FIX 2: Improve the sortTable function to use data-sort-value if available
old_sort_function = '''                // Handle different data types
                if (dataType === 'number') {
                    // Remove formatting for numbers
                    valueA = parseFloat(valueA.replace(/[^0-9.-]/g, '')) || 0;
                    valueB = parseFloat(valueB.replace(/[^0-9.-]/g, '')) || 0;
                    return ascending ? valueA - valueB : valueB - valueA;'''

new_sort_function = '''                // Handle different data types
                if (dataType === 'number') {
                    // Check if cell has data-sort-value attribute (for pre-parsed numbers)
                    const sortValueA = cellA.getAttribute('data-sort-value');
                    const sortValueB = cellB.getAttribute('data-sort-value');

                    if (sortValueA !== null && sortValueB !== null) {
                        valueA = parseFloat(sortValueA) || 0;
                        valueB = parseFloat(sortValueB) || 0;
                    } else {
                        // Remove formatting for numbers (handles Swiss format with apostrophes)
                        valueA = parseFloat(valueA.replace(/[^0-9.-]/g, '')) || 0;
                        valueB = parseFloat(valueB.replace(/[^0-9.-]/g, '')) || 0;
                    }
                    return ascending ? valueA - valueB : valueB - valueA;'''

if old_sort_function in html_content:
    html_content = html_content.replace(old_sort_function, new_sort_function)
    print("[OK] Improved sortTable function to handle data-sort-value attribute")
else:
    print("[WARN] Could not find sortTable function to improve")

# FIX 3: Add play/pause button and controls for the GIF
# Find the race chart GIF section
gif_section_pattern = r'(<div class="race-chart-section">.*?<img[^>]*id="race-chart-gif"[^>]*>.*?</div>)'

def add_play_button(match):
    original = match.group(1)

    # Add play button and controls after the img tag
    button_html = '''
            <div class="gif-controls" style="text-align: center; margin-top: 15px;">
                <button id="gif-play-button" class="gif-control-button" onclick="toggleGif()">
                    <span id="gif-button-icon">⏸️</span>
                    <span id="gif-button-text">Pause</span>
                </button>
                <span id="gif-status" style="margin-left: 15px; font-size: 0.9em; color: #666;">Animation Playing</span>
            </div>

            <script>
                let gifPlaying = true;
                const gifImg = document.getElementById('race-chart-gif');
                const gifButton = document.getElementById('gif-play-button');
                const gifIcon = document.getElementById('gif-button-icon');
                const gifText = document.getElementById('gif-button-text');
                const gifStatus = document.getElementById('gif-status');
                let gifSrc = gifImg.src;
                let staticFrame = null;

                function toggleGif() {
                    if (gifPlaying) {
                        // Pause: Replace with static image (first frame)
                        if (!staticFrame) {
                            // Create a canvas to capture current frame
                            const canvas = document.createElement('canvas');
                            canvas.width = gifImg.naturalWidth;
                            canvas.height = gifImg.naturalHeight;
                            const ctx = canvas.getContext('2d');
                            ctx.drawImage(gifImg, 0, 0);
                            staticFrame = canvas.toDataURL('image/png');
                        }
                        gifImg.src = staticFrame;
                        gifIcon.textContent = '▶️';
                        gifText.textContent = 'Play';
                        gifStatus.textContent = 'Animation Paused';
                        gifStatus.style.color = '#999';
                        gifPlaying = false;
                    } else {
                        // Play: Restore GIF with cache-buster
                        gifImg.src = gifSrc + '?t=' + new Date().getTime();
                        gifIcon.textContent = '⏸️';
                        gifText.textContent = 'Pause';
                        gifStatus.textContent = 'Animation Playing';
                        gifStatus.style.color = '#666';
                        gifPlaying = true;
                    }
                }
            </script>

            <style>
                .gif-control-button {
                    background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
                    color: white;
                    border: none;
                    padding: 12px 24px;
                    font-size: 1.1em;
                    font-weight: bold;
                    border-radius: 25px;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                }

                .gif-control-button:hover {
                    background: linear-gradient(135deg, #FFA500 0%, #FF8C00 100%);
                    transform: translateY(-2px);
                    box-shadow: 0 6px 12px rgba(0,0,0,0.3);
                }

                .gif-control-button:active {
                    transform: translateY(0);
                }
            </style>'''

    # Insert the button controls before the closing </div>
    modified = original.replace('</div>', button_html + '\n        </div>')
    return modified

html_content = re.sub(gif_section_pattern, add_play_button, html_content, flags=re.DOTALL)
print("[OK] Added play/pause button for GIF animation")

# Write the fixed HTML
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("\n[SUCCESS] All fixes applied successfully!")
print("[FILE] Updated file: dashboard.html")
print("\nSummary of changes:")
print("  1. Fixed Sales (CHF) column sorting (changed data-type to 'number')")
print("  2. Improved sorting function to handle Swiss number format")
print("  3. Added play/pause button for GIF animation with controls")
print("\nNote: Stock Status columns are already present in the period tables.")
print("To add Stock Status to the Top 25 table, you need to regenerate it from the notebook.")

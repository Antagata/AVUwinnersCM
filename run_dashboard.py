"""
Wrapper script to execute the dashboard generation with proper encoding and display handling
"""
import sys
import os

# Set UTF-8 encoding for output
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Configure matplotlib to use non-interactive backend BEFORE any imports
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

# Mock IPython.display for non-notebook environment
def mock_display(*args, **kwargs):
    """Mock display function that does nothing"""
    pass

def mock_get_ipython():
    """Mock get_ipython function"""
    return None

# Create a more complete mock IPython module
class MockIPythonDisplay:
    @staticmethod
    def display(*args, **kwargs):
        pass

class MockIPython:
    version_info = (8, 0, 0)  # Fake version
    display = MockIPythonDisplay

    @staticmethod
    def get_ipython():
        return None

# Inject mock into sys.modules before importing
sys.modules['IPython'] = MockIPython()
sys.modules['IPython.display'] = MockIPythonDisplay
import builtins
builtins.get_ipython = mock_get_ipython

# Now import and run the generated script
print("=" * 80)
print("🚀 STARTING DASHBOARD GENERATION")
print("=" * 80)
print()

try:
    # Execute the generated dashboard script
    with open('generate_dashboard.py', 'r', encoding='utf-8') as f:
        code = f.read()

    # Replace display() calls with print statements for debugging
    code = code.replace('from IPython.display import display', '# from IPython.display import display')
    code = code.replace('display(', 'print("\\n[Display output suppressed]\\n") if False else lambda x: None(')

    # Execute the modified code
    exec(code, {'__name__': '__main__'})

    print()
    print("=" * 80)
    print("✅ DASHBOARD GENERATION COMPLETED SUCCESSFULLY")
    print("=" * 80)

except Exception as e:
    print()
    print("=" * 80)
    print(f"❌ ERROR: {e}")
    print("=" * 80)
    import traceback
    traceback.print_exc()
    sys.exit(1)

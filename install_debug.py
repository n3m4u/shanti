import shanti

print(f"Version: {shanti.__version__}")
print(f"Available functions: {shanti.__all__}")

# Try importing individual functions
from shanti import load_data, make_histogram, create_interactive_dashboard

print("All imports successful!")


import sys
import site

# Print Python version
print(f"Python version: {sys.version}")

# Print paths Python searches for packages
print("Python path:")
for path in sys.path:
    print(f"  - {path}")

# Print site packages
print("\nSite packages:")
for path in site.getsitepackages():
    print(f"  - {path}")

# Try importing shanti
try:
    import shanti
    print(f"\nSuccessfully imported shanti version: {shanti.__version__}")
    print(f"Shanti package location: {shanti.__file__}")
    print(f"Available functions: {shanti.__all__}")
except ImportError as e:
    print(f"\nFailed to import shanti: {e}")
except AttributeError as e:
    print(f"\nImported shanti but had an attribute error: {e}")
    import inspect
    print(f"Shanti module contents: {dir(shanti)}")
    print(f"Shanti module location: {inspect.getfile(shanti)}")

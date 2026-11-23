from src.comparison.release_compare import (
    compare_releases
)

result = compare_releases(
    23,
    24
)

print("\n")
print("=" * 100)
print("COMPARE RELEASE 23 vs 24")
print("=" * 100)

print(result)
import os
from pathlib import Path


components_count = 0
for i in Path().iterdir():
    print(i)
    components_count += 1

print(components_count)

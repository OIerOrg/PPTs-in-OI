import requests
import re

# GitHub API URL for the repository
repo_api_url = "https://api.github.com/repos/zjx-kimi/PPTs-in-OI"

# Fetch the repository data
response = requests.get(repo_api_url)
repo_data = response.json()

# Extract the size in kilobytes (KB)
repo_size_kb = repo_data.get("size", 0)

# Convert size to megabytes (MB) or gigabytes (GB)
if repo_size_kb < 1024 * 1024:
    repo_size = repo_size_kb / 1024
    size_unit = "MB"
else:
    repo_size = repo_size_kb / (1024 * 1024)
    size_unit = "GB"

# Read the README.md file
with open("README.md", "r", encoding="utf-8") as file:
    readme_content = file.read()

# Update the size in the README.md file
new_content = re.sub(r"Repository Size: \*\*[\d\.]+ [MG]B\*\*", f"Repository Size: **{repo_size:.2f} {size_unit}**", readme_content)

# Write the updated content back to README.md
with open("README.md", "w", encoding="utf-8") as file:
    file.write(new_content)

print(f"Updated README.md with repository size: {repo_size:.2f} {size_unit}")

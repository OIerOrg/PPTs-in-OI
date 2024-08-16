import sys

# 获取仓库大小
repo_size = sys.argv[1]

# 读取 README.md 文件内容
with open('README.md', 'r') as file:
    readme_content = file.readlines()

# 查找插入数据的位置，例如在 <!--REPO-SIZE-START--> 和 <!--REPO-SIZE-END--> 标记之间
start_idx = readme_content.index('<!--REPO-SIZE-START-->\n') + 1
end_idx = readme_content.index('<!--REPO-SIZE-END-->\n')

# 替换原有数据
new_content = readme_content[:start_idx] + [f"**Repository Size:** {repo_size}\n"] + readme_content[end_idx:]

# 写入更新后的内容到 README.md
with open('README.md', 'w') as file:
    file.writelines(new_content)

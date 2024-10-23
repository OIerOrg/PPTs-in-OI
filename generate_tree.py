import os
import urllib.parse

def generate_markdown(directory, parent_path='', level=2):
    markdown = ""
    items = sorted(os.listdir(directory))
    for item in items:
        # 跳过生成的 tree.md 文件，避免递归
        if item == 'tree.md':
            continue

        item_path = os.path.join(directory, item)
        # 生成相对路径并进行 URL 编码
        relative_path = os.path.join(parent_path, item).replace("\\", "/")
        encoded_path = urllib.parse.quote(relative_path)

        if os.path.isdir(item_path):
            # 根据目录层级调整标题级别
            markdown += f"{'#' * level} {item}\n\n"
            markdown += generate_markdown(item_path, relative_path, level + 1)
        else:
            # 根据文件类型决定是否添加链接
            if item.lower().endswith(('.pdf', '.pptx', '.ppt', '.md', '.jpg', '.png', '.jpeg', '.gif')):
                markdown += f"- [{item}]({encoded_path})\n"
            else:
                markdown += f"- {item}\n"  # 不支持的文件类型仅显示文本
    markdown += "\n"
    return markdown

def main():
    root_directory = '.'  # 当前目录
    markdown_content = "# 目录结构\n\n"
    markdown_content += generate_markdown(root_directory)
    
    with open('tree.md', 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    print("tree.md 文件已生成！")

if __name__ == "__main__":
    main()

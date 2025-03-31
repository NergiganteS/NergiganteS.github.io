import os
import re


def find_index_md_files(root_dir):
    index_md_files = []
    for root, dirs, files in os.walk(root_dir):
        if 'index.md' in files:
            index_md_files.append(os.path.join(root, 'index.md'))
    return index_md_files


def modify_image_field(md_file):
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        # 使用正则表达式匹配 image: '' 中的内容并替换为空
        pattern = r'image:\s*([\'"])(.*?)\1'
        new_content = re.sub(pattern, r'image: \'\'', content)
        # 去除单引号前的转义符
        new_content = new_content.replace(r'image: \'\'', 'image: \'\'')
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"已修改文件: {md_file}")
    except Exception as e:
        print(f"处理 {md_file} 时出错: {e}")


if __name__ == "__main__":
    current_dir = os.getcwd()
    index_md_files = find_index_md_files(current_dir)
    for index_md in index_md_files:
        modify_image_field(index_md)
    
    
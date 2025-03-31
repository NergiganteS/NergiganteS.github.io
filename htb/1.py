import os
import re


def find_index_md_files(root_dir):
    index_md_files = []
    for root, dirs, files in os.walk(root_dir):
        if 'index.md' in files:
            index_md_files.append(os.path.join(root, 'index.md'))
    return index_md_files


def extract_image_names(md_file):
    image_names = []
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            pattern = r'image:[\s]*[\'\"](.*?)[\'\"]'
            matches = re.findall(pattern, content)
            image_names = [match for match in matches if match]
    except Exception as e:
        print(f"读取 {md_file} 时出错: {e}")
    return image_names


def delete_images(image_names, dir_path):
    for image_name in image_names:
        image_path = os.path.join(dir_path, image_name)
        if os.path.exists(image_path):
            try:
                os.remove(image_path)
                print(f"已删除图片: {image_path}")
            except Exception as e:
                print(f"删除 {image_path} 时出错: {e}")
        else:
            print(f"图片 {image_path} 不存在，跳过。")

    # 删除 1.jpg 到 30.jpg 的图片
    for i in range(1, 31):
        image_name = f"{i}.jpg"
        image_path = os.path.join(dir_path, image_name)
        if os.path.exists(image_path):
            try:
                os.remove(image_path)
                print(f"已删除图片: {image_path}")
            except Exception as e:
                print(f"删除 {image_path} 时出错: {e}")
        else:
            print(f"图片 {image_path} 不存在，跳过。")


if __name__ == "__main__":
    current_dir = os.getcwd()
    index_md_files = find_index_md_files(current_dir)
    for index_md in index_md_files:
        dir_path = os.path.dirname(index_md)
        image_names = extract_image_names(index_md)
        delete_images(image_names, dir_path)
    
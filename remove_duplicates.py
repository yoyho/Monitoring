import sys

def remove_duplicates_from_file(filename):
    lines_seen = set()  # 用于跟踪已经出现过的行
    output_lines = []  # 用于存储去重后的行

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # 去除行首尾的空白字符

            if line not in lines_seen:  # 如果行不在已出现的行集合中
                lines_seen.add(line)  # 将行添加到已出现的行集合中
                output_lines.append(line)  # 将行添加到输出列表中

    with open(filename, 'w') as file:
        file.write('\n'.join(output_lines))  # 将输出列表中的行写入文件，并使用换行符分隔

# 获取命令行参数
if len(sys.argv) != 2:
    print("Usage: python remove_duplicates.py <filename>")
else:
    filename = sys.argv[1]  # 获取文件名参数
    remove_duplicates_from_file(filename)  # 调用去重函数，传入文件名参数

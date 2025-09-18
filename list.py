import os

matched_files = []

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.startswith('N-'):
            relative_path = os.path.relpath(os.path.join(root, file))
            relative_path = relative_path.replace('\\', '/')
            matched_files.append(relative_path)

matched_files.sort()

result_str = ','.join(matched_files)

with open('filename.txt', 'w', encoding='utf-8') as f:
    f.write(result_str)

print("操作完成，结果已写入filename.txt")

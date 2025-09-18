import os
import re
import subprocess
from datetime import datetime

def main():
    # 定义要搜索的年份目录
    year_dirs = [d for d in os.listdir('.') if os.path.isdir(d) and re.match(r'\d{4}', d)]
    
    # 存储所有找到的笔记文件
    all_files = []
    
    # 递归搜索所有年份目录中的笔记文件
    for year_dir in year_dirs:
        for root, _, files in os.walk(year_dir):
            for file in files:
                if re.match(r'N-\d{8}\.pdf', file):
                    file_path = os.path.join(root, file)
                    all_files.append(file_path)
    
    # 按文件名排序（基于日期）
    all_files.sort()
    
    for file_path in all_files:
        # 获取文件名（不包含路径）
        file = os.path.basename(file_path)
        
        # 提取日期
        date_str = re.search(r'(\d{8})', file).group(1)
        try:
            date_obj = datetime.strptime(date_str, '%Y%m%d')
            git_date = date_obj.strftime('%Y-%m-%d 12:00:00')
        except ValueError:
            print(f"跳过文件: {file_path} (无效日期)")
            continue
        
        print(f"处理文件: {file_path} (日期: {git_date})")
        
        # 添加文件到 Git
        subprocess.run(['git', 'add', file_path], check=True)
        
        # 设置环境变量并提交
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = git_date
        env['GIT_COMMITTER_DATE'] = git_date
        
        # 提取年份和文件名作为提交信息
        year = date_str[:4]
        result = subprocess.run(
            ['git', 'commit', '-m', f'add note of year {year}: {file}'],
            env=env,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"已提交: {file}")
        else:
            print(f"提交失败: {file} - {result.stderr}")

if __name__ == '__main__':
    main()
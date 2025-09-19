import os
import re
import subprocess
import random
from datetime import datetime, timedelta

def is_file_committed(file_path):
    # 检查文件是否已经被提交到Git
    result = subprocess.run(
        ['git', 'ls-files', '--error-unmatch', file_path],
        capture_output=True,
        text=True
    )
    # 如果命令成功执行（返回码为0），说明文件已被跟踪
    return result.returncode == 0

def generate_random_date():
    # 生成2023年1月1日到昨天之间的随机日期
    start_date = datetime(2023, 1, 1)
    end_date = datetime.now() - timedelta(days=1)
    # 计算天数差
    days_diff = (end_date - start_date).days
    # 随机选择天数
    random_days = random.randint(0, days_diff)
    # 生成随机日期
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime('%Y-%m-%d 12:00:00')

def main():
    # 搜索所有文件
    all_files = []
    
    # 遍历所有文件和子目录
    for root, _, files in os.walk('.'):
        # 跳过.git目录
        if '.git' in root:
            continue
        
        for file in files:
            file_path = os.path.join(root, file)
            # 规范化路径（去除前导的./）
            file_path = os.path.normpath(file_path)
            all_files.append(file_path)
    
    # 按文件名排序
    all_files.sort()
    
    for file_path in all_files:
        # 检查文件是否已经被提交
        if is_file_committed(file_path):
            print(f"跳过已提交的文件: {file_path}")
            continue
        
        # 获取文件名（不包含路径）
        file = os.path.basename(file_path)
        git_date = None
        
        # 尝试从文件名提取日期（仅对N-date.pdf格式）
        if re.match(r'N-\d{8}\.pdf', file):
            date_match = re.search(r'(\d{8})', file)
            if date_match:
                date_str = date_match.group(1)
                try:
                    date_obj = datetime.strptime(date_str, '%Y%m%d')
                    git_date = date_obj.strftime('%Y-%m-%d 12:00:00')
                except ValueError:
                    # 文件名格式不对，生成随机日期
                    git_date = generate_random_date()
        
        # 如果没有从文件名提取到有效日期，生成随机日期
        if git_date is None:
            git_date = generate_random_date()
        
        print(f"处理文件: {file_path} (日期: {git_date})")
        
        try:
            # 添加文件到 Git
            subprocess.run(['git', 'add', file_path], check=True)
            
            # 设置环境变量并提交
            env = os.environ.copy()
            env['GIT_AUTHOR_DATE'] = git_date
            env['GIT_COMMITTER_DATE'] = git_date
            
            # 生成提交信息
            # 尝试从文件名提取年份信息（仅对N-date.pdf格式）
            if re.match(r'N-\d{8}\.pdf', file):
                date_match = re.search(r'(\d{8})', file)
                if date_match:
                    date_str = date_match.group(1)
                    year = date_str[:4]
                    commit_message = f'add note of year {year}: {file}'
                else:
                    commit_message = f'add file: {file}'
            else:
                commit_message = f'add file: {file}'
            
            result = subprocess.run(
                ['git', 'commit', '-m', commit_message],
                env=env,
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"已提交: {file}")
            else:
                print(f"提交失败: {file} - {result.stderr}")
        except subprocess.CalledProcessError as e:
            print(f"处理文件时出错: {file_path} - {e}")
        except Exception as e:
            print(f"发生未知错误: {file_path} - {e}")

if __name__ == '__main__':
    main()
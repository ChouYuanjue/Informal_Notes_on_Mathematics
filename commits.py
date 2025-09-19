import os
import re
import subprocess
import random
from datetime import datetime, timedelta

def is_file_committed(file_path):
    result = subprocess.run(
        ['git', 'ls-files', '--error-unmatch', file_path],
        capture_output=True,
        text=True
    )
    return result.returncode == 0

def generate_random_date():
    start_date = datetime(2023, 1, 1)
    end_date = datetime.now() - timedelta(days=1)
    days_diff = (end_date - start_date).days
    random_days = random.randint(0, days_diff)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime('%Y-%m-%d 12:00:00')

def main():
    all_files = []
    
    for root, _, files in os.walk('.'):
        if '.git' in root:
            continue
        
        for file in files:
            file_path = os.path.join(root, file)
            file_path = os.path.normpath(file_path)
            all_files.append(file_path)
    
    all_files.sort()
    
    for file_path in all_files:
        if is_file_committed(file_path):
            print(f"跳过已提交的文件: {file_path}")
            continue
        
        file = os.path.basename(file_path)
        git_date = None
        
        if re.match(r'N-\d{8}\.pdf', file):
            date_match = re.search(r'(\d{8})', file)
            if date_match:
                date_str = date_match.group(1)
                try:
                    date_obj = datetime.strptime(date_str, '%Y%m%d')
                    git_date = date_obj.strftime('%Y-%m-%d 12:00:00')
                except ValueError:
                    git_date = generate_random_date()
        
        if git_date is None:
            git_date = generate_random_date()
        
        print(f"处理文件: {file_path} (日期: {git_date})")
        
        try:
            subprocess.run(['git', 'add', file_path], check=True)
            
            env = os.environ.copy()
            env['GIT_AUTHOR_DATE'] = git_date
            env['GIT_COMMITTER_DATE'] = git_date

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
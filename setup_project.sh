#!/bin/bash

# Tạo thư mục dự án và vào đó
mkdir -p SelfEvolvingAI/data/logs
cd SelfEvolvingAI || exit

# Khởi tạo Git
git init
git branch -M main

# Tạo các file code cơ bản

# ai_core.py
cat > ai_core.py << 'EOF'
class SelfEvolvingAI:
    def __init__(self):
        self.version = "v1.0"
        self.knowledge = []

    def learn(self, data):
        self.knowledge.append(data)
        print(f"Đã học: {data}")

    def show_version(self):
        print(f"AI phiên bản: {self.version}")

    def upgrade(self):
        major, minor = self.version.strip('v').split('.')
        minor = int(minor) + 1
        self.version = f"v{major}.{minor}"
        print(f"Đã nâng cấp lên phiên bản {self.version}")

    def download_code_from_github(self, repo_url):
        print(f"Tải code mới nhất từ {repo_url}... (chưa triển khai)")
EOF

# updater.py
cat > updater.py << 'EOF'
def check_for_upgrade(ai):
    if len(ai.knowledge) >= 3:
        ai.upgrade()
        with open("data/logs/upgrade.log", "a") as f:
            f.write(f"AI nâng cấp lên {ai.version}\n")
        return True
    return False
EOF

# main.py
cat > main.py << 'EOF'
from ai_core import SelfEvolvingAI
from updater import check_for_upgrade
import time

def main():
    ai = SelfEvolvingAI()

    data_samples = ["dữ liệu ngày 1", "dữ liệu ngày 2", "dữ liệu ngày 3", "dữ liệu ngày 4"]

    for data in data_samples:
        ai.learn(data)
        upgraded = check_for_upgrade(ai)
        if upgraded:
            print("AI đã tự nâng cấp!")
        time.sleep(1)

    ai.show_version()

if __name__ == "__main__":
    main()
EOF

# requirements.txt (trống)
touch requirements.txt

# README.md
cat > README.md << 'EOF'
# SelfEvolvingAI

Dự án AI tự nâng cấp cơ bản.

## Cấu trúc thư mục

- main.py: Chương trình chính
- ai_core.py: Mã lõi AI
- updater.py: Kiểm tra và thực hiện nâng cấp
- data/: Dữ liệu học và logs

## Hướng dẫn chạy

1. Cài Python 3.x
2. Chạy: python main.py
EOF

# Tạo file dữ liệu mẫu
echo "sample,data,for,learning" > data/data.csv
touch data/logs/upgrade.log

# Thêm tất cả file vào Git và commit
git add .
git commit -m "Init SelfEvolvingAI project with basic AI code and structure"

# Thêm remote repo GitHub, nhớ đổi URL thành repo của bạn
git remote add origin https://github.com/trongpro300/SelfEvolvingAI.git

echo "Hoàn tất tạo dự án SelfEvolvingAI. Bạn có thể push lên GitHub với:"
echo "git push -u origin main"

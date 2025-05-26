from ai_core import SelfEvolvingAI
from updater import check_for_upgrade, learn_from_csv
import time

def main():
    ai = SelfEvolvingAI()

    # Học từ dữ liệu CSV
    learn_from_csv(ai, "data/data.csv")

    # Kiểm tra điều kiện nâng cấp và nâng cấp nếu đủ điều kiện
    data_samples = ["dữ liệu ngày 1", "dữ liệu ngày 2", "dữ liệu ngày 3", "dữ liệu ngày 4"]
    for data in data_samples:
        ai.learn(data)
        upgraded = check_for_upgrade(ai)
        if upgraded:
            print("AI đã tự nâng cấp!")
        time.sleep(1)

    # Hiển thị phiên bản sau khi nâng cấp
    ai.show_version()

    # Tải mã nguồn từ GitHub nếu cần
    ai.download_code_from_github('https://github.com/yourusername/yourrepo')

if __name__ == "__main__":
    main()

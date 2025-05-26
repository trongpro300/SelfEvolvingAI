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

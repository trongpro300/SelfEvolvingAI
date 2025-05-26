import os
from ai_core import SelfEvolvingAI

def check_for_upgrade(ai):
    if len(ai.knowledge) >= 3:
        ai.upgrade()
        with open("data/logs/upgrade.log", "a") as f:
            f.write(f"AI nâng cấp lên {ai.version}\n")
        return True
    return False

def learn_from_csv(ai, file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    for index, row in data.iterrows():
        ai.learn(row['data'])
    print(f"Học từ file CSV: {file_path}")

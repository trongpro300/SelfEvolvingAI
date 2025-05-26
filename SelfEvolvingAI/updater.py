def check_for_upgrade(ai):
    if len(ai.knowledge) >= 3:
        ai.upgrade()
        with open("data/logs/upgrade.log", "a") as f:
            f.write(f"AI nâng cấp lên {ai.version}\n")
        return True
    return False

import os
import requests

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

    def download_code_from_github(self, repo_url, branch='main'):
        # Tải mã nguồn từ GitHub
        print(f"Tải code từ {repo_url} branch {branch}")
        os.system(f"git clone -b {branch} {repo_url} temp_repo")
        os.system("cp -r temp_repo/* .")
        os.system("rm -rf temp_repo")
        print("Đã tải mã nguồn từ GitHub và cập nhật code!")

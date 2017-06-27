import json
import os


class Requirements:
    def __init__(self, data, config_id):
        self.deleted_files = data["settings"][config_id]["commit-requirements"]["deleted-files"]
        self.changed_files = data["settings"][config_id]["commit-requirements"]["changed-files"]
        self.new_files = data["settings"][config_id]["commit-requirements"]["new-files"]
        self.changed_lines = data["settings"][config_id]["commit-requirements"]["changed-lines"]


class Config:
    def __init__(self, config_id):
        self.load_data(config_id)

    def load_data(self, config_id):
        file_path = os.getcwd() + "\config.json"
        with open(file_path) as data_file:
            self.data = json.load(data_file)
            self.config_name = self.data["settings"][config_id]["config-name"]
            self.auto_commit = self.data["settings"][config_id]["auto-commit"]
            self.commit_message = self.data["settings"][config_id]["commit-message"]
            self.check_interval_seconds = self.data["settings"][config_id]["check-interval-seconds"]
            self.requirements = Requirements(self.data, config_id)

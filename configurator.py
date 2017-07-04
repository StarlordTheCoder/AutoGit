import json
import os

import math


class Requirements:
    """
    Limits der Konfiguration
    """

    def __init__(self, data, config_id):
            self.changed_files = int(data["settings"][config_id]["commit-requirements"]["changed-files"])
            self.untracked_files = int(data["settings"][config_id]["commit-requirements"]["untracked-files"])
            self.added_lines = int(data["settings"][config_id]["commit-requirements"]["added-lines"])
            self.removed_lines = int(data["settings"][config_id]["commit-requirements"]["removed-lines"])

            # Falls eine Limite negativ ist wird sie mit der Unendlichkeit ersetzt.
            # Dies erlaubt das ignorieren von gewissen Limits
            if self.changed_files < 0:
                self.changed_files = math.inf
            if self.untracked_files < 0:
                self.untracked_files = math.inf
            if self.added_lines < 0:
                self.added_lines = math.inf
            if self.removed_lines < 0:
                self.removed_lines = math.inf


class Config:
    """
    Gesamte Konfiguration
    """
    def __init__(self, config_id, data):
        self.load_data(config_id, data)

    def load_data(self, config_id, data):
        self.config_name = str(data["settings"][config_id]["config-name"])
        self.commit_message = str(data["settings"][config_id]["commit-message"])
        self.interval = int(data["settings"][config_id]["check-interval-seconds"])
        self.requirements = Requirements(data, config_id)


class ConfigManager:
    """
    Manager welcher das Laden von Konfigurationen erlaubt
    """

    def __init__(self):
        self.load_data()

    def get_config(self, config_id):
        return Config(config_id, self.data)

    def get_configs(self):
        """
        Lädt alle Konfigurationen
        """

        settings = self.data["settings"]
        for i in range(0, len(settings)):
            yield (i, settings[i]["config-name"])

    def load_data(self):
        file_path = os.getcwd()+"\config.json"
        with open(file_path) as data_file:
            self.data = json.load(data_file)

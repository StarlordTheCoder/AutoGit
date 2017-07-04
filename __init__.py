import os
from optparse import OptionParser

from configurator import ConfigManager
from main import Main

# Parser für Kommandozeilenargumente
parser = OptionParser()
parser.add_option("-r", "--repository",
                  dest="repository", help="GIT Repository to use", metavar="FOLDER")
parser.add_option("-c", "--config", dest="config",
                  help="Configuration ID to use")

(options, args) = parser.parse_args()

configuration = options.config
repository = options.repository

config_manager = ConfigManager()

# Keine Konfiguration angegeben => Zeige Auswahl
if not configuration:
    for i in config_manager.get_configs():
        print(str(i[0]) + ": " + i[1])

    configuration = input("Configuration: ")

# Kein Repository-Pfad angegeben => Nimm Working Directory
if not repository:
    repository = os.getcwd()

print("Config: " + configuration)
print("Repo: " + repository)

main = Main(config_manager, int(configuration), repository)
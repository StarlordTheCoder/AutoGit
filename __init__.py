import os
from optparse import OptionParser

from main import Main

parser = OptionParser()
parser.add_option("-r", "--repository",
                  dest="repository", help="GIT Repository to use")
parser.add_option("-c", "--config", dest="config",
                  help="Configuration ID to use", metavar="FILE")

(options, args) = parser.parse_args()

configuration = options.config
repository = options.repository

if not configuration:
    # TODO Print available configs
    configuration = input("Configuration: ")

if not repository:
    repository = os.getcwd()

print("Config: " + configuration)
print("Repo: " + repository)

main = Main(int(configuration), repository)
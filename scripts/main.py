import sys
from ia_config import IaConfig
from ia_manager import IaManager
import subprocess

def main() :
    PROJECT_NAME = 'IA Project'
    PROJECT_DESCRIPTION = 'This project purpose is to integrate IA with github, \
being able to generate commits based on the commit content.'
    print(
'''{} is running!
{}'''.format(str(PROJECT_NAME), str(PROJECT_DESCRIPTION))
    )

    config = IaConfig()
    client = IaManager(config)

    message = subprocess.check_output(["git", "show", "--name-only", sys.argv[0]])
    print("{}".format(message))
    #message = message.decode("utf-8")

    message = sys.argv[1]
    commit_hash = sys.argv[2]
    new_commit = client.chat(message)
    print("{}".format(commit_hash))
    a = subprocess.check_output(["git", "commit", "--amend", "-m", new_commit])

    print("{}".format(a))
main()
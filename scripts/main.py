import sys
from ia_config import IaConfig
from ia_manager import IaManager
import subprocess
import os

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


    message = sys.argv[1]
    commit_hash = sys.argv[2]

    rebase_command = ['git', 'rebase', '-i', commit_hash+'~1']
    subprocess.run(rebase_command, check=False)
    #message = message.decode("utf-8")
    rebase_message = subprocess.check_output(['git', 'log', '-n', '1', '--pretty=format:%s%n%n%b', commit_hash])
    commit_message = rebase_message.decode('utf-8').strip()
    
    new_commit = client.chat(message)

    todo_file = os.path.join(os.getcwd(), '.git/rebase-merge/git-rebase-todo')
    with open(todo_file, 'r+') as file:
        content = file.read()
        file.seek(0, 0)
        new_content = content.replace(f"pick {commit_hash} ", f"reword {commit_hash} ")
        file.write(new_content)
        file.truncate()

    with open('../.git/COMMIT_EDITMSG', 'r+') as file:
        content = file.read()
        file.seek(0, 0)
        new_content = content.replace(f"auto", f"{new_commit}")
        file.write(new_content)

    #subprocess.run(['git', 'commit', '--amend', '-m', new_commit], check=True)
main()
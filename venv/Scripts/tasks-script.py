#!D:\kyligence\kyligence_github\pytest_prac\bopytest-code\code\tasks_proj\venv\Scripts\python3.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'tasks==0.1.0','console_scripts','tasks'
__requires__ = 'tasks==0.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('tasks==0.1.0', 'console_scripts', 'tasks')()
    )

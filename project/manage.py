#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import threading,time
def a():
    for i in range(6):
        time.sleep(5)
        print('\n\n\n\n\n\n\nYO BOI KAAM KRTA HAI \n\n\n\n\n\n\n\n')

'''
thd=threading.Thread(target=a)
thd.daemon=True
thd.start()'''

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


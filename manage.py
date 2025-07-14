"""
🚀 Entry point for Django's command-line utility.
Used to manage the project via commands like runserver, migrate, etc.
"""

import os
import sys


# 🏁 Main entry function
def main():
    """Set up environment and run Django command-line utility."""

    # ⚙️ Set the default settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

    try:
        # 🚨 Attempt to import Django's CLI executor
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHON PATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # ▶️ Execute the command-line instruction
    execute_from_command_line(sys.argv)


# 🔓 Run main only if executed as script
if __name__ == '__main__':
    main()

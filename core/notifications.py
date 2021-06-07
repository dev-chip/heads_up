"""
Shows notifications via Windows 10 OS.
"""

__author__ = "James Cook"
__copyright__ = "Copyright (C) 2021 James Cook"
__license__ = "GNU General Public License v3"
__version__ = "1.0.0"
__maintainer__ = "James Cook"
__email__ = "contact@cookjames.uk"

from win10toast_click import ToastNotifier


def notify_win10(title, msg, app_icon_path=None):
    """
    Sends a windows 10 notification.

    Will freeze the program. Should be ran on a thread.
    """
    toaster = ToastNotifier()
    toaster.show_toast(title=title,
                       msg=msg,
                       duration=None,
                       icon_path=app_icon_path,
                       threaded=False,
                       callback_on_click=lambda: print(1+1))


if __name__ == "__main__":
    print("Running module manual test.")
    notify_win10(title="Hey! Take a break now!", msg="You should follow the 20-20-20 rule to keep your eyes healthy.")
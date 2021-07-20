#-------------------------------------------------------------------------------
# Classes for workers signal-slot mechanism
#-------------------------------------------------------------------------------

from PyQt5 import QtCore


class CommunicateSuccess(QtCore.QObject):
    myGUI_signal = QtCore.pyqtSignal([int, list, list, list])


class CommunicateError(QtCore.QObject):
    myGUI_signal = QtCore.pyqtSignal([Exception])


if __name__ == "__main__":
    print("Module test not implemented")
from modules.request import request
import modules.gui as gui
from modules.auth import get_auth
import modules.vars as horsy_vars
import threading
from PyQt5 import QtWidgets
from modules.http_status import handle


def change(email):
    UiLoginWindow = QtWidgets.QMainWindow()
    login_ui = gui.Ui_LoginWindow()
    login_ui.setupUi(UiLoginWindow)

    if email == "":
        gui.popup('Error', 'Please enter new email address')
        return

    auth = get_auth(True, login_ui, QtWidgets.QMainWindow())

    try:
        def change_in_new_thread():
            try:
                r_code = handle(request.put(horsy_vars.protocol + horsy_vars.server_url + '/users',
                                            json={'auth': auth, 'email': email}).status_code)
                gui.cpopup("Changing email", r_code[0])
            except:
                gui.cpopup('Error', 'Unexpected error.')

        threading.Thread(target=change_in_new_thread).start()
        gui.popup('Started', 'Check your email for confirmation')
    except:
        gui.popup('Error', 'Unexpected error.')

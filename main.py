import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QTableWidget
from PyQt5.QtCore import Qt
from qt import Ui_MainWindow
from db import Database


class PasswordCrypter(QMainWindow):
    def __init__(self):
        super(PasswordCrypter, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.window().setFixedSize(465, 257)

        self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.ui.pushButton_2.clicked.connect(
            lambda: self.add_password([self.ui.Soc_set_le.text(), self.ui.password_le.text(), self.ui.dop_le.text()],
                                      self.ui.crypt_password_le.text()))
        self.ui.GO_pb.clicked.connect(lambda: self.go(self.ui.crypt_password_le.text()))
        self.ui.actionAdd_new_note.triggered.connect(lambda: self.ui.tabWidget.setCurrentIndex(0))
        self.ui.actionRead.triggered.connect(lambda: self.ui.tabWidget.setCurrentIndex(1))
        self.ui.actionEnglish.triggered.connect(lambda: QMessageBox.information(self, "", 'info'))
        self.ui.action_3.triggered.connect(lambda: QMessageBox.information(self, "", 'информация'))

    def add_password(self, data: [], key: str):
        if key == '':
            return QMessageBox.information(self, "", "Для начала работы введите ваш ключ. Если вы пользуетесь программой "
                                              "первый раз, рекомендуем ознакомиться с инструкцией: Help -> "
                                              "How_it_works -> Your_language")
        if len(key) != 32:
            return QMessageBox.warning(self, "", "Ключ должен состоять из 32 символов!")
        if data[0] == '' or data[1] == '':
            return QMessageBox.warning(self, '', 'Поля "Соц. сеть" и "Пароль" не могут быть пустыми!')
        if db.write(data, key):
            self.ui.Soc_set_le.setText('')
            self.ui.password_le.setText('')
            self.ui.dop_le.setText('')
            self.set_table(key)
            return QMessageBox.information(self, "",
                                           f"Пароль от {data[0]} успешно добавлен. Вы можете посмотреть список ваших "
                                           f"паролей во вкладке \"Прочитать\"")
        else:
            return QMessageBox.critical(self, "", f"Возникла ошибка при добавлении пароля от {data[0]}. Пароль был добавлен, однако он не не сможет быть прочитан системой. Проверьте правильность ключа!")

    def set_table(self, key):
        row_count = 0
        decrypted_data = db.read(key)
        self.ui.tableWidget.clearContents()
        if not decrypted_data:
            return QMessageBox.information(self, '123', 'В базе нету данных. Самое время что-нибудь добавить!')
        for row in decrypted_data:
            row_count += 1
            self.ui.tableWidget.setRowCount(row_count)
            self.ui.tableWidget.setItem(row_count - 1, 0, QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(row_count - 1, 1, QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(row_count - 1, 2, QTableWidgetItem(row[2]))
        row_count = 0
        for row in decrypted_data:
            row_count += 1
            if '(!) Decryption_error (!)' in row:
                QMessageBox.warning(self, 'decription error',
                                    f'It seems like you have decryption error in row {row_count}. Go Help -> '
                                    f'How_it_works -> Your_language for more information.')
                break

    def go(self, key):
        if len(key) == 32:
            self.set_table(key)
        elif key == '':
            QMessageBox.information(self, "", "Для начала работы введите ваш ключ. Если вы пользуетесь программой "
                                              "первый раз, рекомендуем ознакомиться с инструкцией: Help -> "
                                              "How_it_works -> Your_language")
        else:
            QMessageBox.warning(self, "", "Ключ должен состоять из 32 символов!")

    def show_question_box(self):
        selected_items = self.ui.tableWidget.selectedItems()
        row = selected_items[0].row()
        data = [self.ui.tableWidget.item(row, col).text() for col in range(self.ui.tableWidget.columnCount())]
        reply = QMessageBox.question(self, 'Вопрос', f'Вы уверены, что удалить пароль от {data[0]}?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:

            db.delete(data, self.ui.crypt_password_le.text())
            self.ui.tableWidget.removeRow(row)
        else:
            print('Действие отменено')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Backspace:
            PasswordCrypter.show_question_box(self)
        if event.key() == Qt.Key_Enter:
            PasswordCrypter.go(self, self.ui.crypt_password_le.text())


if __name__ == '__main__':
    db = Database('db.db')
    app = QApplication(sys.argv)
    window = PasswordCrypter()
    window.show()

    sys.exit(app.exec())

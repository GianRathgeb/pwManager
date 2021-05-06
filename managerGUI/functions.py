from managerModules import *

def showPasswords(self):
        data = [
            [4, 9, 2],
            [1, 0, 0],
            [3, 5, 0],
            [3, 3, 2],
            [7, 8, 9],
        ]


        self.model = TableModel(data)
        self.ui.table_view_your_passwords.setModel(self.model)
        self.ui.table_view_your_passwords.horizontalHeader().setStretchLastSection(True) 
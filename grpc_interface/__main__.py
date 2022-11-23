#!/usr/bin/env python3

import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class Interface:
    def __init__(self):
        self.running = False
        # You need one (and only one) QApplication instance per application.
        # Pass in sys.argv to allow command line arguments for your app.
        # If you know you won't use command line arguments QApplication([]) works too.
        self.app = QApplication(list())
        # Create a Qt widget, which will be our window.
        self.window = QPushButton("PushButton")
        self.window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    def runAdmin(self):
        # self.label = ctk.CTkLabel(
        #     master=self.frame, text="Admin Interface", text_font=("monospace, 48"))
        # self.label.pack(pady=36, padx=30)
        return 0

    def displayMainMenu(self):
        # run_button = ctk.Button(
        #     master=self.frame, text="Run", command=runAdmin)
        # run_button.pack(pady=36, padx=30)
        # import_button = ctk.Button(
        #     master=self.frame, text="Import", command=importBotnet)
        # import_button.pack(pady=36, padx=30)
        # export_button = ctk.Button(
        #     master=self.frame, text="Export", command=exportBotnet)
        # export_button.pack(pady=36, padx=30)
        return 0

    def mainMenu(self):
        # self.label = ctk.CTkLabel(
        #     master=self.frame, text="Main Menu", text_font=("monospace, 48"))
        # self.label.pack(pady=36, padx=30)
        # if self.running:
        #     displayAdmin()
        # else:
        #     displayMainMenu()
        return 0

    def runme(self):
        if not self.running:
            self.app.exec()
        return 0


def main():
    interface = Interface()
    interface.runme()
    return 0


if __name__ == '__main__':
    sys.exit(main())

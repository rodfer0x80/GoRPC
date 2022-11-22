#!/usr/bin/env python3

import sys

import customtinker as ctk


class Interface:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_theme_color("dark-blue")
        self.root = ctk.CTk()
        root.geometry = ("1440x900")

    def runme(self):
        frame = ctk.CTkFrame(master=root)
        frame.pack(pady=50, padx=150, fill="both", expand=True)



def main():
    interface = Interface()
    Interface.runme()
    return 0


if __name__ == '__main__':
    sys.exit(main())


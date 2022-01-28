import webbrowser
import os

webbrowser.open(os.path.abspath(f'html/p{input("Problem Number? ").zfill(3)}.html'))

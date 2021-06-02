from appJar import gui
import os
import time
import subprocess
import sys


class Application:
    def __init__(self):
        self.app = gui(useTtk=True)
        self.terrablock_path = '/volumes/terrablock/'

    def network_connection(self):
        if os.path.exists(self.terrablock_path):
            return True
        else:
            return False

    def path_exists(self, path):
        if os.path.exists(path):
            try:
                subprocess.call(['open', '-R', path])
            except Exception as error:
                self.app.errorBox('Error', f'{error}')
        else:
            self.app.errorBox("Error", "File might not exist!")

    def convert_path(self, path):
        char_replace = {
            't:\\': '/volumes/terrablock/',
            '\\': '/',
            '/volumes/terrablock/': '/volumes/terrablock/'
        }

        if not path:
            self.app.warningBox('Error', 'Path field is empty!')
            return None

        elif list(char_replace.keys())[0] in path:
            path = path[path.index('t:'):]
            #path = path.split(' ')[0]

            for k, v in char_replace.items():
                if k in path:
                    path = path.replace(k, char_replace.get(k))
            self.path_exists(path)

        elif list(char_replace.keys())[2] in path:
            path = path[path.index('/volumes/terrablock/'):]
            #path = path.split(' ')[0]
            self.path_exists(path)
        else:
            self.app.warningBox('Error', 'Your Windows Path is wrong, it should be start from T:\\ or /volumes/terrablock')

    def prepare(self, app):
        app.setTitle('XPath 2020 / Milo Postproduction')
        app.setSize('550x110')
        app.setResizable(canResize=False)
        app.setLocation('CENTER')
        app.setFont(size=14, family='Helvetica')
        app.setButtonFont(size=11, family='Helvetica')
        app.setTtkTheme('arc')

        app.startLabelFrame('  Input Windows / MacOsX Network Path  ')

        app.setPadding([20, 0])
        app.stretch = 'both'
        app.sticky = "ew"

        app.addEntry('check_validity', 0, 1, 3)
        app.setFocus('check_validity')

        app.addButtons(['   Show In Finder   '], self.submit, 1, 2)
        app.addButtons(['Paste From Clipboard'], self.paste, 1, 1)
        app.enableEnter(self.submit)
        app.stopLabelFrame()

        if not self.network_connection():
            app.errorBox("Error", "You don't have access to Terrablock!\nCheck connection!")
            sys.exit(0)
    
        return app

    def start(self):
        self.app = self.prepare(self.app)
        self.app.go()

    def paste(self, btnName):
        if btnName == 'Paste From Clipboard':
            paste = self.app.topLevel.clipboard_get()
            self.app.setEntry('check_validity', paste)

    def submit(self, btnName):
        if btnName == '   Show In Finder   ':
            path = self.app.getEntry('check_validity').lower().strip()
            self.convert_path(path)


if __name__ == '__main__':
    app = Application()
    app.start()

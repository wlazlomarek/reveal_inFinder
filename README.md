# xPath
Simple Mac App allows to reveal windows and mac network file path in finder.

Building app by pyinstaller:
```console
$ pyinstaller --windowed --icon icon_path --name ProjectCreator myapp.py 
$ cd dist/myapp.app/Contents/MacOs
$ mkdir tcl tk
$ cp -R /Library/Frameworks/Python.framework/Versions/3.7/lib/tcl* tcl/
$ cp -R /Library/Frameworks/Python.framework/Versions/3.7/lib/tk* tk/
$ cp -R /Library/Frameworks/Python.framework/Versions/3.7/lib/Tk* tk/ 

or 

$ pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' your_script.py
```

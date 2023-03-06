from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser


#messagebox.showwarning('Titulek', 'Sory Eroor!')

#odpoved = messagebox.askyesnocancel('Titulek', 'Otáka... ?')

print(colorchooser.askcolor())

odpoved = filedialog.asksaveasfilename()
print(odpoved)


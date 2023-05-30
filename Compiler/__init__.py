from Compiler_main import*
import os 
from tkinter.filedialog import*

n=askopenfilename(filetypes=[('TBANYTHON Files','*.tby')])
with open(n,'r') as nn:
    app=nn.read()
    dupe=TBANYTHONCompiler()
    derpax=dupe.compile(app)
    x=asksaveasfilename(filetypes=[('Python Data','*.py')])
    with open(x,'w') as data:
        data.write(derpax)
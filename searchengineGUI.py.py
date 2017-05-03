from Tkinter import *
import webbrowser
import mechanize
from PIL import ImageTk
from bs4 import BeautifulSoup
root = Tk()

options = ["10","20","30"]

var = StringVar(root)
var.set('10')

def browser():
    word = Search.get()
    url = 'https://www.google.com/#q={}'.format(word)
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    webbrowser.get(chrome_path)
    webbrowser.open_new_tab(url)

def clear_search():#Reset the search field
    Search.delete(0,END)
    Result.delete("1.0",END)
    var.set('10')

def fun(self=0):
    new = Search.get()
    url = "https://duckduckgo.com/"
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open(url)
    br.select_form(name="x")
    br["q"] = str(new)
    res = br.submit()
    content = res.read()
    soup = BeautifulSoup(content,"html.parser")
    mylink = soup.find_all('a')
    v = 1
    b = var.get()
    
    for i in mylink:
        try:
             
             if v <= int(b):
                
                if i.attrs['class'][0] == "result__a":
                    Result.insert(END,v)
                    Result.insert(END,i.text)
                    Result.insert(END,'\n')
                elif i.attrs['class'][0] == "result__snippet":
                    Result.insert(END,i.text)
                    Result.insert(END,'\n')
                    Result.insert(END,i.attrs['href'])
                    Result.insert(END,'\n ')
                    Result.insert(END,'--------------------------------------------------------------------')
                    v = v + 1
        except KeyError:
            pass
            
            
    with open("result1.xls", "w") as f:
        f.write(content)
      
Value = Label(root,text="Search", font="-weight bold")
Value.grid(row=0,column=0,sticky="W")

Search = Entry(root,width=50)
Search.grid(row=0,column=1)

Go = Button(root,text="GO",width=5,command=fun)
Go.bind("<Key>",fun)
Go.grid(row=0,column=2,sticky="W")

Dropdownlist = OptionMenu(root,var,*options)
Dropdownlist.grid(row=0,column=4,padx=5,sticky="W")

Reset = Button(root,text="RESET",width=5,command=clear_search)
Reset.grid(row=0,column=5,padx=5,sticky="W")

bro = Button(root,command=browser)
photo = ImageTk.PhotoImage(file="mew1.png")
bro.config(image=photo)
bro.image = photo
bro.grid(row=0,column=6,sticky="W")

Result = Text(root,height=20,width=69)
Result.grid(rowspan=10,columnspan=40,sticky='W',padx=5)
Scroll = Scrollbar(root,command=Result.yview)
Scroll.grid(row=1,column=6,padx=18,ipady=135)
Result.config(yscrollcommand=Scroll.set)

root.mainloop()



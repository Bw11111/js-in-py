class js:
  global surpressedDialog
  surpressedDialog = False
  class superGlobals:
    def surpress():
        global surpressedDialog
        surpressedDialog = True

  class config:
    def openSiteOnProgramStart(string, url):
      if string == "True":
        import webbrowser
        webbrowser.open(url)
      else:
        print("nope")
    
  class window:
    import tkinter as tk
    from tkinter import ttk
    import webbrowser
    def alert(string, string2):
      if surpressedDialog == False:
        
        import tkinter as tk
        windows = tk.Tk()
        windows.title(string2)
        tk.Label(text="                 " + string + "                 ").pack()
        def closerJsLib():
          windows.destroy()
  
        
        tk.Button(text="Ok", command=closerJsLib).pack()
        tk.Button(text="Surpress Dialogs", command=js.superGlobals.surpress).pack()
        #def getInputJsLib():
       
   
        tk.mainloop()
      else:
        print("surpressed")
    def open(url):
      import webbrowser
      webbrowser.open(url)
  #class test:
    #print("hi")
#js.window.alert("Hi", "Hi")
#js.window.alert("Hi", "Hi")
#js.window.open("https://www.google.com")
#js.config.openSiteOnProgramStart("True", "https://www.google.com")

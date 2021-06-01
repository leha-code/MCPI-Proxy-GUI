#from proxy.proxy import *
from tkinter import *
import tkinter.messagebox as msgbox
from threading import *

'''
# Proxy
proxy_lock = threading.Lock()
proxy_thread: threading.Thread = None
proxy = Proxy()

def update_proxy():
    global proxy, proxy_thread, proxy_lock, current_ip, current_port
    proxy_lock.acquire()
    if proxy_thread is not None:
        proxy.stop()
        proxy_thread.join()
    try:
        proxy.set_option("src_addr", current_ip.get())
        proxy.set_option("src_port", int(current_port.get()))
        proxy_thread = threading.Thread(target=lambda *args: proxy.run())
        proxy_thread.start()
    except ValueError:
        # Invalid Port
        pass
    proxy_lock.release()
    '''


class ProxyGUI(Tk):
    def __init__(self, *args):
        super().__init__()
        self.title("GUI Proxy")
        self.geometry("400x200")
        #self.resizable(False, True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=3)

        self.title_label = Label(self, text="GUI Proxy")
        self.title_label.config(font=('', 30))
        self.title_label.place(x=100, y=0)

        self.ip_label = Label(self, text="IP: ")
        self.ip_label.place(x=50, y=50)
        self.current_ip = StringVar(self)
        self.ip = Entry(self, width=35, textvariable=self.current_ip)
        self.ip.place(x=70, y=50)

        self.port_label = Label(self, text="Port: ")
        self.port_label.place(x=35, y=100)
        self.current_port = StringVar(self)
        self.port = Entry(self, width=35, textvariable=self.current_port)
        self.port.place(x=70, y=100)
        
        self.start_button = Button(self, text="Start!")

        

        
        


if __name__ == "__main__":
    app = ProxyGUI()
    app.mainloop()
    
    

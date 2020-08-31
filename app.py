import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title = "Options Trader"
        self.root.geometry("300x300")

        self.ticker = ''
        self.entry_ticker = tk.StringVar()

        tk.Label(self.root, text="Symbol").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.entry_ticker).grid(row=0, column=1)
        ticker_search = tk.Button(self.root, text="Search")
        ticker_search.grid(row=0, column=2)
        ticker_search.bind('<Button-1>', self.update_ticker)

    def update_ticker(self, event=None):
        print(self.entry_ticker.get())

    def mainloop(self):
        self.root.mainloop()
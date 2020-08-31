import os
import tkinter as tk
import options_data as od

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Options Trader")
        self.root.geometry("300x300")
        self.root.iconphoto(False, tk.PhotoImage(file=os.getcwd() + '/img/icon.png'))

        self.ticker = ''
        self.entry_ticker = tk.StringVar()

        tk.Label(self.root, text="Symbol:", width=8, anchor='e').grid(row=0, column=0)
        tk.Entry(self.root, width=20, textvariable=self.entry_ticker).grid(row=0, column=1)
        ticker_search = tk.Button(self.root, width=8, text="Search")
        ticker_search.grid(row=0, column=2)
        ticker_search.bind('<Button-1>', self.update_ticker)

        tk.Label(self.root, text="Maturity:", width=8, anchor='e').grid(row=1, column=0)

        self.maturity = tk.StringVar()
        self.maturities = tk.OptionMenu(self.root, self.maturity, [])
        self.maturities.config(width=20)
        self.maturities.grid(row=1, column=1)

    def update_ticker(self, event=None):
        ticker = self.entry_ticker.get()
        
        if od.validate_ticker(ticker):
            self.ticker = ticker

            menu = self.maturities['menu']
            menu.delete(0, 'end')

            new_mats = od.get_maturities(ticker)
            for date, value in new_mats:
                menu.add_command(label=date, command=tk._setit(self.maturity, date))
            
            first_mat = new_mats[0][0]
            self.maturity.set(first_mat)
        else:
            # Label error
            pass

    def mainloop(self):
        self.root.mainloop()
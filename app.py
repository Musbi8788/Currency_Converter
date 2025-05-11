# Import Statement
import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
import os

# API
API_KEY = os.environ.get("Currency_API_KEY")
FONT = "Arial", 12
BG = 'lightblue'

def exchange_rate():
    """send a requests to the api and get api data"""
    URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    response = requests.get(URL)
    if response.status_code == 200:
        result = response.json()
        currency_code = result['conversion_rates']
        return currency_code
    
    else:
        messagebox.showerror("Your Free Api is finish.")
        return None
    
# currency code list
exchange_data = exchange_rate()

if exchange_rate is None:
    messagebox.showerror("Error", "Could not fetch exchange rates.")
    win.destroy()

if exchange_data is not None:
    currencies = list(exchange_data.keys())
else:
    currencies = []
print(currencies)

def currency_converter():
    """
        Get the following stuff from the user:
        From Currrency Code  = country code
        To Currency Code = country code
        Amount = int
        convert amount to flaot value and divid the to_currency with from_currency and multiply it by the amount. 
    """
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror(title="Error", message=f"Invalid amount.")
        return

    from_curr_code = from_entry.get()
    to_curr_code = to_curr_entry.get()

    if from_curr_code not in currencies or to_curr_code not in currencies: 
        messagebox.showerror("Error currency code not selected.")
        return
    
    # check if exchange data is none before converting the currency.
    if exchange_data is None:
        messagebox.showerror("Error", "Exchange rate is not avaible.")
        return 
    

    converted_amount = amount * (exchange_data[to_curr_code] / exchange_data[from_curr_code]) 

    # update the converted result and display to the user
    converted_result.config(text=f"Converted Amount: {converted_amount:.2f} {to_curr_code}")
    print(converted_result)


# -------------------------- UI -----------------------------
win = tk.Tk()
win.title("Currency Converter")
win_width = 300
win_height = 200
win.configure(bg="lightblue")
win.geometry(f"{win_width}x{win_height}")
win.resizable(False, False)
# center window

# Show the app title
heading = tk.Label(win, text="Musbi's Currency Converter", font=("Arial", 13, "bold"), fg='green', bg=BG)
heading.grid(row=0, column=1 , columnspan=3)

# from currency 
from_curr = tk.Label(win, text="From:", font=("Arial",13, 'bold'), fg='blue', bg=BG)
from_curr.grid(row=2, column=1 )

# from currency list
from_entry = ttk.Combobox(win, values=currencies)
from_entry.set("Select Currency") # Set a default value
from_entry.grid(row=2, column=2, columnspan=2)

# to Currency 
to_curr = tk.Label(win, text="To:", font=("Arial",13, 'bold'), fg='blue',bg=BG)
to_curr.grid(row=3, column=1)

# To currency list
to_curr_entry = ttk.Combobox(win, values=currencies)
to_curr_entry.set("Select Currency") # Set a default value
to_curr_entry.grid(row=3, column=2, columnspan=2)

# amount of money
c_amount = tk.Label(win, text="Amount:", font=("Arial",13, 'bold'), fg='blue', bg=BG)
c_amount.grid(row=4, column=1)

# amount entry
amount_entry = tk.Entry(win, font=(FONT), width=15,)
amount_entry.grid(row=4, column=2, columnspan=2)

# converter button
converter_btn = tk.Button(win, text="Convert Now.",font=("Arial", 12, 'bold'), bg='green', fg='white', command=currency_converter)
converter_btn.grid(row=6, column=2, columnspan=3)

# set an empty label for converted result
converted_result = tk.Label(win, text="",font=("Arial", 12, 'bold'), bg=BG)
converted_result.grid(row=8, column=1, columnspan=3)

# keep opening
if __name__ == "__main__":
    win.mainloop()








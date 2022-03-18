# Importeren van package Pandas
//w3 schools voor panda
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename

def open_exel_file():
    filepath = askopenfilename(
        filetypes=[("Excel", "*.xlsx"), ("All Files", "*.*")]
    )
    if not filepath:
        return  
    # Open van het Excel bestand wat gekozen is
    df = pd.read_excel(filepath)
    # Verkrijgen van aantal rijen en kolommen
    n_rows, n_columns = get_number_rows_columns(df)
    # Verkrijgen van de maximale waarde
    max_value = get_highest_value(df)
    # Updaten van de labels
    update_labels(n_rows, n_columns, max_value)

# Hulpfunctie voor het verkrijgen van het aantal rijen en kolommen
def get_number_rows_columns(df):
    shape = df.shape
    n_rows = shape[0]
    n_columns = shape[1]
    return n_rows, n_columns
    
# Hulpfunctie voor het verkrijgen van de maximale waarde
def get_highest_value(df):
    max_value = df.max().max()
    return max_value

# Hulpfunctie om de labels te updaten
def update_labels(n_rows, n_columns, max_value):
    label_rows["text"] = f"Number of rows: {n_rows}"
    label_columns["text"] = f"Number of columns: {n_columns}"
    label_max["text"] = f"Highest value: {max_value}"
    
window = tk.Tk()
window.title("Excel")

window.columnconfigure([0], minsize=20)
window.rowconfigure([0, 1, 2, 3], minsize=20)

label_rows = tk.Label(text="Number of rows:")
label_columns = tk.Label(text="Number of columns:")
label_max = tk.Label(text="Highest value:")
button_open = tk.Button(text='Open Excel file', width=20, command=open_exel_file)

label_rows.grid(row=0, column=0, sticky="w", padx=5, pady=5)
label_columns.grid(row=1, column=0, sticky="w", padx=5, pady=5)
label_max.grid(row=2, column=0, sticky="w", padx=5, pady=5)
button_open.grid(row=3, column=0, padx=5, pady=5)

window.mainloop()
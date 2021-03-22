import tkinter as tk
# Importeren van de methode om een bestand te openen
from tkinter.filedialog import askopenfilename

# De functie die aangeroepen wordt om een bestand te openen
def open_exel_file():
    filepath = askopenfilename(
        filetypes=[("Excel", "*.xlsx"), ("All Files", "*.*")]
    )
    if not filepath:
        return   

window = tk.Tk()
window.title("Excel")

window.columnconfigure([0], minsize=20)
window.rowconfigure([0, 1, 2, 3], minsize=20)

label_rows = tk.Label(text="Number of rows:")
label_columns = tk.Label(text="Number of columns:")
label_max = tk.Label(text="Highest value:")
# Toevoegen van 'command=open_exel_file' waarmee de een functie wordt aangeroepen
button_open = tk.Button(text='Open Excel bestand', width=20, command=open_exel_file)

label_rows.grid(row=0, column=0, sticky="w", padx=5, pady=5)
label_columns.grid(row=1, column=0, sticky="w", padx=5, pady=5)
label_max.grid(row=2, column=0, sticky="w", padx=5, pady=5)
button_open.grid(row=3, column=0, padx=5, pady=5)

window.mainloop()
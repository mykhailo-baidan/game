import tkinter as tk

def check_text():
    input_text = text_entry.get()
    if input_text.lower() == "ahoj":
        response_label.config(text="Ahoj!")
        # Nastavení zpoždění pro změnu textu zpět na prázdný řetězec po 2000 ms (2 sekundy)
        root.after(2000, clear_response_label)
        # Schovat tlačítko po stisknutí
        submit_button.pack_forget()
    else:
        response_label.config(text="Nerozumím, zkuste to znovu.")

def clear_response_label():
    response_label.config(text="")
    # Znovu zobrazit tlačítko po smazání textu
    submit_button.pack()

# Vytvoření okna
root = tk.Tk()
root.title("Ahoj")

# Vytvoření pole pro psaní textu
text_entry = tk.Entry(root, width=30)
text_entry.pack(pady=10)

# Tlačítko pro odeslání textu
submit_button = tk.Button(root, text="Odeslat", command=check_text)
submit_button.pack()

# Label pro odpověď
response_label = tk.Label(root, text="")
response_label.pack(pady=10)

# Spuštění hlavní smyčky
root.mainloop()

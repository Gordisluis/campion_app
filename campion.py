import random
import tkinter as tk

def get_quote():
    quotes = [
        "otra mas para mi cuadro de copas.",
        "no puedo se me cae el WIFI en el juego.",
        "Me tienes harto PIÑA!.",
        "Se humilde deja de celebrar goles.",
        "lagero, sepa ganar!.",
        "Anno DOMINI!!!.",
    ]
    return random.choice(quotes)

def show_quote():
    quote_label.config(text=get_quote())

# Create the main window
window = tk.Tk()
window.title("Campion App")

# Create a label for displaying the quote
quote_label = tk.Label(window, text="")
quote_label.pack()

# Create a button to show a new quote
button = tk.Button(window, text="Anno Domini!", command=show_quote)
button.pack()

# Run the main event loop
window.mainloop()
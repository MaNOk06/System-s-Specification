# Natural Language → Symbolic Logic Translator
# Supports: AND, OR, IF...THEN, & NOT
import tkinter as tk
from tkinter import ttk


symbol_table = {}          # Maps the propositions with their corresponding variable letters
symbol_counter = 0         # Next unused letter index (p, q, r, ...)

#Removes excess spaces around and in the text
def normalize(text):
    text = text.lower().strip()
    while "  " in text:
        text = text.replace("  ", " ")
    return text


def assign_symbol(proposition):
    """
    Assigns a letter to each unique atomic proposition.
    Returns the symbol letter.
    """
    global symbol_counter

    #Checks if the proposition is already stored in the dictionary
    if proposition not in symbol_table:
        #Makes the variable letters start from p onwards
        symbol_table[proposition] = chr(ord('p') + symbol_counter)
        symbol_counter += 1

    return symbol_table[proposition]


def contains_embedded_not(sentence):
    return " not " in sentence


# Recursive translator
def translate(sentence):
    sentence = normalize(sentence)
    
    # IF ... THEN (supports comma form too)
    if "if" in sentence and ("then" in sentence or "," in sentence):

        if "then" in sentence:
            before_then = sentence.split("then", 1)[0]
            antecedent_text = before_then.split("if", 1)[1].strip()
            consequent_text = sentence.split("then", 1)[1].strip()

        else:  # using comma syntax
            before_comma = sentence.split(",", 1)[0]
            antecedent_text = before_comma.split("if", 1)[1].strip()
            consequent_text = sentence.split(",", 1)[1].strip()

        left = translate(antecedent_text)
        right = translate(consequent_text)

        return f"({left} → {right})"

    # logic for detecting and handling conjunctions (AND) in the sentence
    if " and " in sentence:
        parts = [p.strip() for p in sentence.split(" and ")]
        translated = [translate(p) for p in parts]
        return "(" + " ∧ ".join(translated) + ")"

    # logic for detecting and handling disjunctions (OR) in the sentence
    if " or " in sentence:
        parts = [p.strip() for p in sentence.split(" or ")]
        translated = [translate(p) for p in parts]
        return "(" + " ∨ ".join(translated) + ")"

    # logic for detecting and handling negation (NOT) in the sentence
    if contains_embedded_not(sentence):
        positive_form = sentence.replace(" not ", " ", 1)
        symbol = assign_symbol(positive_form)
        return f"¬{symbol}"

    # Atomic proposition lacks a connective so it goes straight into the dictionnary
    return assign_symbol(sentence)



# Tkinter GUI Code

def update_legend():
    """Handling logic for refreshing the legend panel."""
    legend_text.delete("1.0", tk.END)
    if not symbol_table:
        legend_text.insert(tk.END, "(No symbols assigned yet)")
        return
    for proposition, symbol in symbol_table.items():
        legend_text.insert(tk.END, f"{symbol} : {proposition}\n")


def perform_translation():
    """ Handling logic for when the Translate button is clicked."""
    text = input_field.get("1.0", tk.END).strip()
    if text:
        output = translate(text)
        output_field.delete("1.0", tk.END)
        output_field.insert(tk.END, output)
        update_legend()


def clear_all():
    """Handling logic to clear input, output, and symbol table."""
    global symbol_table, symbol_counter
    input_field.delete("1.0", tk.END)
    output_field.delete("1.0", tk.END)
    symbol_table = {}
    symbol_counter = 0
    update_legend()


# Root window
root = tk.Tk()
root.title("Systems Specifications App")
root.geometry("650x500")


# Input section taking in the sentence to be translated

ttk.Label(root, text="Enter your statement:").pack(pady=5)

input_field = tk.Text(root, width=70, height = 4, wrap = "word")
input_field.pack(pady=5)

translate_button = ttk.Button(root, text="Translate", command=perform_translation)
translate_button.pack(pady=5)


# 
# Output section showing the symbolic form of the sentence

ttk.Label(root, text="Symbolic Form:").pack(pady=5)

output_field = tk.Text(root, width=70, height=4, wrap="word")
output_field.pack(pady=5)


# Legend Section of the GUI displaying what propositions correspond to each variable letter

ttk.Label(root, text="Legend (What each variable represents:").pack(pady=5)

legend_text = tk.Text(root, width=70, height=10, wrap="word")
legend_text.pack(pady=5)
legend_text.insert(tk.END, "(No symbols assigned yet)")


# Clear Button
clear_button = ttk.Button(root, text="Clear All", command=clear_all)
clear_button.pack(pady=10)


# Start the GUI loop
root.mainloop()
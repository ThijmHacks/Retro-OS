import tkinter as tk

def product_key(P):
    raw_input = P.replace("-", "")

    if raw_input.isdigit() or raw_input == "":
        if len(raw_input) > 16:
            return False

        formatted_input = ""
        for i in range(0, len(raw_input), 4):
            formatted_input += raw_input[i:i + 4] + "-"

        formatted_input = formatted_input.rstrip('-')

        return formatted_input
    return False
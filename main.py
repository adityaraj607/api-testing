import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("API Testing")
root.geometry("1000x700")
root.minsize(800, 550)

request_frame = ttk.Frame(root, padding=12)
request_frame.pack(fill="x")

method_var = tk.StringVar(value="GET")
url_var = tk.StringVar()

method_dropdown = ttk.Combobox(
    request_frame,
    textvariable=method_var,
    values=["GET", "POST"],
    state="readonly",
    width=10
)
method_dropdown.pack(side="left", padx=(0, 8))

url_entry = ttk.Entry(request_frame, textvariable=url_var)
url_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))

send_button = ttk.Button(request_frame, text="Send")
send_button.pack(side="left")

status_label = ttk.Label(root, text="Ready")
status_label.pack(anchor="w", padx=12)


root.mainloop()
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

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=12, pady=12)

params_tab = ttk.Frame(notebook, padding=10)
headers_tab = ttk.Frame(notebook, padding=10)
body_tab = ttk.Frame(notebook, padding=10)
auth_tab = ttk.Frame(notebook, padding=10)

notebook.add(params_tab, text="Params")
notebook.add(headers_tab, text="Headers")
notebook.add(body_tab, text="Body")
notebook.add(auth_tab, text="Auth")

ttk.Label(params_tab, text="Query Parameters").pack(anchor="w")
ttk.Label(headers_tab, text="Request Headers").pack(anchor="w")
ttk.Label(body_tab, text="Request Body").pack(anchor="w")
ttk.Label(auth_tab, text="Authentication").pack(anchor="w")

root.mainloop()
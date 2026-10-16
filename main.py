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




def create_key_value_table(parent, title):
    frame = ttk.Frame(parent)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text=title).pack(anchor="w", pady=(0, 8))

    table = ttk.Frame(frame)
    table.pack(fill="x")

    ttk.Label(table, text="Key").grid(row=0, column=0, sticky="w")
    ttk.Label(table, text="Value").grid(row=0, column=1, sticky="w")

    table.columnconfigure(0, weight=1)
    table.columnconfigure(1, weight=2)

    rows = []

    def add_row():
        row = len(rows) + 1

        key = ttk.Entry(table)
        value = ttk.Entry(table)

        key.grid(row=row, column=0, sticky="ew", padx=(0, 8), pady=4)
        value.grid(row=row, column=1, sticky="ew", pady=4)

        rows.append((key, value))

    def get_data():
        return {
            key.get().strip(): value.get()
            for key, value in rows
            if key.get().strip()
        }

    ttk.Button(frame, text="Add Row", command=add_row).pack(
        anchor="w", pady=8
    )

    add_row()
    return get_data

get_params = create_key_value_table(params_tab, "Query Parameters")
get_headers = create_key_value_table(headers_tab, "Request Headers")
ttk.Label(body_tab, text="Request Body").pack(anchor="w")
ttk.Label(auth_tab, text="Authentication").pack(anchor="w")

root.mainloop()
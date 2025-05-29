import tkinter as tk

root = tk.Tk()
root.title("Simple Text Editor")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)

text_area = tk.Text(root, width=50, height=20)
text_area.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(root, orient="vertical", command=text_area.yview)
scrollbar.pack(side="right", fill="y")

text_area.config(yscrollcommand=scrollbar.set)

root.mainloop()

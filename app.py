import tkinter as tk
import pymongo

# Connet to mongoDb
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["PythonChat"]
messages_col = db["messages"]

# GUI 
root = tk.Tk()
root.title("PythonChat")
root.geometry("500x300")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

send_button = tk.Button(root, text="Send")
send_button.pack(pady=5)

root.mainloop()

# git statuts (optional)
# git add .
# git commit -m "Add new code for mongo"
# git push


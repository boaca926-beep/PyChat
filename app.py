import tkinter as tk
import pymongo

# Connet to mongoDb
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["PythonChat"]
messages_col = db["messages"]

# GUI 
root = tk.Tk()
root.title("PythonChat")
root.geometry("1000x700")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

def send_message():
    if entry.get():
        messages_col.insert_one({"text": entry.get()})
        entry.delete(0, tk.END) # delete from first position to the end


    return


send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)


message_label = tk.Label(root, text="Message: ", justify="left")
message_label.pack()

def fetch_message():
    messages = messages_col.find().sort("_id")
    message_label.config(text="messages:\n" + "\n".join(f"- {m['text']}" for m in messages))
    root.after(1000, fetch_message) #every 2 seonds: 2000

fetch_message()
root.mainloop()

# git statuts (optional)
# git add .
# git commit -m "Add new code for mongo"
# git push


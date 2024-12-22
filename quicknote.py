import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

class QuickNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note App")
        self.root.geometry("400x300")
        self.root.attributes('-topmost', True)

        # default Values
        self.default_json = "notes.json"
        self.default_creator = "local"

        # JSON-Dateipfad
        self.json_file = None
        self.default_tags = ["Private", "Work", "Server", "utils"]
        self.check_for_json()

        # Themes
        self.dark_mode = {
            "bg_color": "#2E2E2E", "fg_color": "#FFFFFF",
            "entry_bg": "#424242", "button_bg": "#555555", "button_fg": "#FFFFFF"
        }
        self.light_mode = {
            "bg_color": "#F0F0F0", "fg_color": "#000000",
            "entry_bg": "#FFFFFF", "button_bg": "#E0E0E0", "button_fg": "#000000"
        }
        self.current_theme = "dark"
        self.apply_theme()

        # Widgets
        self.create_widgets()

    def check_for_json(self):
        if not os.path.exists(self.default_json):
            self.prompt_for_json()
        else:
            self.json_file = self.default_json

    def prompt_for_json(self):
        popup = tk.Toplevel()
        popup.title("Default setup")
        popup.geometry("300x200")
        popup.attributes('-topmost', True)

        tk.Label(popup, text="Filename:").pack(pady=5)
        filename_entry = tk.Entry(popup)
        filename_entry.pack(pady=5)
        filename_entry.insert(0, self.default_json)

        tk.Label(popup, text="Creator:").pack(pady=5)
        creator_entry = tk.Entry(popup)
        creator_entry.pack(pady=5)
        creator_entry.insert(0, self.default_creator)

        def create_json():
            filename = filename_entry.get().strip()
            creator = creator_entry.get().strip()
            if not filename.endswith(".json"):
                filename += ".json"

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            initial_data = {
                "creator": creator,
                "last_change": now,
                "tags": self.default_tags,
                "notes": []
            }
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(initial_data, file, ensure_ascii=False, indent=4)

            self.json_file = filename
            #messagebox.showinfo("Erfolg", f"Datei '{filename}' wurde erstellt!")
            popup.destroy()

        tk.Button(popup, text="create", command=create_json).pack(pady=5)

    def create_widgets(self):
        title_frame = tk.Frame(self.root, bg=self.theme["bg_color"])
        title_frame.pack(pady=(10, 0), fill="x", padx=10)

        tk.Label(title_frame, text="Title:", bg=self.theme["bg_color"], fg=self.theme["fg_color"]).pack(side="left")
        self.title_entry = tk.Entry(title_frame, bg=self.theme["entry_bg"], fg=self.theme["fg_color"])
        self.title_entry.pack(side="left", expand=True, fill="x", padx=(5, 5))

        self.switch_button = tk.Button(title_frame, text="🌙", command=self.toggle_theme, width=3)
        self.switch_button.pack(side="right")

        tk.Label(self.root, text="Notes:", bg=self.theme["bg_color"], fg=self.theme["fg_color"]).pack()
        self.notes_text = tk.Text(self.root, height=5, bg=self.theme["entry_bg"], fg=self.theme["fg_color"])
        self.notes_text.pack(pady=(0, 10), padx=10)

        tag_frame = tk.Frame(self.root, bg=self.theme["bg_color"])
        tag_frame.pack(pady=(0, 10))

        tk.Label(tag_frame, text="Tags:", bg=self.theme["bg_color"], fg=self.theme["fg_color"]).pack(side="left")
        self.tag_var = tk.StringVar(value=self.default_tags[0])
        self.tag_dropdown = ttk.Combobox(tag_frame, textvariable=self.tag_var, state="readonly")
        self.tag_dropdown["values"] = self.default_tags
        self.tag_dropdown.pack(side="left", padx=5)

        self.settings_button = tk.Button(tag_frame, text="⚙", command=self.open_tag_manager, width=3)
        self.settings_button.pack(side="left")

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit, bg=self.theme["button_bg"], fg=self.theme["button_fg"])
        self.submit_button.pack(pady=(0, 10))

    def open_tag_manager(self):
        tag_popup = tk.Toplevel()
        tag_popup.title("Tag Manager")
        tag_popup.geometry("300x400")
        tag_popup.attributes('-topmost', True)

        with open(self.json_file, "r") as file:
            data = json.load(file)

        tk.Label(tag_popup, text="Configure Tags:").pack(pady=5)
        tag_list = data["tags"]

        def delete_tag(tag):
            tag_list.remove(tag)
            refresh_tags()

        def add_tag():
            new_tag = new_tag_entry.get().strip()
            if new_tag and new_tag not in tag_list:
                tag_list.append(new_tag)
                refresh_tags()

        def refresh_tags():
            for widget in tags_frame.winfo_children():
                widget.destroy()
            for tag in tag_list:
                tag_row = tk.Frame(tags_frame)
                tag_row.pack(fill="x", padx=5, pady=2)
                tk.Label(tag_row, text=tag).pack(side="left", padx=5)
                tk.Button(tag_row, text="🗑", command=lambda t=tag: delete_tag(t), width=3).pack(side="right")

        tags_frame = tk.Frame(tag_popup)
        tags_frame.pack(pady=5, fill="both", expand=True)

        new_tag_entry = tk.Entry(tag_popup)
        new_tag_entry.pack(pady=5)
        tk.Button(tag_popup, text="➕ add Tag", command=add_tag).pack(pady=5)

        tk.Button(tag_popup, text="Save", command=lambda: self.save_tags(tag_list, tag_popup)).pack(pady=10)
        refresh_tags()

    def save_tags(self, tag_list, popup):
        with open(self.json_file, "r") as file:
            data = json.load(file)
        data["tags"] = tag_list
        with open(self.json_file, "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        self.tag_dropdown["values"] = tag_list
        popup.destroy()

    def apply_theme(self):
        self.theme = self.dark_mode if self.current_theme == "dark" else self.light_mode
        self.root.configure(bg=self.theme["bg_color"])

    def toggle_theme(self):
        self.current_theme = "light" if self.current_theme == "dark" else "dark"
        self.apply_theme()
        self.switch_button.config(text="🌙" if self.current_theme == "dark" else "☀")

    def submit(self):
        title = self.title_entry.get()
        notes = self.notes_text.get("1.0", tk.END).strip()
        tag = self.tag_var.get().strip()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if not notes:
            messagebox.showerror("Error", "The note cannot be empty!")
            return
        
        if not title:
            title = "empty"

        if not tag:
            tag = self.tag_dropdown["values"][0]

        new_note = {"title": title, "note": notes, "tag": tag, "added": now}

        with open(self.json_file, "r") as file:
            data = json.load(file)

        data["notes"].append(new_note)
        data["last_change"] = now

        with open(self.json_file, "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        #messagebox.showinfo("Erfolg", "Notiz gespeichert!")
        self.title_entry.delete(0, tk.END)
        self.notes_text.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuickNoteApp(root)
    root.mainloop()

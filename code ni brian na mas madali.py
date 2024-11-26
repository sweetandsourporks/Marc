import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk


# Professor Class
class Professor:
    def __init__(self, name, title, contact, email, picture=None):
        self.name = name
        self.title = title
        self.contact = contact
        self.email = email
        self.picture = picture


# Main App Class
class ProfessorDirectoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Professor Directory")
        self.root.geometry("1000x700")
        self.setup_styles()
        
        # Data
        self.professors = [
            Professor("Mr. Brian Sarmiento", "Instructor", "+1-555-0123", "brianjmesonez@gmail.com"),
            Professor("Dr. Charles Tabares", "Professor", "+1-555-0124", "sarah.johnson@university.edu"),
            Professor("Dr. Wensley Naarte", "Instructor", "+1-555-0125", "michael.brown@university.edu")
        ]

        # Main UI
        self.setup_ui()

    # Define styles for the app
    def setup_styles(self):
        self.colors = {
            'primary': '#2563eb',  # Modern blue
            'secondary': '#3b82f6',  # Lighter blue
            'background': '#f8fafc',  # Light gray background
            'surface': '#ffffff',  # White surface
            'text': '#1e293b',  # Dark text
            'text_secondary': '#64748b'  # Secondary text
        }

        # Apply styles
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Modern.TFrame', background=self.colors['background'])
        self.style.configure('Modern.TButton',
                             padding=(10, 5),
                             background=self.colors['primary'],
                             foreground='white',
                             font=('Segoe UI', 10),
                             borderwidth=0)
        self.style.map('Modern.TButton', background=[('active', self.colors['secondary'])])
        self.style.configure('Modern.Title.TLabel', font=('Segoe UI', 24, 'bold'), background=self.colors['background'])
        self.style.configure('Modern.Treeview', rowheight=40, font=('Segoe UI', 10),
                             background=self.colors['surface'], foreground=self.colors['text'])
        self.style.configure('Modern.Treeview.Heading',
                             font=('Segoe UI', 12, 'bold'), background=self.colors['primary'], foreground='white')

    # Set up UI elements
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, style='Modern.TFrame', padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        ttk.Label(main_frame, text="Professor Directory", style='Modern.Title.TLabel').pack(anchor='w', pady=(0, 10))

        # Search bar and Add button
        search_frame = ttk.Frame(main_frame, style='Modern.TFrame')
        search_frame.pack(fill=tk.X, pady=(0, 20))
        self.search_var = tk.StringVar()
        self.search_var.trace_add('write', self.update_treeview)
        ttk.Entry(search_frame, textvariable=self.search_var, font=('Segoe UI', 11), width=30).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(search_frame, text="Add Professor", style='Modern.TButton', command=self.open_add_professor).pack(side=tk.RIGHT)

        # Treeview (Table)
        tree_frame = ttk.Frame(main_frame, style='Modern.TFrame')
        tree_frame.pack(fill=tk.BOTH, expand=True)
        self.tree = ttk.Treeview(tree_frame, columns=('Name', 'Title', 'Contact', 'Email'), show='headings', style='Modern.Treeview')
        for col in ('Name', 'Title', 'Contact', 'Email'):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200, anchor='w')
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind('<<TreeviewSelect>>', self.show_professor_profile)
        self.update_treeview()

    # Refresh treeview based on search
    def update_treeview(self, *args):
        search_text = self.search_var.get().lower()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for prof in self.professors:
            if search_text in prof.name.lower() or search_text in prof.title.lower():
                self.tree.insert('', tk.END, values=(prof.name, prof.title, prof.contact, prof.email))

    # Open professor profile
    def show_professor_profile(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return
        prof_name = self.tree.item(selected_item[0])['values'][0]
        prof = next((p for p in self.professors if p.name == prof_name), None)

        if prof:
            self.display_profile_window(prof)

    # Display profile window
    def display_profile_window(self, professor):
        profile_win = tk.Toplevel(self.root)
        profile_win.title("Professor Profile")
        profile_win.geometry("500x400")
        ttk.Label(profile_win, text=professor.name, font=('Segoe UI', 20, 'bold')).pack(pady=10)
        ttk.Label(profile_win, text=professor.title, font=('Segoe UI', 16)).pack(pady=5)
        ttk.Label(profile_win, text=f"Contact: {professor.contact}", font=('Segoe UI', 14)).pack(pady=5)
        ttk.Label(profile_win, text=f"Email: {professor.email}", font=('Segoe UI', 14)).pack(pady=5)
        ttk.Button(profile_win, text="Close", style='Modern.TButton', command=profile_win.destroy).pack(pady=20)

    # Open Add Professor dialog
    def open_add_professor(self):
        add_win = tk.Toplevel(self.root)
        add_win.title("Add Professor")
        add_win.geometry("400x300")

        fields = {'Name': '', 'Title': '', 'Contact': '', 'Email': ''}
        entries = {}

        for i, (field, _) in enumerate(fields.items()):
            ttk.Label(add_win, text=field).grid(row=i, column=0, padx=10, pady=5, sticky='w')
            entry = ttk.Entry(add_win, font=('Segoe UI', 11))
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[field] = entry

        def save_professor():
            values = {field: entry.get().strip() for field, entry in entries.items()}
            if any(not val for val in values.values()):
                messagebox.showerror("Error", "All fields must be filled!")
                return
            self.professors.append(Professor(**values))
            self.update_treeview()
            add_win.destroy()

        ttk.Button(add_win, text="Save", style='Modern.TButton', command=save_professor).grid(row=len(fields), column=1, pady=10)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ProfessorDirectoryApp(root)
    root.mainloop()

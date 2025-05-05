import tkinter as tk
from tkinter import messagebox
import webbrowser

# Global constant for maps URL
MAP_URL = "https://www.google.com/maps"

# --- Login Window ---
class LoginPage:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login Page")
        self.window.geometry("300x200")
        self.window.configure(bg="#f0f0f0")

        tk.Label(self.window, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack(pady=5)

        tk.Label(self.window, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.window, text="Login", command=self.check_login).pack(pady=15)

        self.window.mainloop()

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "123":
            self.window.destroy()  # Close login window
            Dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

# --- Dashboard Window ---
class Dashboard:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Dashboard")
        self.window.geometry("400x200")
        self.window.configure(bg="#e0ffe0")

        tk.Label(self.window, text="Welcome to Dashboard", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.window, text="Open Google Maps", command=self.open_map).pack(pady=10)
        tk.Button(self.window, text="Logout", command=self.logout).pack(pady=10)

        self.window.mainloop()

    def open_map(self):
        webbrowser.open(MAP_URL)

    def logout(self):
        self.window.destroy()  # Simulate crash
        LoginPage()            # Restart login window

# Run the app
if __name__ == "__main__":
    LoginPage()

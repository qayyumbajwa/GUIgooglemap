import tkinter as tk
from tkinter import messagebox
import webbrowser

# Constant for Google Maps URL
GOOGLE_MAPS_URL = "https://www.google.com/maps"

# Login Window Class
class GoogleMapsLogin:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Google Maps App - Login")
        self.window.geometry("300x200")
        self.window.configure(bg="#dce1f0")

        tk.Label(self.window, text="Username:", font=("Arial", 10)).pack(pady=5)
        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack(pady=5)

        tk.Label(self.window, text="Password:", font=("Arial", 10)).pack(pady=5)
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.window, text="Login", command=self.validate_login).pack(pady=15)

        self.window.mainloop()

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "123":
            self.window.destroy()  # Close login window
            GoogleMapsDashboard()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")

# Dashboard Window Class
class GoogleMapsDashboard:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Google Maps App - Dashboard")
        self.window.geometry("400x200")
        self.window.configure(bg="#e0ffe0")

        tk.Label(self.window, text="Welcome to Google Maps Dashboard", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.window, text="Open Google Maps", command=self.open_google_maps, width=20).pack(pady=10)
        tk.Button(self.window, text="Logout", command=self.logout, width=20).pack(pady=10)

        self.window.mainloop()

    def open_google_maps(self):
        webbrowser.open(GOOGLE_MAPS_URL)

    def logout(self):
        self.window.destroy()  # Simulate crash
        GoogleMapsLogin()      # Return to login

# Main App Entry Point
if __name__ == "__main__":
    GoogleMapsLogin()

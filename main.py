import tkinter as tk

def main():
    """
    Main function to create and run the Tkinter application.
    """
    def on_button_click():
        """
        Function to handle button click event.
        """
        output_label.config(text="Hello, World!\nThis is a test to verify that the packaging was successful.")

    # Create the main window
    root = tk.Tk()
    root.title("Tkinter Application")
    root.geometry("300x150")  # Set window size

    # Create a button
    button = tk.Button(root, text="Click Me", command=on_button_click)
    button.pack(pady=20)  # Add some padding

    # Create a label to display output
    output_label = tk.Label(root, text="", justify="center")
    output_label.pack()

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
import os
import shutil
import tkinter as tk
from tkinter import messagebox

def copy_and_rename_pur_file(source_path, target_path, new_filename):
    try:
        # Ensure the target directory exists
        os.makedirs(target_path, exist_ok=True)
        
        # Construct the full path to the new file
        new_file_path = os.path.join(target_path, new_filename)
        
        # Copy and rename the file
        shutil.copyfile(source_path, new_file_path)
        
        print(f"Copied and renamed file to: {new_file_path}")
        return new_file_path
    except Exception as e:
        print(f"Error copying and renaming file: {e}")
        messagebox.showerror("Error", f"Error copying and renaming file: {e}")
        return None

def create_client_structure(base_path, client_name, source_pur_path):
    # Create the main client folder
    client_folder_path = os.path.join(base_path, client_name)
    assets_folder_path = os.path.join(client_folder_path, 'assets')  # Assets folder inside the client's folder
    
    try:
        # Create the client folder
        os.makedirs(client_folder_path)
        print(f"Created directory: {client_folder_path}")
        
        # Create the assets folder inside the client's folder
        os.makedirs(assets_folder_path)
        print(f"Created directory: {assets_folder_path}")
    except FileExistsError:
        print(f"The directory {client_folder_path} or {assets_folder_path} already exists.")
        messagebox.showerror("Error", f"The directory {client_folder_path} or {assets_folder_path} already exists.")
        return
    
    # New filename for the .pur file (using client_name as an example)
    new_filename = f"{client_name}.pur"
    
    # Copy and rename .pur file from source to client's assets folder
    copied_pur_path = copy_and_rename_pur_file(source_pur_path, client_folder_path, new_filename)
    
    if copied_pur_path:
        messagebox.showinfo("Success", f"Created client structure for {client_name}.\nCopied .pur file to:\n{copied_pur_path}")

def on_submit():
    client_name = entry.get().strip()
    if client_name:
        base_path = r"\\ORTHANC\Fileserver\Torres\Ark Assets\Projects"  # Network path
        source_pur_path = r"\\ORTHANC\Fileserver\Torres\My Programms\Client Master\assets\NewScene.pur"
        create_client_structure(base_path, client_name, source_pur_path)
    else:
        messagebox.showwarning("Input Error", "Please enter a client's name.")

# Create the main window
root = tk.Tk()
root.title("Client Master")
root.geometry("400x200")
root.configure(bg='#1e1e1e')  # Dark background

# Create and place the label
label = tk.Label(root, text="Enter the client's name:", font=('Calibri', 14), bg='#1e1e1e', fg='white')
label.pack(pady=(20, 10))

# Create and place the entry widget
entry = tk.Entry(root, width=30, font=('Helvetica', 12), bg='#2e2e2e', fg='white', insertbackground='white', relief='flat')
entry.pack(pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Create Structure", command=on_submit, font=('Calibri', 12), bg='#2e2e2e', fg='white', relief='flat', padx=10, pady=5)
submit_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()

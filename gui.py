"""
Modern GUI for Image Metadata Remover
Features: Drag-and-drop, bulk upload, custom output folder selection
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
from pathlib import Path
import threading
from metadata_remover import MetadataRemover


class MetadataRemoverGUI:
    """Modern GUI for the metadata remover application."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Image Metadata Remover - 100% Clean Images")
        self.root.geometry("900x750")
        self.root.minsize(850, 650)
        
        # Initialize metadata remover
        self.remover = MetadataRemover()
        
        # File list
        self.file_list = []
        self.output_folder = None
        self.is_processing = False
        
        # Configure style
        self.setup_styles()
        
        # Create UI
        self.create_widgets()
        
        # Center window
        self.center_window()
    
    def setup_styles(self):
        """Configure modern styles for the application."""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        bg_color = "#f0f0f0"
        accent_color = "#2196F3"
        success_color = "#4CAF50"
        danger_color = "#f44336"
        
        # Configure styles
        style.configure("Title.TLabel", font=("Segoe UI", 24, "bold"), 
                       foreground="#333333")
        style.configure("Subtitle.TLabel", font=("Segoe UI", 10), 
                       foreground="#666666")
        style.configure("Header.TLabel", font=("Segoe UI", 12, "bold"), 
                       foreground="#333333")
        style.configure("Info.TLabel", font=("Segoe UI", 9), 
                       foreground="#666666")
        
        style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"),
                       padding=10, background=accent_color)
        style.configure("Success.TButton", font=("Segoe UI", 10, "bold"),
                       padding=10, background=success_color)
        style.configure("Danger.TButton", font=("Segoe UI", 9),
                       padding=5, background=danger_color)
        
        self.root.configure(bg=bg_color)
    
    def center_window(self):
        """Center the window on the screen."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """Create all UI widgets."""
        # Main container with reduced padding
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self.create_header(main_frame)
        
        # Upload section
        self.create_upload_section(main_frame)
        
        # File list section
        self.create_file_list_section(main_frame)
        
        # Output folder section
        self.create_output_section(main_frame)
        
        # Progress section
        self.create_progress_section(main_frame)
        
        # Action buttons
        self.create_action_buttons(main_frame)
    
    def create_header(self, parent):
        """Create the header section."""
        header_frame = ttk.Frame(parent)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        title = ttk.Label(header_frame, text="🖼️ Image Metadata Remover", 
                         style="Title.TLabel")
        title.pack()
        
        subtitle = ttk.Label(header_frame, 
                           text="Remove EXIF, copyright, and all embedded data - Make your images 100% clean",
                           style="Subtitle.TLabel")
        subtitle.pack()
    
    def create_upload_section(self, parent):
        """Create the upload section with drag-and-drop."""
        upload_frame = ttk.LabelFrame(parent, text="📁 Upload Images", padding="10")
        upload_frame.pack(fill=tk.X, pady=(0, 8))
        
        # Drag and drop area
        drop_frame = tk.Frame(upload_frame, bg="#e3f2fd", relief=tk.RIDGE, 
                             borderwidth=2, height=90)
        drop_frame.pack(fill=tk.X, pady=(0, 8))
        drop_frame.pack_propagate(False)
        
        # Enable drag and drop
        drop_frame.drop_target_register(DND_FILES)
        drop_frame.dnd_bind('<<Drop>>', self.on_drop)
        
        drop_label = tk.Label(drop_frame, 
                             text="🎯 Drag & Drop Images Here\n\nSupported formats: JPG, PNG, TIFF, WebP, BMP",
                             bg="#e3f2fd", fg="#1976D2", 
                             font=("Segoe UI", 10, "bold"))
        drop_label.pack(expand=True)
        
        # Upload buttons
        button_frame = ttk.Frame(upload_frame)
        button_frame.pack(fill=tk.X)
        
        btn_single = ttk.Button(button_frame, text="📄 Upload Single Image",
                               command=self.upload_single, style="Primary.TButton")
        btn_single.pack(side=tk.LEFT, padx=(0, 10), expand=True, fill=tk.X)
        
        btn_multiple = ttk.Button(button_frame, text="📚 Upload Multiple Images",
                                 command=self.upload_multiple, style="Primary.TButton")
        btn_multiple.pack(side=tk.LEFT, expand=True, fill=tk.X)
    
    def create_file_list_section(self, parent):
        """Create the file list section."""
        list_frame = ttk.LabelFrame(parent, text="📋 Selected Images", padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        
        # Info label
        self.file_count_label = ttk.Label(list_frame, text="No images selected",
                                         style="Info.TLabel")
        self.file_count_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Scrollable listbox
        list_container = ttk.Frame(list_frame)
        list_container.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(list_container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.file_listbox = tk.Listbox(list_container, yscrollcommand=scrollbar.set,
                                       font=("Segoe UI", 9), selectmode=tk.EXTENDED,
                                       bg="#ffffff", relief=tk.FLAT, borderwidth=1)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.file_listbox.yview)
        
        # Clear button
        btn_clear = ttk.Button(list_frame, text="🗑️ Clear List",
                              command=self.clear_file_list, style="Danger.TButton")
        btn_clear.pack(anchor=tk.E, pady=(5, 0))
    
    def create_output_section(self, parent):
        """Create the output folder selection section."""
        output_frame = ttk.LabelFrame(parent, text="💾 Output Folder", padding="10")
        output_frame.pack(fill=tk.X, pady=(0, 8))
        
        # Container for label and button
        content_frame = ttk.Frame(output_frame)
        content_frame.pack(fill=tk.X)
        
        self.output_label = ttk.Label(content_frame, 
                                     text="Default: 'cleaned_images' folder in source directory",
                                     style="Info.TLabel", wraplength=600)
        self.output_label.pack(anchor=tk.W, pady=(0, 8))
        
        btn_output = ttk.Button(content_frame, text="📂 Choose Output Folder",
                               command=self.choose_output_folder, 
                               style="Primary.TButton")
        btn_output.pack(anchor=tk.W)
    
    def create_progress_section(self, parent):
        """Create the progress section."""
        progress_frame = ttk.LabelFrame(parent, text="📊 Progress", padding="10")
        progress_frame.pack(fill=tk.X, pady=(0, 8))
        
        self.progress_label = ttk.Label(progress_frame, text="Ready to process images",
                                       style="Info.TLabel")
        self.progress_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.progress_bar = ttk.Progressbar(progress_frame, mode='determinate', length=400)
        self.progress_bar.pack(fill=tk.X)
    
    def create_action_buttons(self, parent):
        """Create the main action buttons."""
        action_frame = ttk.LabelFrame(parent, text="⚡ Action", padding="10")
        action_frame.pack(fill=tk.X, pady=(0, 5))
        
        self.btn_process = ttk.Button(action_frame, text="🚀 REMOVE METADATA & CLEAN IMAGES",
                                     command=self.process_images, 
                                     style="Success.TButton")
        self.btn_process.pack(fill=tk.X, ipady=12)
    
    def on_drop(self, event):
        """Handle drag and drop event."""
        files = self.root.tk.splitlist(event.data)
        self.add_files(files)
    
    def upload_single(self):
        """Upload a single image file."""
        file = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.tiff *.tif *.webp *.bmp"),
                ("All files", "*.*")
            ]
        )
        if file:
            self.add_files([file])
    
    def upload_multiple(self):
        """Upload multiple image files."""
        files = filedialog.askopenfilenames(
            title="Select images",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.tiff *.tif *.webp *.bmp"),
                ("All files", "*.*")
            ]
        )
        if files:
            self.add_files(files)
    
    def add_files(self, files):
        """Add files to the processing list."""
        added_count = 0
        for file in files:
            # Handle directory drops
            if os.path.isdir(file):
                # Add all images in the directory
                for root, dirs, filenames in os.walk(file):
                    for filename in filenames:
                        filepath = os.path.join(root, filename)
                        if self.remover.is_supported_image(filepath) and filepath not in self.file_list:
                            self.file_list.append(filepath)
                            self.file_listbox.insert(tk.END, filepath)
                            added_count += 1
            else:
                # Add single file
                if self.remover.is_supported_image(file) and file not in self.file_list:
                    self.file_list.append(file)
                    self.file_listbox.insert(tk.END, file)
                    added_count += 1
        
        self.update_file_count()
        
        if added_count > 0:
            messagebox.showinfo("Files Added", f"Added {added_count} image(s) to the list.")
    
    def clear_file_list(self):
        """Clear the file list."""
        if self.file_list and messagebox.askyesno("Clear List", 
                                                  "Are you sure you want to clear the file list?"):
            self.file_list.clear()
            self.file_listbox.delete(0, tk.END)
            self.update_file_count()
    
    def update_file_count(self):
        """Update the file count label."""
        count = len(self.file_list)
        if count == 0:
            self.file_count_label.config(text="No images selected")
        elif count == 1:
            self.file_count_label.config(text="1 image selected")
        else:
            self.file_count_label.config(text=f"{count} images selected")
    
    def choose_output_folder(self):
        """Choose a custom output folder."""
        folder = filedialog.askdirectory(title="Select output folder")
        if folder:
            self.output_folder = folder
            # Shorten path if too long
            display_path = folder if len(folder) < 60 else "..." + folder[-57:]
            self.output_label.config(text=f"Output: {display_path}")
    
    def get_output_folder(self):
        """Get the output folder path."""
        if self.output_folder:
            return self.output_folder
        
        # Default: create 'cleaned_images' folder in the first file's directory
        if self.file_list:
            first_file_dir = os.path.dirname(self.file_list[0])
            return os.path.join(first_file_dir, "cleaned_images")
        
        return None
    
    def update_progress(self, current, total, message):
        """Update progress bar and label."""
        progress = (current / total) * 100
        self.progress_bar['value'] = progress
        self.progress_label.config(text=f"Processing: {current}/{total} - {message}")
        self.root.update_idletasks()
    
    def process_images(self):
        """Process all images in the list."""
        if not self.file_list:
            messagebox.showwarning("No Images", "Please add images to process.")
            return
        
        if self.is_processing:
            messagebox.showwarning("Processing", "Already processing images. Please wait.")
            return
        
        output_folder = self.get_output_folder()
        if not output_folder:
            messagebox.showerror("Error", "Could not determine output folder.")
            return
        
        # Confirm processing
        if not messagebox.askyesno("Confirm Processing", 
                                   f"Process {len(self.file_list)} image(s)?\n\n"
                                   f"Output folder: {output_folder}"):
            return
        
        # Disable process button
        self.is_processing = True
        self.btn_process.config(state=tk.DISABLED)
        
        # Process in a separate thread
        thread = threading.Thread(target=self._process_thread, args=(output_folder,))
        thread.daemon = True
        thread.start()
    
    def _process_thread(self, output_folder):
        """Thread function for processing images."""
        try:
            results = self.remover.process_images(
                self.file_list,
                output_folder,
                progress_callback=self.update_progress
            )
            
            # Show results
            self.root.after(0, self._show_results, results, output_folder)
            
        except Exception as e:
            self.root.after(0, messagebox.showerror, "Error", 
                          f"An error occurred during processing:\n{str(e)}")
        finally:
            self.is_processing = False
            self.root.after(0, lambda: self.btn_process.config(state=tk.NORMAL))
    
    def _show_results(self, results, output_folder):
        """Show processing results."""
        summary = self.remover.get_summary()
        summary += f"\n📂 Output folder: {output_folder}"
        
        messagebox.showinfo("Processing Complete", summary)
        
        # Ask if user wants to open output folder
        if messagebox.askyesno("Open Folder", "Do you want to open the output folder?"):
            os.startfile(output_folder)
        
        # Reset progress
        self.progress_bar['value'] = 0
        self.progress_label.config(text="Ready to process images")


def main():
    """Main entry point for the application."""
    root = TkinterDnD.Tk()
    app = MetadataRemoverGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

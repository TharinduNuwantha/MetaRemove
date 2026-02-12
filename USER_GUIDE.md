# 📖 User Guide - Image Metadata Remover

## Table of Contents
1. [Getting Started](#getting-started)
2. [Interface Overview](#interface-overview)
3. [Step-by-Step Guide](#step-by-step-guide)
4. [Features Explained](#features-explained)
5. [Tips & Best Practices](#tips--best-practices)
6. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Installation
1. Make sure Python 3.7+ is installed on your system
2. Open a terminal/command prompt in the project folder
3. Run: `pip install -r requirements.txt`

### Launching the Application

**Windows:**
- Double-click `run.bat`, OR
- Open Command Prompt and run: `python gui.py`

**macOS/Linux:**
- Run in terminal: `python3 gui.py`, OR
- Make `run.sh` executable: `chmod +x run.sh` then run: `./run.sh`

---

## Interface Overview

The application window consists of several sections:

### 1. Header
- **Title**: "Image Metadata Remover"
- **Subtitle**: Brief description of the tool's purpose

### 2. Upload Images Section
- **Drag & Drop Area**: Large blue area where you can drag files
- **Upload Single Image**: Button to select one image
- **Upload Multiple Images**: Button to select multiple images at once

### 3. Selected Images List
- Shows all images you've added
- Displays the full file path for each image
- Shows count of selected images
- **Clear List** button to remove all files

### 4. Output Folder Section
- Shows where cleaned images will be saved
- **Choose Output Folder** button to select custom location
- Default: Creates `cleaned_images` folder in source directory

### 5. Progress Section
- Progress bar showing processing status
- Text showing current operation

### 6. Action Button
- **Remove Metadata & Clean Images**: Main button to start processing

---

## Step-by-Step Guide

### Basic Usage (Single Image)

1. **Launch the application**
   - Double-click `run.bat` (Windows) or run `python gui.py`

2. **Add an image**
   - Click "Upload Single Image"
   - Browse and select your image
   - OR drag and drop the image into the blue area

3. **Process the image**
   - Click "Remove Metadata & Clean Images"
   - Confirm the operation
   - Wait for processing to complete

4. **Access your cleaned image**
   - Click "Yes" when asked to open the output folder
   - OR navigate to the `cleaned_images` folder manually

### Bulk Processing (Multiple Images)

1. **Launch the application**

2. **Add multiple images**
   - Click "Upload Multiple Images"
   - Select all images you want to process (Ctrl+Click or Shift+Click)
   - OR drag and drop a folder containing images
   - OR drag and drop multiple image files

3. **Review the list**
   - Check that all desired images are listed
   - Use "Clear List" if you need to start over

4. **Choose output location (optional)**
   - Click "Choose Output Folder" if you want a custom location
   - Otherwise, images will be saved in `cleaned_images` folder

5. **Process all images**
   - Click "Remove Metadata & Clean Images"
   - Confirm the operation
   - Monitor progress in the progress bar
   - Wait for completion message

6. **Access your cleaned images**
   - All cleaned images will be in the output folder
   - Named as `[original_name]_cleaned.jpg`

---

## Features Explained

### 🎯 Drag & Drop
- **What it does**: Allows you to drag files/folders directly into the app
- **How to use**: 
  - Drag image files from File Explorer/Finder
  - Drop them in the blue "Drag & Drop" area
  - Files are automatically added to the list

### 📄 Single Image Upload
- **What it does**: Opens a file browser to select one image
- **How to use**: Click the button and navigate to your image
- **Best for**: Processing individual images

### 📚 Multiple Image Upload
- **What it does**: Opens a file browser to select multiple images
- **How to use**: 
  - Click the button
  - Hold Ctrl (Windows/Linux) or Cmd (Mac) to select multiple files
  - Or use Shift to select a range
- **Best for**: Batch processing

### 📂 Custom Output Folder
- **What it does**: Lets you choose where cleaned images are saved
- **How to use**: Click "Choose Output Folder" and select a directory
- **Default behavior**: Creates `cleaned_images` in the source folder

### 🔄 Default Output Folder
- **Location**: Same directory as your first selected image
- **Folder name**: `cleaned_images`
- **Auto-creation**: Folder is created automatically if it doesn't exist

### 📊 Progress Tracking
- **Real-time updates**: See which image is being processed
- **Progress bar**: Visual indication of completion percentage
- **Status messages**: Success/failure for each image

---

## Tips & Best Practices

### ✅ Do's

1. **Keep Backups**: Always keep original images as backup
2. **Batch Process**: Process multiple images at once for efficiency
3. **Organize First**: Put images in a folder before processing
4. **Check Output**: Verify cleaned images before deleting originals
5. **Use Default Output**: Let the app create the output folder automatically

### ❌ Don'ts

1. **Don't Delete Originals**: Keep your original images safe
2. **Don't Interrupt**: Let processing complete before closing the app
3. **Don't Mix Formats**: While supported, keep similar formats together
4. **Don't Overwrite**: The app prevents this, but be careful with manual moves

### 💡 Pro Tips

1. **Folder Drag & Drop**: Drag entire folders to add all images at once
2. **Clear and Restart**: Use "Clear List" to start fresh without restarting
3. **Custom Naming**: Output files are named `[original]_cleaned.jpg`
4. **Quality Preserved**: Images are saved at 95% quality (high)
5. **Format Conversion**: All outputs are JPEG for maximum compatibility

---

## Troubleshooting

### Problem: "No images selected" error
**Solution**: Add images using upload buttons or drag & drop before processing

### Problem: Application won't start
**Solution**: 
- Ensure Python 3.7+ is installed
- Run: `pip install -r requirements.txt`
- Check for error messages in the console

### Problem: Drag & drop not working
**Solution**: 
- Make sure you're dropping files in the blue area
- Try using the upload buttons instead
- Restart the application

### Problem: Images not processing
**Solution**:
- Check that files are supported formats (JPG, PNG, TIFF, WebP, BMP)
- Ensure files aren't corrupted
- Check file permissions
- Look at error messages in the completion dialog

### Problem: Can't find cleaned images
**Solution**:
- Check the `cleaned_images` folder in the source directory
- Or check the custom output folder you selected
- Click "Yes" when asked to open the output folder after processing

### Problem: Output folder error
**Solution**:
- Ensure you have write permissions in the output location
- Try selecting a different output folder
- Use the default output location

### Problem: Processing is slow
**Solution**:
- This is normal for large images or many files
- Don't interrupt the process
- Close other applications to free up resources

---

## What Metadata is Removed?

The application removes **ALL** metadata including:

- ✅ **EXIF Data**: Camera make, model, settings, date/time
- ✅ **GPS Coordinates**: Location information
- ✅ **Copyright Info**: Author, copyright notices
- ✅ **Software Info**: Editing software details
- ✅ **Comments**: Text descriptions and notes
- ✅ **Thumbnails**: Embedded preview images
- ✅ **Color Profiles**: ICC color profiles
- ✅ **XMP Data**: Adobe metadata
- ✅ **IPTC Data**: News and media metadata
- ✅ **Orientation**: Image rotation data
- ✅ **Any other embedded data**

---

## Need More Help?

If you encounter issues not covered here:
1. Check the README.md file
2. Review error messages carefully
3. Open an issue on GitHub
4. Ensure all dependencies are installed correctly

---

**Happy cleaning! 🎉**

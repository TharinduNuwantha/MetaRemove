# 🖼️ Image Metadata Remover

A professional Python application that removes **all metadata** from images, including EXIF data, copyright information, GPS coordinates, and any other embedded data. Make your images 100% clean!

## ✨ Features

- **🎯 Drag & Drop Support** - Simply drag images into the application
- **📄 Single Image Upload** - Process one image at a time
- **📚 Bulk Upload** - Process multiple images simultaneously
- **📂 Custom Output Folder** - Choose where to save cleaned images
- **🔄 Default Output** - Automatically creates a `cleaned_images` folder in the source directory
- **✅ Multiple Format Support** - JPG, PNG, TIFF, WebP, BMP
- **🚀 Fast Processing** - Efficient metadata removal
- **📊 Progress Tracking** - Real-time progress updates
- **💯 100% Clean** - Removes ALL metadata including:
  - EXIF data (camera settings, date/time)
  - GPS coordinates
  - Copyright information
  - Author information
  - Software information
  - Comments and descriptions
  - Thumbnails
  - Color profiles
  - Any other embedded data

## 📋 Requirements

- Python 3.7 or higher
- Windows, macOS, or Linux

## 🚀 Installation

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Running the Application

**Windows:**
```bash
python gui.py
```

Or double-click `run.bat`

**macOS/Linux:**
```bash
python3 gui.py
```

### Using the Application

1. **Upload Images:**
   - Drag and drop images into the designated area
   - Click "Upload Single Image" for one file
   - Click "Upload Multiple Images" for bulk selection

2. **Choose Output Folder (Optional):**
   - By default, cleaned images are saved in a `cleaned_images` folder
   - Click "Choose Output Folder" to select a custom location

3. **Process Images:**
   - Click "Remove Metadata & Clean Images"
   - Wait for processing to complete
   - Cleaned images will be saved as `[filename]_cleaned.jpg`

## 🔒 Privacy & Security

- **100% Local Processing** - All processing happens on your computer
- **No Internet Required** - Your images never leave your device
- **No Data Collection** - We don't collect or store any information
- **Complete Metadata Removal** - All embedded data is stripped

## 📁 Output Format

- All cleaned images are saved as **JPEG** format
- Quality: 95% (high quality)
- Optimized for size
- Completely metadata-free

## 🛠️ Technical Details

### Supported Input Formats
- JPEG (.jpg, .jpeg)
- PNG (.png)
- TIFF (.tiff, .tif)
- WebP (.webp)
- BMP (.bmp)

### What Gets Removed
- **EXIF Data**: Camera make/model, settings, date/time
- **GPS Data**: Location coordinates
- **Copyright**: Author, copyright notices
- **Software**: Editing software information
- **Comments**: Any text descriptions
- **Thumbnails**: Embedded preview images
- **Color Profiles**: ICC profiles
- **XMP Data**: Adobe metadata
- **IPTC Data**: News/media metadata

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## 📄 License

This project is open source and available under the MIT License.

## ⚠️ Disclaimer

This tool is designed to remove metadata from images. Always keep backups of your original images. The developers are not responsible for any data loss.

## 🆘 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Made with ❤️ for privacy-conscious users**

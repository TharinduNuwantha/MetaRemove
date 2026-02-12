# 📦 Project Structure

```
MetaRemove/
│
├── 📄 gui.py                    # Main GUI application
├── 📄 metadata_remover.py       # Core metadata removal engine
├── 📄 requirements.txt          # Python dependencies
├── 📄 test.py                   # Basic functionality tests
├── 📄 examples.py               # Programmatic usage examples
│
├── 🪟 run.bat                   # Windows launcher
├── 🐧 run.sh                    # Linux/macOS launcher
│
├── 📖 README.md                 # Main documentation
├── 📖 USER_GUIDE.md             # Detailed user guide
├── 📖 QUICKSTART.md             # Quick start guide
├── 📖 PROJECT_INFO.md           # This file
│
└── 📁 .gitignore                # Git ignore rules
```

---

## 🎯 Project Overview

**Image Metadata Remover** is a professional Python application designed to remove all metadata from images, ensuring complete privacy and data cleanliness.

### Key Features
- ✅ **100% Metadata Removal** - Removes EXIF, GPS, copyright, and all embedded data
- ✅ **Modern GUI** - User-friendly interface with drag-and-drop support
- ✅ **Bulk Processing** - Handle single or multiple images efficiently
- ✅ **Multiple Formats** - Supports JPG, PNG, TIFF, WebP, BMP
- ✅ **Privacy-Focused** - All processing happens locally
- ✅ **Cross-Platform** - Works on Windows, macOS, and Linux

---

## 🔧 Technical Stack

### Core Technologies
- **Python 3.7+** - Main programming language
- **Tkinter** - GUI framework (built-in with Python)
- **TkinterDnD2** - Drag-and-drop functionality
- **Pillow (PIL)** - Image processing library
- **piexif** - EXIF data handling

### Architecture
```
┌─────────────────────────────────────┐
│         GUI Layer (gui.py)          │
│  - User interface                   │
│  - Event handling                   │
│  - Progress tracking                │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Core Engine (metadata_remover.py) │
│  - Metadata removal logic           │
│  - File validation                  │
│  - Batch processing                 │
└─────────────────────────────────────┘
```

---

## 📋 File Descriptions

### Core Application Files

#### `gui.py`
- **Purpose**: Main GUI application
- **Features**:
  - Modern, responsive interface
  - Drag-and-drop support
  - Single and bulk upload
  - Custom output folder selection
  - Real-time progress tracking
  - Threading for non-blocking UI

#### `metadata_remover.py`
- **Purpose**: Core metadata removal engine
- **Features**:
  - Comprehensive metadata stripping
  - Multiple format support
  - Batch processing capabilities
  - Error handling and reporting
  - Progress callbacks

### Utility Files

#### `test.py`
- **Purpose**: Basic functionality testing
- **Usage**: `python test.py`
- **Tests**: Format validation, basic operations

#### `examples.py`
- **Purpose**: Programmatic usage examples
- **Usage**: `python examples.py`
- **Shows**: Various automation scenarios

### Launcher Scripts

#### `run.bat` (Windows)
- Simple batch file to launch the GUI
- Double-click to run

#### `run.sh` (Unix/Linux)
- Shell script to launch the GUI
- Make executable: `chmod +x run.sh`

### Documentation

#### `README.md`
- Main project documentation
- Installation instructions
- Feature overview
- Technical details

#### `USER_GUIDE.md`
- Comprehensive user manual
- Step-by-step tutorials
- Troubleshooting guide
- Tips and best practices

#### `QUICKSTART.md`
- Quick reference guide
- Minimal instructions to get started
- Common usage patterns

---

## 🚀 Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone <repository-url>
cd MetaRemove

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Unix/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python gui.py
```

### Code Style
- **PEP 8** compliant
- Comprehensive docstrings
- Type hints where applicable
- Clear variable naming

### Testing
```bash
# Run basic tests
python test.py

# Run examples
python examples.py
```

---

## 🔒 Privacy & Security

### Data Handling
- **100% Local Processing** - No internet connection required
- **No Data Collection** - Zero telemetry or analytics
- **No External Services** - All operations are offline
- **Complete Metadata Removal** - All embedded data is stripped

### What Gets Removed
1. **EXIF Data**: Camera settings, timestamps
2. **GPS Coordinates**: Location information
3. **Copyright**: Author and copyright notices
4. **Software Info**: Editing software details
5. **Comments**: Text descriptions
6. **Thumbnails**: Embedded previews
7. **Color Profiles**: ICC profiles
8. **XMP/IPTC**: Adobe and media metadata
9. **Orientation**: Rotation data
10. **Any other embedded data**

---

## 📊 Supported Formats

### Input Formats
- ✅ JPEG (.jpg, .jpeg)
- ✅ PNG (.png)
- ✅ TIFF (.tiff, .tif)
- ✅ WebP (.webp)
- ✅ BMP (.bmp)

### Output Format
- **Format**: JPEG
- **Quality**: 95% (high quality)
- **Optimization**: Enabled
- **Metadata**: None (completely clean)

---

## 🎨 GUI Features

### Design Principles
- **Modern**: Clean, professional interface
- **Intuitive**: Easy to understand and use
- **Responsive**: Adapts to window resizing
- **Accessible**: Clear labels and instructions

### User Experience
- **Drag & Drop**: Effortless file addition
- **Bulk Operations**: Process many files at once
- **Progress Feedback**: Real-time status updates
- **Error Handling**: Clear error messages
- **Confirmation Dialogs**: Prevent accidental actions

---

## 🔄 Workflow

### Typical User Flow
```
1. Launch Application
   ↓
2. Add Images (drag-drop or browse)
   ↓
3. (Optional) Choose Output Folder
   ↓
4. Click "Remove Metadata"
   ↓
5. Confirm Processing
   ↓
6. Wait for Completion
   ↓
7. Access Cleaned Images
```

### Default Behavior
- **Output Location**: `cleaned_images` folder in source directory
- **File Naming**: `[original_name]_cleaned.jpg`
- **Duplicate Handling**: Auto-increment (`_cleaned_1.jpg`, `_cleaned_2.jpg`)

---

## 🛠️ Customization

### Programmatic Usage
The `metadata_remover.py` module can be imported and used in other Python scripts:

```python
from metadata_remover import MetadataRemover

remover = MetadataRemover()
success, message = remover.remove_metadata(
    "input.jpg",
    "output.jpg"
)
```

See `examples.py` for more usage patterns.

---

## 📈 Future Enhancements

Potential features for future versions:
- [ ] Additional output formats (PNG, WebP)
- [ ] Batch rename options
- [ ] Preview before/after metadata
- [ ] Command-line interface (CLI)
- [ ] Recursive folder processing
- [ ] Metadata viewing (before removal)
- [ ] Undo functionality
- [ ] Preset configurations
- [ ] Multi-language support

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Bug fixes
- Performance optimizations
- New features
- Documentation improvements
- UI/UX enhancements

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🙏 Acknowledgments

Built with:
- **Pillow** - Image processing
- **piexif** - EXIF handling
- **TkinterDnD2** - Drag-and-drop support
- **Python** - Programming language

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check the documentation files
- Review the examples

---

**Version**: 1.0.0  
**Last Updated**: February 2026  
**Status**: Production Ready ✅

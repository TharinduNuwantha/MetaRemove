# 🚀 Quick Start Guide

## Installation (One-Time Setup)

```bash
# Install dependencies
pip install -r requirements.txt
```

## Running the Application

### Windows
```bash
# Option 1: Double-click
run.bat

# Option 2: Command line
python gui.py
```

### macOS/Linux
```bash
# Option 1: Terminal
python3 gui.py

# Option 2: Shell script
chmod +x run.sh
./run.sh
```

## Quick Usage

1. **Add Images**
   - Drag & drop images into the blue area, OR
   - Click "Upload Single Image" or "Upload Multiple Images"

2. **Process**
   - Click "Remove Metadata & Clean Images"
   - Confirm the action

3. **Get Results**
   - Find cleaned images in the `cleaned_images` folder
   - Or click "Yes" to open the output folder automatically

## That's It! 🎉

Your images are now 100% metadata-free!

---

## What Gets Removed?

✅ EXIF data (camera info, date/time)  
✅ GPS coordinates  
✅ Copyright information  
✅ Author details  
✅ Software information  
✅ Comments and descriptions  
✅ ALL embedded metadata  

## Output Format

- **Format**: JPEG
- **Quality**: 95% (high quality)
- **Naming**: `[original_name]_cleaned.jpg`
- **Location**: `cleaned_images` folder (by default)

## Need Help?

📖 See `USER_GUIDE.md` for detailed instructions  
📝 See `README.md` for full documentation

---

**Privacy First** 🔒 - All processing happens locally on your computer!

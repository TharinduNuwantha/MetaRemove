"""
Image Metadata Remover
A comprehensive tool to remove all metadata from images including EXIF, copyright, and embedded data.
"""

import os
import io
from PIL import Image
import piexif
from pathlib import Path
from typing import List, Tuple


class MetadataRemover:
    """Handles the removal of all metadata from images."""
    
    SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.tiff', '.tif', '.webp', '.bmp'}
    
    def __init__(self):
        self.processed_count = 0
        self.failed_count = 0
        self.errors = []
    
    def is_supported_image(self, file_path: str) -> bool:
        """Check if the file is a supported image format."""
        return Path(file_path).suffix.lower() in self.SUPPORTED_FORMATS
    
    def remove_metadata(self, input_path: str, output_path: str) -> Tuple[bool, str]:
        """
        Remove all metadata from an image.
        
        Args:
            input_path: Path to the input image
            output_path: Path where the cleaned image will be saved
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            # Open the image
            with Image.open(input_path) as img:
                # Convert to RGB if necessary (for PNG with transparency, etc.)
                if img.mode in ('RGBA', 'LA', 'P'):
                    # Create a white background
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    if img.mode in ('RGBA', 'LA'):
                        background.paste(img, mask=img.split()[-1])  # Use alpha channel as mask
                        img = background
                    else:
                        img = img.convert('RGB')
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Create a new image without any metadata
                # We'll save it to a bytes buffer first to ensure all metadata is stripped
                img_bytes = io.BytesIO()
                
                # Save without any EXIF or metadata
                img.save(img_bytes, format='JPEG', quality=95, optimize=True)
                
                # Reload the image from bytes to ensure it's completely clean
                img_bytes.seek(0)
                clean_img = Image.open(img_bytes)
                
                # Save the final clean image
                clean_img.save(output_path, format='JPEG', quality=95, optimize=True)
            
            self.processed_count += 1
            return True, f"Successfully cleaned: {os.path.basename(input_path)}"
            
        except Exception as e:
            self.failed_count += 1
            error_msg = f"Failed to process {os.path.basename(input_path)}: {str(e)}"
            self.errors.append(error_msg)
            return False, error_msg
    
    def process_images(self, input_files: List[str], output_folder: str, 
                      progress_callback=None) -> dict:
        """
        Process multiple images and remove their metadata.
        
        Args:
            input_files: List of input file paths
            output_folder: Folder where cleaned images will be saved
            progress_callback: Optional callback function for progress updates
            
        Returns:
            Dictionary with processing results
        """
        self.processed_count = 0
        self.failed_count = 0
        self.errors = []
        
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        total_files = len(input_files)
        results = {
            'processed': [],
            'failed': [],
            'skipped': []
        }
        
        for idx, input_file in enumerate(input_files):
            # Check if file is a supported image
            if not self.is_supported_image(input_file):
                results['skipped'].append(input_file)
                if progress_callback:
                    progress_callback(idx + 1, total_files, 
                                    f"Skipped (unsupported format): {os.path.basename(input_file)}")
                continue
            
            # Generate output filename
            base_name = Path(input_file).stem
            output_file = os.path.join(output_folder, f"{base_name}_cleaned.jpg")
            
            # Handle duplicate filenames
            counter = 1
            while os.path.exists(output_file):
                output_file = os.path.join(output_folder, 
                                         f"{base_name}_cleaned_{counter}.jpg")
                counter += 1
            
            # Process the image
            success, message = self.remove_metadata(input_file, output_file)
            
            if success:
                results['processed'].append(output_file)
            else:
                results['failed'].append(input_file)
            
            # Update progress
            if progress_callback:
                progress_callback(idx + 1, total_files, message)
        
        return results
    
    def get_summary(self) -> str:
        """Get a summary of the processing results."""
        summary = f"Processing Complete!\n\n"
        summary += f"✓ Successfully processed: {self.processed_count}\n"
        summary += f"✗ Failed: {self.failed_count}\n"
        
        if self.errors:
            summary += f"\nErrors:\n"
            for error in self.errors[:5]:  # Show first 5 errors
                summary += f"  • {error}\n"
            if len(self.errors) > 5:
                summary += f"  ... and {len(self.errors) - 5} more errors\n"
        
        return summary

"""
Example script demonstrating programmatic usage of the metadata remover
This can be used for automation or integration into other projects
"""

from metadata_remover import MetadataRemover
import os


def example_single_image():
    """Example: Process a single image"""
    print("\n" + "="*60)
    print("Example 1: Processing a Single Image")
    print("="*60)
    
    remover = MetadataRemover()
    
    # Define paths
    input_image = "path/to/your/image.jpg"
    output_image = "path/to/output/cleaned_image.jpg"
    
    # Process the image
    success, message = remover.remove_metadata(input_image, output_image)
    
    if success:
        print(f"✅ {message}")
    else:
        print(f"❌ {message}")


def example_bulk_processing():
    """Example: Process multiple images"""
    print("\n" + "="*60)
    print("Example 2: Bulk Processing Multiple Images")
    print("="*60)
    
    remover = MetadataRemover()
    
    # Define input files
    input_files = [
        "path/to/image1.jpg",
        "path/to/image2.png",
        "path/to/image3.tiff",
    ]
    
    # Define output folder
    output_folder = "path/to/output/folder"
    
    # Progress callback function
    def progress_callback(current, total, message):
        print(f"[{current}/{total}] {message}")
    
    # Process all images
    results = remover.process_images(
        input_files,
        output_folder,
        progress_callback=progress_callback
    )
    
    # Print summary
    print("\n" + remover.get_summary())
    print(f"\nProcessed files: {len(results['processed'])}")
    print(f"Failed files: {len(results['failed'])}")
    print(f"Skipped files: {len(results['skipped'])}")


def example_folder_processing():
    """Example: Process all images in a folder"""
    print("\n" + "="*60)
    print("Example 3: Processing All Images in a Folder")
    print("="*60)
    
    remover = MetadataRemover()
    
    # Define input folder
    input_folder = "path/to/input/folder"
    output_folder = "path/to/output/folder"
    
    # Get all image files from the folder
    input_files = []
    for filename in os.listdir(input_folder):
        filepath = os.path.join(input_folder, filename)
        if os.path.isfile(filepath) and remover.is_supported_image(filepath):
            input_files.append(filepath)
    
    print(f"Found {len(input_files)} images in {input_folder}")
    
    # Process all images
    if input_files:
        results = remover.process_images(
            input_files,
            output_folder,
            progress_callback=lambda c, t, m: print(f"[{c}/{t}] {m}")
        )
        
        print("\n" + remover.get_summary())
    else:
        print("No images found to process")


def example_check_supported_formats():
    """Example: Check if a file is supported"""
    print("\n" + "="*60)
    print("Example 4: Checking Supported Formats")
    print("="*60)
    
    remover = MetadataRemover()
    
    test_files = [
        "photo.jpg",
        "image.png",
        "document.pdf",
        "picture.tiff",
        "video.mp4",
        "graphic.webp"
    ]
    
    print("\nSupported formats:")
    for fmt in remover.SUPPORTED_FORMATS:
        print(f"  • {fmt}")
    
    print("\nFile validation:")
    for file in test_files:
        is_supported = remover.is_supported_image(file)
        status = "✅" if is_supported else "❌"
        print(f"  {status} {file}")


def example_custom_output_naming():
    """Example: Custom output file naming"""
    print("\n" + "="*60)
    print("Example 5: Custom Output File Naming")
    print("="*60)
    
    remover = MetadataRemover()
    
    input_files = [
        "vacation_photo_1.jpg",
        "vacation_photo_2.jpg",
        "vacation_photo_3.jpg"
    ]
    
    output_folder = "cleaned_vacation_photos"
    
    # Create output folder
    os.makedirs(output_folder, exist_ok=True)
    
    # Process with custom naming
    for idx, input_file in enumerate(input_files, 1):
        output_file = os.path.join(output_folder, f"clean_vacation_{idx:03d}.jpg")
        success, message = remover.remove_metadata(input_file, output_file)
        print(f"{'✅' if success else '❌'} {message}")


def main():
    """Main function to run all examples"""
    print("\n" + "="*60)
    print("📚 Metadata Remover - Programmatic Usage Examples")
    print("="*60)
    print("\nThese examples show how to use the MetadataRemover class")
    print("in your own Python scripts for automation.\n")
    
    # Note: These are examples - they won't run without actual image files
    print("⚠️  Note: Update the file paths in this script to run the examples")
    print("    with your actual images.\n")
    
    # Show what each example does
    print("Available examples:")
    print("  1. example_single_image() - Process one image")
    print("  2. example_bulk_processing() - Process multiple images")
    print("  3. example_folder_processing() - Process all images in a folder")
    print("  4. example_check_supported_formats() - Check file format support")
    print("  5. example_custom_output_naming() - Custom output naming")
    
    # Run the format checking example (doesn't need actual files)
    example_check_supported_formats()
    
    print("\n" + "="*60)
    print("💡 Tip: Uncomment the example functions above to try them")
    print("    with your own images!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()

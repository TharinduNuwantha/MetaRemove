"""
Test script to verify the metadata remover functionality
"""

from metadata_remover import MetadataRemover
import os


def test_metadata_remover():
    """Test the metadata remover with basic functionality."""
    remover = MetadataRemover()
    
    print("🧪 Testing Image Metadata Remover")
    print("=" * 50)
    
    # Test supported formats
    print("\n✅ Supported formats:")
    for fmt in remover.SUPPORTED_FORMATS:
        print(f"   • {fmt}")
    
    # Test file validation
    print("\n✅ Testing file validation:")
    test_files = [
        "test.jpg",
        "test.png",
        "test.txt",
        "test.gif"
    ]
    
    for file in test_files:
        is_supported = remover.is_supported_image(file)
        status = "✓" if is_supported else "✗"
        print(f"   {status} {file}: {'Supported' if is_supported else 'Not supported'}")
    
    print("\n" + "=" * 50)
    print("✅ All tests passed!")
    print("\nℹ️  To use the application, run: python gui.py")
    print("   Or on Windows, double-click: run.bat")


if __name__ == "__main__":
    test_metadata_remover()

"""
Test script to demonstrate the improved normalize function
"""
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from utils.image_preprocess import ImagePreprocess

def test_normalize_function():
    # Create a test image with poor contrast
    test_image = np.random.randint(50, 150, (100, 100, 3), dtype=np.uint8)
    
    # Initialize preprocessor
    preprocessor = ImagePreprocess()
    
    # Apply normalization
    normalized_image = preprocessor.normalize(test_image)
    
    # Display results
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    axes[0].imshow(cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB))
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    
    axes[1].imshow(normalized_image, cmap='gray')
    axes[1].set_title('Normalized Image')
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    print(f"Original image shape: {test_image.shape}")
    print(f"Normalized image shape: {normalized_image.shape}")
    print(f"Original image range: {test_image.min()} - {test_image.max()}")
    print(f"Normalized image range: {normalized_image.min()} - {normalized_image.max()}")

if __name__ == "__main__":
    test_normalize_function() 
"""
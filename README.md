# Image Encryption Tool
This Python project implements a simple image encryption and decryption tool. Each pixel in the image is transformed to enhance security.

## How It Works
### Encryption
- Takes an encrypted image as input
- Transforms each pixel back:
  - Decreases the pixel values by 50
  - Swaps the red and blue color channels back
  - Ensures pixel values are within the valid range (0-255)
- Saves the decrypted image
### Decryption
- Takes an encrypted image as input
- Transforms each pixel back:
    - Decreases the pixel values by 50
    - Swaps the red and blue color channels back
    - Ensures pixel values are within the valid range (0-255)
- Saves the decrypted image

### Usage
- Clone the repository
- Run the Python Script
- Follow the on-screen prompts to encrypt or decrypt an image

### Requirements
- Python 3
- PIL (Pillow)
- NumPy

    -To install all three run ```pip install Pillow numpy``` in the terminal 

### Additional Comments.
The repository has a ```requirements.txt``` file. To use it run ```pip install -r requirements.txt```. This will install all the necessary Python packages all at once.
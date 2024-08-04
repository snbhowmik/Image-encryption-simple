from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path):
    image = Image.open(input_image_path)
    pixels = np.array(image)

    encrypted_pixels = np.copy(pixels)
    height, width, channels = pixels.shape

    for i in range(height):
        for j in range(width):
            encrypted_pixels[i][j][0], encrypted_pixels[i][j][2] = pixels[i][j][2], pixels[i][j][0]
            encrypted_pixels[i][j] = (encrypted_pixels[i][j] + 50)  

            encrypted_pixels[i][j] = np.clip(encrypted_pixels[i][j], 0, 255)

    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path):
    encrypted_image = Image.open(input_image_path)
    pixels = np.array(encrypted_image)

    decrypted_pixels = np.copy(pixels)
    height, width, channels = pixels.shape

    for i in range(height):
        for j in range(width):
            decrypted_pixels[i][j] = (decrypted_pixels[i][j] - 50)  

            decrypted_pixels[i][j] = np.clip(decrypted_pixels[i][j], 0, 255)

            decrypted_pixels[i][j][0], decrypted_pixels[i][j][2] = decrypted_pixels[i][j][2], decrypted_pixels[i][j][0]

    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

if __name__ == "__main__":
    while True:
        print("\nImage Encryption Tool")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            input_image = input("Enter the path of the image to encrypt: ")
            output_image = input("Enter the path to save the encrypted image: ")
            encrypt_image(input_image, output_image)

        elif choice == '2':
            input_image = input("Enter the path of the image to decrypt: ")
            output_image = input("Enter the path to save the decrypted image: ")
            decrypt_image(input_image, output_image)

        elif choice == '3':
            print("Exiting the tool.")
            break

        else:
            print("Invalid option, please try again.")
from PIL import Image
import numpy as np
import tkinter as tk

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Convert key to integer if it's a string
    if isinstance(key, str):
        key = sum(ord(c) for c in key)
    
    # XOR operation on each pixel value
    encrypted = img_array ^ key
    
    # Convert back to image
    encrypted_img = Image.fromarray(encrypted.astype('uint8'))
    return encrypted_img

def decrypt_image(encrypted_img, key):
    # Convert image to numpy array
    img_array = np.array(encrypted_img)
    
    # Convert key to integer if it's a string
    if isinstance(key, str):
        key = sum(ord(c) for c in key)
    
    # XOR operation to decrypt (XOR with same key)
    decrypted = img_array ^ key
    
    # Convert back to image
    decrypted_img = Image.fromarray(decrypted.astype('uint8'))
    return decrypted_img

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    input_image = "input_image.png"  # Path to your input image
    key =   "my_secret_key"  # Your encryption key      
    
    # Encrypt
    encrypted = encrypt_image(input_image, key)
    encrypted.save("encrypted_image.png")
    
    # Decrypt
    decrypted = decrypt_image(encrypted, key)
    decrypted.save("decrypted_image.png")

if __name__ == "__main__":
    main()
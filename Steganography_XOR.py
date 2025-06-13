import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# ASCII mapping
char_to_ascii = {chr(i): i for i in range(256)}
ascii_to_char = {i: chr(i) for i in range(256)}


    # --- User Input ---
def enc():
    image_path = input("Enter the path to the image: ").strip()

    if not os.path.exists(image_path):
        raise FileNotFoundError("Image path does not exist!")

    secret_message = input("Enter the secret message to hide: ")
    key = input("Enter the encryption key: ")

    if not secret_message or not key:
        raise ValueError("Secret message and key cannot be empty!")

    # --- Load Image ---
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Failed to load image. Check file format and path.")

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.title("Original Image")
    plt.show()

    # --- Convert message and key to ASCII ---
    text_ascii = [char_to_ascii[ch] for ch in secret_message]
    key_ascii = [char_to_ascii[ch] for ch in key]

    # --- Encrypt the message ---
    encrypted_image = image.copy()
    rows, cols, _ = image.shape
    text_len = len(secret_message)
    key_len = len(key)

    n = m = z = kl = 0  # initialize indexes

    for i in range(text_len):
        original_pixel_value = encrypted_image[n, m, z]
        encrypted_value = text_ascii[i] ^ key_ascii[kl]
        encrypted_image[n, m, z] = encrypted_value

        print(f"Embedding '{secret_message[i]}' -> Pixel({n},{m},{z}): {original_pixel_value} XOR {key[kl]}({key_ascii[kl]}) = {encrypted_value}")

        # Advance through image
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == cols:
                m = 0
                n += 1
                if n == rows:
                    raise ValueError("Image not large enough to embed the message.")

        kl = (kl + 1) % key_len

    # Save encrypted image
    output_path = os.path.abspath("encrypted_image.png")
    cv2.imwrite(output_path, encrypted_image)
    print(f"\n[+] Encrypted image saved at: {output_path}")
    plt.imshow(cv2.cvtColor(encrypted_image, cv2.COLOR_BGR2RGB))
    plt.title("Encrypted Image")
    plt.axis('off')
    plt.show()

    # --- Decryption ---

def dec():
    image_path = input("Enter the path to the encrypted image: ").strip()
    key = input("Enter the decryption key: ").strip()

    if not os.path.exists(image_path):
        print("❌ Image file does not exist.")
        return
    
    encrypted_image = cv2.imread(image_path)
    if encrypted_image is None:
        print("❌ Could not read the image.")
        return
    
    key_ascii = [char_to_ascii[ch] for ch in key]
    key_len = len(key)

    rows, cols, _ = encrypted_image.shape
    decrypted_message = ""

    try:
        length = int(input("Enter the number of characters to decrypt: ").strip())
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return

    n = m = z = kl = 0

    for _ in range(length):
        if n >= rows:
            print("❌ Image does not contain enough data.")
            return

        val = encrypted_image[n, m, z]
        orig_char = ascii_to_char[val ^ key_ascii[kl]]
        decrypted_message += orig_char

        print(f"Decrypting ({n},{m},{z}) -> {val} XOR {key[kl]} = '{orig_char}'")

        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == cols:
                m = 0
                n += 1
                if n == rows:
                    raise ValueError("Image not large enough to embed the message.")

        kl = (kl + 1) % key_len

    print("\n✅ Decrypted Message:", decrypted_message)

def main():
    print("📦 Welcome to XOR Image Steganography")
    print("1. Encrypt a message into an image")
    print("2. Decrypt a message from an image")

    choice = input("Enter your choice (1/2): ").strip()

    if choice == '1':
        enc()
    elif choice == '2':
        dec()
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
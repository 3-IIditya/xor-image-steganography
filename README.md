# 🔐 XOR Image Steganography Tool

A Python-based tool to hide and retrieve secret messages inside images using XOR-based steganography. This project is ideal for educational purposes, simple data hiding, and getting hands-on with image processing and basic encryption.

---

## 🚀 Features

- 🔒 Encrypt a secret message inside an image using XOR
- 🔓 Decrypt the hidden message using the same key
- 🧠 User-friendly CLI with menu-driven interface
- 🖼️ Image preview using Matplotlib
- 📁 Clean code structure for learning or extending

---

## 🧠 How It Works

This tool modifies the RGB values of an image's pixels by XOR-ing them with ASCII values of your secret message and key. The message is encoded into the image pixel-by-pixel and can later be retrieved by reversing the XOR operation using the same key.

---

## 📦 Requirements

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

# 🧑‍💻 How to Use
Run the Python script:

```bash
python encrypt_decrypt.py
```
Follow the prompts:

# 🔐 Encryption

```bash
📦 Welcome to XOR Image Steganography
1. Encrypt a message into an image
2. Decrypt a message from an image

Enter your choice (1/2): 1
Enter the path to the image to encrypt: sample.png
Enter the secret message to hide: hello
Enter the encryption key: 123
```
The output will be:

encrypted_image.png saved in your project folder

Preview of the encrypted image

# 🔓 Decryption

```bash
Enter your choice (1/2): 2
Enter the path to the encrypted image: encrypted_image.png
Enter the decryption key: 123
Enter the number of characters to decrypt: 5
```
Output:
```bash
✅ Decrypted Message: hello
```

# 💡 Notes
Make sure the image has enough pixels to hold your message.

The decryption process requires you to know:

The original encryption key

The length of the message

# 📝 License

This project is licensed under the MIT License – see the LICENSE file for details.

# 👨‍💻 Author

Developed by AĐ!†¥∆ 

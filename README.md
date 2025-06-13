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


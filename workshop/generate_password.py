#!/usr/bin/env python3
"""
Password Generator for PDF Chatbot Authentication
This script helps you generate hashed passwords for secure authentication.
"""

import hashlib
import getpass

def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    print("🔐 PDF Chatbot Password Generator")
    print("=" * 40)
    print()
    
    # Get username
    username = input("Enter username: ").strip()
    if not username:
        print("❌ Username cannot be empty!")
        return
    
    # Get password
    password = getpass.getpass("Enter password: ")
    if not password:
        print("❌ Password cannot be empty!")
        return
    
    # Confirm password
    confirm_password = getpass.getpass("Confirm password: ")
    if password != confirm_password:
        print("❌ Passwords do not match!")
        return
    
    # Generate hash
    password_hash = hash_password(password)
    
    print()
    print("✅ Password generated successfully!")
    print()
    print("Add these to your environment variables:")
    print("-" * 40)
    print(f"APP_USERNAME = {username}")
    print(f"APP_PASSWORD_HASH = {password_hash}")
    print()
    print("For Streamlit Cloud, add to secrets:")
    print("-" * 40)
    print(f"APP_USERNAME = \"{username}\"")
    print(f"APP_PASSWORD_HASH = \"{password_hash}\"")
    print()
    print("For .env file:")
    print("-" * 40)
    print(f"APP_USERNAME={username}")
    print(f"APP_PASSWORD_HASH={password_hash}")

if __name__ == "__main__":
    main()

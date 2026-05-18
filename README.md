# Password Tools
*Simple Tools to Secure the Average Person.*

## Installation

To suit a variety of users, `.exe` and `.appimage` files are included in each release. To use this app, simply run the correct file for your operating system. For Windows, run the `.exe` file. For Linux (most distributions), run the `.appimage` file.

## Overview

It is now more important than ever to have strong passwords and good habits! This app contains tools to:

- Generate strong passwords with a variety of options to fit your security needs. 
- Analyze the strength and security of current passwords and provide ideas for improvement. 
- Provide education about password Dos and Don'ts to keep you safe and secure online. 
- And more coming soon!

### Password Creation

This tool uses python's Secrets module to generate completely random yet secure strings of numbers, letters, and characters, all in an easily usable GUI. Alternatively, it can select random whole dictionary words to string together so your password is easier to remember. 

### Password Analysis

This tool uses the formula for entropy (or randomness; E = log2(R**L)) to determine how difficult your password is to crack. It accounts for usage of repeated characters, dictionary words, substitutions (a --> @, etc), and digits to show a more accurate determination of randomness/security. 

### Security

You might have qualms about putting your secure information into a random developer's program. But don't worry; all sensitive information is only stored in your computer's memory, meaning this data will be forgotten as soon as you close the program unless you choose to save it. 

Please note that when creating a password, while you can select random whole words, it is recommended to use random characters. Using whole words found in the dictionary in a password will make it cryptographically weaker and decrease entropy, making it easier to crack. While using whole words is not inherently unsafe, it is more secure and thus recommended to use random characters. 

## Contributing

Generally I don't accept pull requests, so don't take it personally if I don't accept yours. If you find a bug/have a suggestion please make a new Issue and I'll resolve it in the next release. 

## Notes
*If you really want to run main.py and not the `.exe` or `.appimage` file, simply clone the repository, ensure you have these modules installed (listed below) in a virtual environment, and run main.py. Just using the exe or appimage is recommended for simplicity and to ensure the program doesn't break, however.*

- Customtkinter
- Pillow
- Pyperclip

# Password Tools
*Simple Tools to Secure the Average Person.*

## Installation

To use this app, simply run the correct file for your operating system. For Windows, run the `.exe` file. For Linux (all distributions), run the `.appimage` file.

## Overview

With all the threats out there, is it now more important than ever to have strong passwords and good habits! This app contains tools to:

- Generate strong passwords with a variety of options to fit your security needs. 
- Analyze the strength and security of current passwords and provide ideas for improvement. 
- Provide education about password Dos and Don'ts to keep you safe and secure online. 
- And more coming soon!

Simply open the app and see how this app can change your life for the better!

### Password Creation

This tool uses python's Random module to generate completely random strings of numbers, letters, and characters, all in an easily usable GUI. 

### Password Analysis

This tool uses the formula for entropy (or randomness; E = log2(R**L)) to determine the security of your submitted password. It also accounts for usage of repeated characters, dictionary words, substitutions (a --> @, etc), and digits to show a more accurate determination of randomness/security. 

### Fully Customizable! 

This app's settings menu allows for customization to fit the user's preferences! Choose between different accent colors, and between different styles of dark and light themes to fit your preferences!

### Security

You might have qualms about putting your secure information into a random developer's program. But don't worry; all sensitive information is only stored in your computer's memory, meaning this data will be forgotten as soon as you close the program. The only data that stays on your computer is your customization choices. 

## Contributing

I'm an independent developer and I'm still learning, and I like to work on my own projects mostly without help. Please don't take it personally if I don't accept your pull request. =)

## Notes
*If you really want to run main.py and not the `.exe` or `.appimage` file, simply clone the repository, ensure you have these modules installed (listed below), and run main.py. Just using the exe or appimage is recommended, however.*

- Customtkinter
- Pillow
- Pyperclip
# Password Tools
*Simple Tools to Secure the Average Person.*

## Installation

To use this app, simply download the included `.exe` file. Unfortunately, support for Linux is not included currently but is coming soon!

## Overview

With all the threats out there, is it now more important than ever to have strong passwords and good habits! This app contains tools to:

- Generate strong passwords with a variety of options to fit your security needs. 
- Analyze the strength and security of current passwords and provide ideas for improvement. 
- Provide education about password Dos and Don'ts to keep you safe and secure online. 
- And more coming soon!

Simply open the app and see how this app can change your life for the better!

### Password Creation

This tool uses python's Secrets module to generate completely random yet secure strings of numbers, letters, and characters, all in an easily usable GUI. 

### Password Analysis

This tool uses the formula for entropy (or randomness; E = log2(R**L)) to determine how difficult your password is to crack. It accounts for usage of repeated characters, dictionary words, substitutions (a --> @, etc), and digits to show a more accurate determination of randomness/security.  

### And More Coming Soon!

This project is still in pre-release, so not all features are included. Check back later for more!

### Security

You might have qualms about putting your secure information into a random developer's program. But don't worry; all sensitive information is only stored in your computer's memory, meaning this data will be forgotten as soon as you close the program. The only data that stays on your computer is your customization choices. 

## Contributing

I'm an independent developer and I'm still learning, and I like to work on my own projects mostly without help. Please don't take it personally if I don't accept your pull request. =)

## Notes
*If you really want to run main.py and not the `.exe` or `.appimage` file, simply clone the repository, ensure you have these modules installed (listed below), and run main.py. Just using the `.exe` or `.appimage` is recommended, however. It is recommended that you install the dependencies in a virtual environment to make sure there are no conflicts with other projects*

- Customtkinter
- Pillow
- Pyperclip
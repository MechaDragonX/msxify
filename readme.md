# MSXify

## What is this?
- A simple script that takes Japanese text input and converts this into a format supported by emulators for the ASCII/Microsoft Japanese computer standard, the MSX, from the 80s
- Essentially, fullwidth to halfwidth katakana with the extra carriage returns required by either the MSX or the openMSX emulator
    - I don't know which

## Why?
- Old Japnese computers struggled to handle Japanese in the first place, and while now we have the extra memory to handle all Japanese characters in a way that is pleasing to the eye and easy to read, that was not the case then
- openMSX's own text input is really borked when not using English, which odd since the MSX had an extremely limited presence in Europe
- Early adventure games required typing in commands, as opposed to borrowing from *The Portopia Serial Murder Case*'s system on console with a visible menu of actions, and so a reliable way of giving it this input is necesarry


## Prerequisites
- `pyperclip`

## How to use
1. ```
   python msxify.py <Text>
   ```
2. Converted text is copied to yoru clipboard
3. Paste it into the emulator. **openMSX's text input is pretty borked, so it might not work perfectly.**

## Supported emulators
- openMSX
    - Only tested on Linux, but it probably would work on Windows and macOS


## FAQ
- Does this work for other MSX emulators?
    - I don't know
- Will this support other computers in the future?
    - There's more adventure games for PC88 so I might write a function for it
- Will there be a GUI?
    - Unlikely. I can't write GUI that works

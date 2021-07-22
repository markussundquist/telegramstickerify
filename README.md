# telegramstickerify
A simple script that turns image files into a Telegram sticker compatible format.

Tested on Windows, but should run in all UNIX type operating systems

## What it does in detail
This script scales images to a size, where the longest axis is 512px large

It also converts them to the required .png format

This script supports the following image formats:

.jpg,
.jpeg,
.png,
.gif,
.tif,
.tiff,

## Why
I did this, because I really hate the process of manually resizing images and changing their formats

You decide, whether that's useful

## How to use

1. Add all of the images you wish convert into the "ImageBin"-folder
2. Run the TelegramStickerify.py in cmd, PowerShell or terminal
3. Choose your filename in the program and the program (for ex. choosing the name "new_image" will create files named new_image1.png, new_image2.png...)
4. All done. All of the images saved in the "ImagesReady"-folder should be compatible with the telegram sticker bot.

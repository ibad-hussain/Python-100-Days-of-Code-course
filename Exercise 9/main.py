# EXERCISE 9 - SHOUTOUTS TO EVERYONE
# Problem Statement: Write a program to pronounce list of names using win32 API (pywin32 library). If you are given a list l as follows:
    # l = ["Ali", "Ahmed", "Arman"]
    # Your program should pronouce:
        # Shoutout to Ali
        # Shoutout to Ahmed
        # Shoutout to Arman



import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

lsts = ["hamza", "izaan", "saad", "ali", "asad"]
for lst in lsts:
    speaker.Speak(f"Shoutout to {lst}")
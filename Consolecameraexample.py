from ByteLightProject import ConsoleCam

cam = ConsoleCam.start()  # Starting to record.

print("Hello, JynPopMod!")    # Printing while Camera is recording.
print("This output is being captured.")

captured_output = cam.get_new() # Saving the record.

cam.stop()   # Stopping capturing.

print(captured_output)  # Printing captured output.   U dont have to print it u can use it for data like checking for a spesific message in console.

print("This will not be in the captured output.")   # This won't be captured

# Be cool 🧊 no not that type.That type:😎

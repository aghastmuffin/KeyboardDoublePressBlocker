import keyboard, time #no installation should be necesary, if it is run pip install keyboard
while True:
    key = keyboard.read_key()
    if len(key) == 1:
        keyboard.block_key(key)
        time.sleep(0.1)
        keyboard.unblock_key(key) 

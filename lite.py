import keyboard, time #no installation should be necesary, if it is run pip install keyboard
#this is not set up in a normal module fashion, however it is on pypi, if you would like to set it up, please configure it yourself.
while True:
    key = keyboard.read_key()
    if len(key) == 1:
        keyboard.block_key(key)
        time.sleep(0.1)
        keyboard.unblock_key(key) 

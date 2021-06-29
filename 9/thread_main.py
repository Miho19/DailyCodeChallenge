import logging
import threading
import concurrent.futures





if __name__ == '__main__':
    format =  "%(asctime)s: %(threadName)-10s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    
        
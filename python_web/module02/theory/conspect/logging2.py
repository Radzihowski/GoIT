import logging

logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler("program.log"),
        logging.StreamHandler()
    ])
logging.warning('An example message.')
logging.warning('Another message')

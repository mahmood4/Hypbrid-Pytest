import logging
# Remove all handlers associated with the root logger object.
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
#logging.basicConfig(level = logging.INFO)
class logGen:
    @staticmethod
    def loggen():
       # logging.basicConfig(filename="..\\Logs\\automation.log",format='%(asctime)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.basicConfig(filename="C:\\Users\\user\\PycharmProjects\\Hybrid-Pytest\\Logs\\automation.log", format='%(asctime)s: %(message)s',
                           datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
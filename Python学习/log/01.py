import logging
LOG_FORMAT = "%(asctime)s *%(levelname)s *-> %(message)s"

logging.basicConfig(filename="gc.log",level=logging.DEBUG, format=LOG_FORMAT)

logging.debug("this is a debug")
logging.info("this is a info")
logging.warning("this is a warning")
logging.error("this is a error")
logging.critical("this is a critical")

# 另一种写法
logging.log(logging.DEBUG,"this is a logDEBUG")
logging.log(logging.INFO,"this is a logINFO")
logging.log(logging.WARNING,"this is a logWARNING")
logging.log(logging.ERROR,"this is a logERROR")
logging.log(logging.CRITICAL,"this is a logCRITICAL")

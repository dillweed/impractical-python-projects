"""TBA."""
# Create and configure logger
import logging


logging.basicConfig(filename="log_anagrams.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

# Creating an object
log = logging.getLogger()

# Setting the threshold of logger to DEBUG
log.setLevel(logging.INFO)

# Test messages
# log.debug("Harmless debug Message")
# log.info("Just an information")
# log.warning("Its a Warning")
# log.error("Did you try to divide by zero")
# log.critical("Internet is down")

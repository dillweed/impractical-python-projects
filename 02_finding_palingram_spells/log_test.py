import time
import logger
start_time = time.time()
logger.log.info("Runtime for main() was %s seconds.",
                str(time.time() - start_time))

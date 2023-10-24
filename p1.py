from lib import *
import time
import schedule

example()
"""
schedule.every(1).minutes.do(example)

while True:
    schedule.run_pending()
    time.sleep(1)
    
"""
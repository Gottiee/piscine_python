import datetime
import time

now = datetime.datetime.now()
timestamp = time.time()

regular = "{:,.4f}".format(timestamp)
scientific = "{:.2e} in scientific notation".format(timestamp)

print("Seconds since January 1, 1970:", regular, 'or', scientific)
print(now.strftime("%b %d, %Y"))
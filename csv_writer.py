import csv, uuid
from random import randrange
from time import time
ID_MAX = 2147483647
ROWS_COUNT = 5000000

with open('employee_file.csv', mode='w') as employee_file:
    start_time = time()
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in range(ROWS_COUNT):
        if i % 2 == 0:
            employee_writer.writerow([randrange(ID_MAX), 'John Smith', 'Accounting', '123 Main St San Jose, CA, 95123'])
        else:
            employee_writer.writerow([randrange(ID_MAX), 'Erica Meyers', 'IT', '456 Market St San Jose, CA, 95123'])
        i += 1
    
    end_time = time()
    seconds_elapsed = end_time - start_time

    hours, rest = divmod(seconds_elapsed, 3600)
    minutes, seconds = divmod(rest, 60)
    print(f'It took {hours} hours, {minutes} minutes and {seconds} seconds to finish the job.')
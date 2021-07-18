import csv
from time import time

start_time = time()
with open('employee_file.csv', newline='') as csvfile:
    rdr = csv.reader(csvfile)
    end_time = time()
    seconds_elapsed = end_time - start_time

    hours, rest = divmod(seconds_elapsed, 3600)
    minutes, seconds = divmod(rest, 60)
    print(f'It took {hours} hours, {minutes} minutes and {seconds} seconds to read in the file.')

    start_time = time()
    l = sorted(rdr, key=lambda x: x[0], reverse=False)
    end_time = time()
    seconds_elapsed = end_time - start_time

    hours, rest = divmod(seconds_elapsed, 3600)
    minutes, seconds = divmod(rest, 60)
    print(f'It took {hours} hours, {minutes} minutes and {seconds} seconds to sort the file.')


start_time = time()
with open('employee_file_sorted.csv', 'w') as csvout:
    wrtr = csv.writer(csvout)
    wrtr.writerows(l)
end_time = time()
seconds_elapsed = end_time - start_time

hours, rest = divmod(seconds_elapsed, 3600)
minutes, seconds = divmod(rest, 60)
print(f'It took {hours} hours, {minutes} minutes and {seconds} seconds to write the file.')
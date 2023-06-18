#!/opt/homebrew/bin/python3

import sys

# how to run this script:
# chmod +x clean_up.py && ./clean_up.py input.txt output.txt

if __name__ == "__main__":
    args = sys.argv
    print("Arguments are: {}".format(args))
    if len(args) < 3:
        print("Please provide STAGE argument: gamma or prod!")
        raise Exception("Please provide required arguments!")
    
    in_file = args[1]
    out_file = args[2]

    with open(in_file) as file:
        i = 0
        lines = ""
        for line in file:
            if i % 2:
                lines = lines + line.rstrip() + " "
            if i % 5 == 0:
                lines = lines + "\n"
            i = i + 1
        print("lines are: {}".format(lines))

    with open(out_file, "w") as out:
        out.write("%s" % lines)

    print("Finished cleaning up transcripts to this file: {}".format(out_file))


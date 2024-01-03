import sys
import main

args = sys.argv

if len(args) == 2:
    main.main(int(args[1]))
else:
    print("Usage: python parsing_bar.py [number]")
# author: Tiffany Timbers
# modified by: Wanying Ye
# date: 2021-11-19

"""This script prints out docopt args.
Usage: demo.py <arg1> [<arg4>] --arg2=<arg2> [--arg3=<arg3>]

Options:
<arg1>             Takes any value (this is a required positional argument)
[<arg4>]          Takes any value (this is an optional positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
""" 

from docopt import docopt
opt = docopt(__doc__)

def main(arg1, arg4, arg2, arg3):
  print(opt)
  print(type(opt))
  print(opt["<arg4>"])

if __name__ == "__main__":
    main(opt["<arg1>"], opt["<arg4>"], opt["--arg2"], opt["--arg3"])

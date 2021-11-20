# author: Tiffany Timbers
# modified by: Wanying Ye
# date: 2021-11-19

"This script prints out docopt args.
Usage: demo.R <arg1> [<arg4>] --arg2=<arg2> [--arg3=<arg3>]
Options:
<arg1>             Takes any value (this is a required positional argument)
[<arg4>]          Takes any value (this is an optional positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
" -> doc

library(docopt)
opt <- docopt(doc)

main <- function(arg, arg4, arg2, arg3) {
  print(opt)
  print(typeof(opt))
  print(opt$arg4)
}

main(opt$arg1, opt$arg4, opt$arg2, opt$arg3)
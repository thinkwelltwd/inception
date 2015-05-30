#!/usr/bin/python
import sys, time
from inception.argparsers import BootstrapArgParser, PlantArgParser, LearnArgParser, SyncArgParser
from inception.argparsers.make import MakeArgParser
from inception.argparsers.exceptions import InceptionArgParserException
import logging
logging.basicConfig(level = logging.DEBUG)

if __name__ == "__main__":
    args = sys.argv
    if(len(args) > 1):
        del args[0]


    modeDict = {
        "bootstrap": BootstrapArgParser,
        #"bootstrap2": BootstrapCommandParser2,
        "make": MakeArgParser,
        "plant": PlantArgParser,
        "learn": LearnArgParser,
        "sync": SyncArgParser
    }

    if(len(args) == 0 or args[0] not in modeDict):
        print("Available commands:\n===================")
        print(", ".join(modeDict.keys()))

        sys.exit(1)

    mode = args[0]
    parser = modeDict[mode]()
    #args = vars(parser.parse_args())
    #if len(sys.argv) == 1:

    try:
        start = int(time.time())
        if not parser.process():
            parser.print_help()
        else:
            end = int(time.time())
            elapsed = end - start
            print("Finished in %s seconds" % elapsed)
    except InceptionArgParserException as e:
        print("ERROR!!\n%s" % e)
        sys.exit(1)


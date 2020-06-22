import optparse
parser = optparse.OptionParser()
parser.add_option("-n", "--name", default = "world", 
dest="name", help="Say hello to NAME", metavar = 
"NAME")

(options, args) = parser.parse_args()
print("Hello %s!" % options.name)

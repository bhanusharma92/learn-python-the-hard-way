from sys import argv
from os.path import exists
script, from_file, to_file = argv

print("Copying from %s to %s"%(from_file, to_file))

in_file = open(from_file)
in_data = in_file.read()

print("The input file is %d bytes long"%len(in_data))

print("Does the output file exits %r"%exists(to_file))
print("ready hit Enter to continue Crl-C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print("Allright its done")
out_file.close()
in_file.close()


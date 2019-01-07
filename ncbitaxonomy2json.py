#!/usr/bin/env python

#-------------------------------------------#
#                 Packages                  #
#-------------------------------------------#

import sys
import argparse
from anytree import Node, RenderTree, findall, AsciiStyle
#from anytree.importer import JsonImporter
from anytree.exporter import JsonExporter

#-------------------------------------------#
#                  Parsing                  #
#-------------------------------------------#

# Program description
parser = argparse.ArgumentParser(description='Converts the taxidlineage.dmp file from NCBI into json data.',
                                 add_help=True)

# Command-line argument capture
parser.add_argument('--input',
                    help = 'Path to input taxidlineage.dmp file.',
                    action = 'store',
                    dest = 'dmpFile',
                    required = True)

parser.add_argument('--output',
                    help = 'Path to output file to write json data.',
                    action = 'store',
                    dest = 'outFile',
                    required = True)


# Store command-line arguments
args = vars(parser.parse_args())
lineage_filename = args['dmpFile']
output_filename = args['outFile']

# Prepare the export object to hold json
exporter = JsonExporter(indent=2)

#-----------------------------------------#
#              Setup and IO               #
#-----------------------------------------#

# Get number of lines
print("\nCounting number of lines for the progress log:")
with open(lineage_filename) as lfile:
    for i,l in enumerate(lfile):
        pass
    total = i+1
lfile.close()
print("\t" + str(total) + " lines will be processed." + "\n" )

# Open input and output files for processing
lineage_file = open(lineage_filename, "r")
output_file = open(output_filename, "w")


# Initialize the tree object with a root of 0
taxTree = [Node("0")]
currentNode = taxTree

# Initialize the progress bar with 10% increments
counter = 0
perc = 0
division = 0.10
increment = int(total * division)

#----------------------------------------#
#            File Processing             #
#----------------------------------------#

print("Processing the input file:" + "\n")
print ("0% of input file processed.")

# Read dmp file line by line
readline = lineage_file.readline()
while readline:
    # Remove tab characters
    readline = readline.replace("\t","")
    # Split and remove whitespace
    rawline = readline.strip().split("|")
    splitline = [i.strip() for i in rawline if i]
    # Capture the taxonomic ID for the current line
    childID = splitline[0]
    # For taxa IDs in a root position (ie. kingdoms or domains)
    if len(splitline) == 1:
        node = [Node(childID, taxTree[0])]
        currentNode = node
    # Otherwise, we need to figure out the parent hierarchy
    else:
        # Get the parent ID, it will be the last taxonomic id to appear 
        lineage = splitline[1]
        lineagesplit = lineage.split(" ")
        parentID = lineagesplit[len(lineagesplit)-1]
        # Search for the parent node
        # This tree search takes advantage of how the dmp file comes
        # pre-sorted in a hierarchical manner
        # Keep moving up the tree until you find the parent
        while parentID != currentNode[0].name:
            currentNode = [currentNode[0].parent]
        # When the parent is found
        if parentID == currentNode[0].name:
            parentNode = currentNode
            node = [Node(childID, currentNode[0])]
            currentNode = node
        # If no parent was found, exit the program with information
        else:
            print("No parent node found for child " + childID + " and parent " + parentID)
            quit()


    # Progress log update
    counter += 1
    if counter % increment == 0: 
        perc += division * 100
        print(str(perc) + "% of input file processed.")

    # Read next entry
    readline = lineage_file.readline()

#-----------------------------------------#
#                Export                   #
#-----------------------------------------#
data = exporter.export(taxTree[0])
output_file.write(data)

#test = importer.import_(data)
#print(RenderTree(test, style=AsciiStyle()))

# check if 1935183 is a child of 2157
#check = findall(test, filter_=lambda node: node.name == "2157")[0]
#check_children = check.children
#for child in check_children:
#    print(child.name)


#for pre, fill, node in RenderTree(taxTree, style=AsciiStyle()):
    #print("%s%s" % (pre, node.name))
 #    output_file.write(pre + node.name + "\n")

#-----------------------------------------#
#               Cleanup                   #
#-----------------------------------------#
lineage_file.close()
output_file.close()

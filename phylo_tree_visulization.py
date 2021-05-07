#!/usr/bin/python

from Bio import Phylo
import sys

# Take the filename from the argument
tree_file_name = sys.argv[1]

# Read the file to create the tree
tree = Phylo.read(tree_file_name, "newick")

# Draw the tree in ascii
Phylo.draw_ascii(tree)

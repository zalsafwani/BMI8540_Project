#!/bin/bash
TOOLBIN="/home/zalsafwani/bin"
echo $TOOLBIN
# Download the fasta files from GitHub
#wget https://raw.githubusercontent.com/zalsafwani/files/main/gisaid_hcov-19.fasta?token=AOVMHJ7RKG7LLW6BPIOU3ZLAQ2LGM 

# Run the files through MAFFT
#$TOOLBIN/mafft hcov-19_few.fasta > hcov-19_few.aligned.fa

# Use a Python Script to convert MAFFT to Phylip format
#python3 convert_fa_phylip.py hcov-19_few.aligned.fa > hcov-19.phylip 

# Run PhyML on the phylip format
#$TOOLBIN/PhyML-3.1/PhyML-3.1_linux64 -i hcov-19.phylip

# Use a python Script to convert tree from newick to an actual tree
python3 phylo_tree_visulization.py hcov-19.phylip_phyml_tree.txt > view_tree

# Organize result into diffrent folder
mkdir fasta
mkdir output
mkdir phylip
mv *.fa fasta/
mv *.txt output/
mv *.phylip phylip/

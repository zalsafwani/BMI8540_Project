# BMI8540_Project
# Understand how Nebraska SARS-CoV2 might evolve using phylogeny
The purpose of this project is to create a publicly accessible platform with phylogenetic tree for Nebraska SARS-CoV-2. Comparing sequences for known coronavirus strains could help us understand how the disease might evolve and identify mutations. Also, knowing genes that has high mutation rate could be useful in vaccine design. 

## Language and installation
- Python3
- Install a local copy of MAFFT for multiple sequence alignment: [MAFFT wbsite](https://mafft.cbrc.jp/alignment/software/)
1. Choose your machine type for Odin use Linux then scroll down for the Portable package (BSD license), then hit the source. 
2. Then download mafft-7.475-with-extensions-src.tgz or use wget (https://mafft.cbrc.jp/alignment/software/mafft-7.475-with-extensions-src.tgz)
3. tar xfvz mafft-7.475-with-extensions-src.tgz
4. cd mafft-7.475-with-extensions/core 
5. vim Makefile 
6. Change PREFIX to your tools folder
7. Change BINDIR to your bin folder 
8. make clean
9. make
10. make install
11. To run use the absolute path to the mafft file in your bin folder with your your_fasta_file as an argumant
- Installing a local copy of PhyML for phylogenetic analysis: [PhyML wbsite](http://www.atgc-montpellier.fr/phyml/) 
12. Home -> ATGC provides different kind of services : Software downlowad [PhyML download](http://www.atgc-montpellier.fr/phyml/binaries.php). Enter name and email then Download PhyML binaries. Or do (wget http://www.atgc-montpellier.fr/download/binaries/phyml/PhyML-3.1.zip) in your bin foldar
13. unzip the PhyML-3.1.zip file
14. To run use the absolute path to the PhyML-3.1 file then use PhyML-3.1_linux64 if use Odin and -i your_phylip_file


## Specification Guides for Code and Documentation
- Python Documentation:
- Title: Python 3.7.10 documentation
- Author: Python Software Foundation
- Version: 3.7.10
- Date: 27-Jun-2018
- Source: https://docs.python.org/3.7/ 

- Python Style Guide:
- Title: PEP 8 -- Style Guide for Python Code
- Author: Python Software Foundation
- Version: 8
- Date created: 05-Jul-2001
- Source: https://www.python.org/dev/peps/pep-0008/

## Running

## File Descriptions

#! /usr/bin/env bash
#
# Allele Frequency Estimation
#
#   To run the program and estimate allel frequencies, you need a couple
#   of files. The first is the genotype file, which contains genotype info
#   and the second is the location file, containing lat/lon data for 
#   sampling locations.
#
#   To run the most basic version of SCAT3, use the following pattern:
#   ```
#   ./SCAT3 <genotype file> <location file> <outputdir> L
#   ```
#   L is the number of loci present in the genotype file and outputdir is
#   the location that you want the results to end up in. The below code
#   runs this on the example data included in the SCAT3 `doc/` folder.

../src/SCAT3 \
    ../docs/test.genotype.txt \
    ../docs/test.location.txt \
    ./example1-allele_freq_est \
    2

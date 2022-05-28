"""
Creates a filtered version of the bioconcepts file containing only gene entries
"""
import pandas as pd

# load filtered dataset
dat = pd.read_csv(snakemake.input[0], sep='\t')

# create and store subset with only chemical-related entries
dat = dat[(dat.type == 'Chemical')]
dat.reset_index(drop=True).to_feather(snakemake.output[0])


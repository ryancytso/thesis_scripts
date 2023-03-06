#moving smiles column into the first column space, shifting subsequent rows to the right

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('combined5.csv')

# Get the name of the column with SMILES
smiles_col = df.columns[df.columns.str.contains('SMILES', case=False)][0]

# Move the SMILES column to the front of the DataFrame
cols = list(df.columns)
cols.remove(smiles_col)
cols.insert(0, smiles_col)
df = df.loc[:, cols]

# Save the updated DataFrame to a CSV file
df.to_csv('comb6.csv', index=False)

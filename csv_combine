# combining csv files together 

import os
import glob
import pandas as pd

# Path to directory containing CSV files
path = '/Users/ryantso/Documents/Stokescomp/smpdb_metab'

# Use glob to find all CSV files in the directory
all_files = glob.glob(os.path.join(path))

# Combine all CSV files into a single DataFrame
df_combined = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

# Check the number of rows in the combined DataFrame
num_rows = len(df_combined)
max_rows = 20000

if num_rows > max_rows:
    # Calculate the number of new CSV files required
    num_files = num_rows // max_rows + 1

    # Split the DataFrame into chunks of max_rows rows
    df_chunks = [df_combined[i:i+max_rows] for i in range(0, num_rows, max_rows)]

    # Write each chunk to a new CSV file
    for i, df_chunk in enumerate(df_chunks):
        output_path = os.path.join(path, f"combined{i+1}.csv")
        df_chunk.to_csv(output_path, index=False)
        print(f"Wrote {len(df_chunk)} rows to {output_path}")

else:
    # Save the combined DataFrame to a new CSV file in the same directory
    output_path = os.path.join(path, "combined.csv")
    df_combined.to_csv(output_path, index=False)
    print(f"Combined {len(all_files)} CSV files into {output_path}")

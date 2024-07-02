import pandas as pd
import numpy as np

file_path = 'resseries.series'  
data = pd.read_csv(file_path, sep='\s+')  


header = data.columns.tolist()


averages = data.mean()
std_devs = data.std()


results = pd.DataFrame({'RESIDUE': header[1:],  
                        'FRECUENCY': averages[1:],
                        })


output_file_path = 'processed_contacts.csv'  
results.to_csv(output_file_path, index=False)




import pandas as pd

# Example data for alpha and beta
data = {
    'alpha': [1/2**0.5, 1, 0, 1/3**0.5],
    'beta': [1/2**0.5, 0, 1, (2/3)**0.5]
}

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file named 'photon.csv'
df.to_csv('photon.csv', index=False)

print("CSV file 'photon.csv' created successfully.")

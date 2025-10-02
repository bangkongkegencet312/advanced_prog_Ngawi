import pandas as pd
import numpy as np

# Profile database admin Tashim (value database)
profile_ngawi = {
    'Name': ['Tashim'],
    'Age': [22],
    'Oshi JMK48': ['Imut'],
    'Reason to be a barudakers': ['love kissing with another member']
}

# Variable to define database with data frame
profile_df = pd.DataFrame(profile_ngawi)

# Display the complete DataFrame.
print("My Kisah (Pandas DataFrame)")
print(profile_df)
print("\n" + "="*40 + "\n")

# To demonstrate the use of numpy, we can convert the DataFrame to a numpy array.
# NumPy is highly optimized for numerical operations and is the backbone of pandas.
profile_np_array = np.array(profile_df)

# Display the numpy array.
print("--- My Profile Data (Numpy Array) ---")
print(profile_np_array)
print("\n" + "="*40 + "\n")

# You can also access individual elements from the DataFrame.
name = profile_df['Name'].values[0]
age = profile_df['Age'].values[0]

print(f"Hello, my name is {name} and I am {age} years old.")

# Pijay jawa usluk usluk
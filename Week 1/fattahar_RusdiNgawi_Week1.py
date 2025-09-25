import pandas as pd
import numpy as np

# Menggunakan NumPy array untuk menyimpan data
data = {
    "Name": np.array(["Fattah_Ahmad"]),
    "Age": np.array([21]),
    "Oshi JMK48": np.array(["Mas_Rusdi"]),
    "Reason to be a barudakers": np.array(["Cemimiw"])
}

# Membuat DataFrame dari dictionary yang berisi NumPy array
df = pd.DataFrame(data)

# Menampilkan DataFrame
print(df)
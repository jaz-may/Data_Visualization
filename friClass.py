import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(43)

# df = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie", "David", "Eve"], "Age": [25, 30, 59, 40, 45], "City": ["New York", "Los Angeles", "Chicago", "Houston", np.nan]})
data = np.random.normal(0,1,10000)
# bins = np.arange(min(data), max(data), 100)
plt.hist(data, edgecolor="white", bins=30)
# plt.grid()
plt.savefig("F1")
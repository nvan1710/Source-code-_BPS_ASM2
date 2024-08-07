

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = pd.DataFrame({
    'Time': [1, 2, 3, 4, 5],
    'Sales': [10, 20, 15, 25, 30]
})

# Create a line chart
sns.lineplot(x='Time', y='Sales', data=data)
plt.xlabel('Time')
plt.ylabel('Sales')
plt.title('Sales Over Time')
plt.show()


# import matplotlib.pyplot as plt

# # Sample data
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 25, 30]

# # Create a line chart
# plt.plot(x, y)
# plt.xlabel('Time')
# plt.ylabel('Sales')
# plt.title('Sales Over Time')
# plt.show()

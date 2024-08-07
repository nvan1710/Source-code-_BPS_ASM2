import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
df = pd.read_csv('website_access_category_table.csv')

# Tính số lần sử dụng của từng loại trình duyệt
browser_counts = df['Browser'].value_counts()

# Vẽ biểu đồ tròn
plt.figure(figsize=(10, 7))
plt.pie(browser_counts, labels=browser_counts.index, autopct='%1.1f%%', colors=plt.get_cmap('tab20').colors)
plt.title('Browser Usage Distribution')
plt.show()

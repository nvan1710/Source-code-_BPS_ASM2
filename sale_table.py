import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
df = pd.read_csv('sale_table.csv')

# Lọc các đơn hàng bị trả lại
returned_df = df[df['OrderStatus'] == 'Shipped']

# Nhóm theo ProductID và tính tổng số lượng trả lại
returned_counts = returned_df.groupby('ProductID')['Quantity'].sum().reset_index()

# Sắp xếp theo số lượng trả lại giảm dần
returned_counts = returned_counts.sort_values(by='Quantity', ascending=False)

# Vẽ biểu đồ cột
plt.figure(figsize=(12, 8))
plt.bar(returned_counts['ProductID'].astype(str), returned_counts['Quantity'], color='skyblue')
plt.xlabel('ProductID')
plt.ylabel('Total Returned Quantity')
plt.title('Total Returned Quantity by ProductID')
plt.xticks(rotation=90)  # Xoay nhãn trục x để dễ đọc hơn
plt.tight_layout()  # Đảm bảo biểu đồ không bị cắt bớt
plt.show()

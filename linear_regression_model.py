import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('sale_table.csv')

# Fill missing values or drop rows with missing values
data = data.dropna()

# Convert categorical variables to dummy variables (one-hot encoding)
data = pd.get_dummies(data, columns=['PaymentMethod', 'OrderStatus'])

# Select features and target variable
features = ['Quantity', 'DiscountApplied', 'SalesRepID']
features.extend([col for col in data.columns if 'PaymentMethod_' in col or 'OrderStatus_' in col])
X = data[features]
y = data['TotalAmount']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Calculate the R-squared value
r2 = r2_score(y_test, y_pred)
print(f'R-squared: {r2}')

# Plot the true vs predicted values
plt.scatter(y_test, y_pred)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.title('True vs Predicted Sales')
plt.show()

def prepare_new_data(new_data, reference_data):
    # Get columns from reference data (X_train)
    reference_columns = reference_data.columns
    
    # Create a DataFrame for the new data with the same columns
    new_data_prepared = pd.DataFrame(columns=reference_columns)
    
    # Fill in the new data values
    for col in new_data.columns:
        if col in new_data_prepared.columns:
            new_data_prepared[col] = new_data[col]
    
    # Fill missing columns with zeros
    new_data_prepared = new_data_prepared.fillna(0).infer_objects(copy=False)
    
    return new_data_prepared

# Example new data
new_data = pd.DataFrame({
    'Quantity': [10],
    'DiscountApplied': [5],
    'SalesRepID': [1],
    'PaymentMethod_CreditCard': [1],
    'PaymentMethod_PayPal': [0],
    'PaymentMethod_BankTransfer': [0],
    'OrderStatus_Completed': [1],
    'OrderStatus_Pending': [0],
    'OrderStatus_Cancelled': [0]
})

# Prepare the new data
new_data_prepared = prepare_new_data(new_data, X_train)

# Predict future sales
predicted_sales = model.predict(new_data_prepared)
print(f'Predicted Sales: {predicted_sales[0]}')

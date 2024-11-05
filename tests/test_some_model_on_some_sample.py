"""
IMPLEMENTATION OF A SIMPLE LINEAR REGRESSION MODEL FOR BOX REVENUE PREDICTION
I DO NOT THINK IT IS WORKING CORRECTLY YET (ANDREA)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


# Identify non-numeric columns to help with debugging
non_numeric_cols = [col for col in X.columns if not np.issubdtype(X[col].dtype, np.number)]
print("Columns with non-numeric types:", non_numeric_cols)

# Drop columns with problematic data types (if necessary)
# If the columns with nested data types are not relevant to your analysis, you can drop them.
X = X.drop(columns=non_numeric_cols)

# Alternatively, if any of these columns are crucial, you may need to further process
# them to extract usable information, depending on the content.



# Target variable
y = df_encoded['box_office_revenue']

# Splitting the data after removing problematic columns
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions and evaluating
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
"""
import xgboost as xgb
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

class GradientBoostingRegressorModel:
    def __init__(self, learning_rate=0.1, n_estimators=100, max_depth=3, random_state=42):
        """
        Initializes the Gradient Boosting Regressor (XGBoost) with common hyperparameters.
        """
        self.model = xgb.XGBRegressor(
            learning_rate=learning_rate,
            n_estimators=n_estimators,
            max_depth=max_depth,
            objective="reg:squarederror",  # Ensures it's a regression model
            random_state=random_state
        )

    def train(self, X_train, y_train):
        """
        Trains the XGBoost model on the training data.
        """
        self.model.fit(X_train, y_train)
    
    def predict(self, X):
        """
        Predicts continuous values for regression using the trained model.
        """
        return self.model.predict(X)

    def evaluate(self, X_test, y_test):
        """
        Evaluates the model using MAE, MSE, and RMSE metrics.
        """
        y_pred = self.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        
        print(f"Mean Absolute Error (MAE): {mae}")
        print(f"Mean Squared Error (MSE): {mse}")
        print(f"Root Mean Squared Error (RMSE): {rmse}")
        
        return {"MAE": mae, "MSE": mse, "RMSE": rmse}

import xgboost as xgb
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

class GradientBoostingRegressorModel:
    def __init__(self, learning_rate=0.1, n_estimators=100, max_depth=3, random_state=42, objective="reg:squarederror"):
        """
        Initializes the Gradient Boosting Regressor (XGBoost) with common hyperparameters.
        
        Args:
            learning_rate (float): Boosting learning rate.
            n_estimators (int): Number of boosting rounds.
            max_depth (int): Maximum depth of a tree.
            random_state (int): Seed for random number generation.
            objective (str): XGBoost objective function, defaulted to 'reg:squarederror' for regression.
        """
        self.model = xgb.XGBRegressor(
            learning_rate=learning_rate,
            n_estimators=n_estimators,
            max_depth=max_depth,
            objective=objective,
            random_state=random_state
        )

    def train(self, X_train, y_train):
        """
        Trains the XGBoost model on the training data.
        
        Args:
            X_train (np.ndarray or pd.DataFrame): Training feature data.
            y_train (np.ndarray or pd.Series): Target variable for training.
        """
        self.model.fit(X_train, y_train)
    
    def predict(self, X):
        """
        Predicts continuous values for regression using the trained model.
        
        Args:
            X (np.ndarray or pd.DataFrame): Feature data for predictions.
        
        Returns:
            np.ndarray: Predicted values.
        """
        return self.model.predict(X)

    def evaluate(self, X_test, y_test):
        """
        Evaluates the model using MAE, MSE, and RMSE metrics.
        
        Args:
            X_test (np.ndarray or pd.DataFrame): Test feature data.
            y_test (np.ndarray or pd.Series): True values for the test set.
        
        Returns:
            dict: Evaluation metrics (MAE, MSE, RMSE).
        """
        y_pred = self.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        
        print(f"Mean Absolute Error (MAE): {mae:.2f}")
        print(f"Mean Squared Error (MSE): {mse:.2f}")
        print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
        
        return {"MAE": mae, "MSE": mse, "RMSE": rmse}

    def get_feature_importance(self):
        """
        Retrieves feature importance from the trained model.
        
        Returns:
            dict: Feature importance scores.
        """
        return self.model.get_booster().get_score(importance_type="weight")
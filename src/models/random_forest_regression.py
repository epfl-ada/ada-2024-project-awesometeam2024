from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

class RandomForestModel:
    def __init__(self, n_estimators=100, max_depth=None, random_state=42):
        """
        Initializes the Random Forest Regressor with specified hyperparameters.
        
        Args:
            n_estimators: Number of trees in the forest.
            max_depth: Maximum depth of the trees. If None, nodes are expanded until all leaves are pure.
            random_state: Seed for random number generation.
        """
        self.model = RandomForestRegressor(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=random_state
        )

    def train(self, X_train, y_train):
        """
        Fits the model to the training data.
        
        Args:
            X_train: Training feature data.
            y_train: Target variable for training.
        """
        self.model.fit(X_train, y_train)
    
    def predict(self, X):
        """
        Predicts continuous values using the trained model.
        
        Args:
            X: Feature data for predictions.
        
        Returns:
            Predicted values.
        """
        return self.model.predict(X)

    def evaluate(self, X_test, y_test):
        """
        Evaluates the model using MAE, MSE, and RMSE metrics.
        
        Args:
            X_test: Test feature data.
            y_test: True values for the test set.
        
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
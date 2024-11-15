from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score


class PredLogisticRegression:
    def __init__(self, C=1.0, max_iter=150, solver='lbfgs', threshold=0.5):
        """
        Initializes the Logistic Regression model.

        Args:
            C (float): Inverse of regularization strength; must be a positive float.
            max_iter (int): Maximum number of iterations for the solver.
            solver (str): Algorithm to use in the optimization problem.
            threshold (float): Probability threshold for binary classification.
        """
        self.model = LogisticRegression(
            C=C,
            max_iter=max_iter,
            solver=solver,
            random_state=42
        )
        self.threshold = threshold

    def train(self, X_train, y_train):
        """
        Fits the model to the training data.

        Args:
            X_train (np.ndarray or pd.DataFrame): Training feature data.
            y_train (np.ndarray or pd.Series): Target variable for training.
        """
        self.model.fit(X_train, y_train)

    def predict(self, X):
        """
        Predicts class labels for samples in X.

        Args:
            X (np.ndarray or pd.DataFrame): Feature data for predictions.

        Returns:
            np.ndarray: Predicted class labels.
        """
        if len(self.model.classes_) == 2:  # Binary classification
            return (self.model.predict_proba(X)[:, 1] >= self.threshold).astype(int)
        else:  # Multiclass classification
            return self.model.predict(X)

    def evaluate(self, y_true, X):
        """
        Evaluates the model's performance and returns accuracy, precision, recall, and F1 score.

        Args:
            y_true (np.ndarray or pd.Series): True class labels.
            X (np.ndarray or pd.DataFrame): Feature data for evaluation.

        Returns:
            dict: Evaluation metrics (Accuracy, Precision, Recall, F1 Score).
        """
        y_pred = self.predict(X)
        precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
        recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
        accuracy = accuracy_score(y_true, y_pred)

        print("Evaluation Metrics:")
        print(f"  Accuracy: {accuracy:.2f}")
        print(f"  Precision: {precision:.2f}")
        print(f"  Recall: {recall:.2f}")
        print(f"  F1 Score: {f1:.2f}")

        return {"Accuracy": accuracy, "Precision": precision, "Recall": recall, "F1 Score": f1}
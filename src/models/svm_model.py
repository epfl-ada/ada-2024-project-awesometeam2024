from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

class SVMModel:
    def __init__(self, kernel='rbf', C=1.0, gamma='scale', threshold=0.5):
        """
        Initializes the SVM model for classification.
        
        Args:
            kernel (str): Kernel type to be used in the algorithm ('linear', 'rbf', 'poly', etc.).
            C (float): Regularization parameter.
            gamma (str or float): Kernel coefficient for 'rbf', 'poly', and 'sigmoid'.
            threshold (float): Probability threshold for binary classification.
        """
        self.model = SVC(kernel=kernel, C=C, gamma=gamma, probability=True, random_state=42)
        self.threshold = threshold

    def train(self, X_train, y_train):
        """
        Trains the SVM model.
        
        Args:
            X_train (np.ndarray or pd.DataFrame): Training feature data.
            y_train (np.ndarray or pd.Series): Training target labels.
        """
        self.model.fit(X_train, y_train)

    def predict(self, X):
        """
        Predicts binary labels for given feature data.
        
        Args:
            X (np.ndarray or pd.DataFrame): Feature data for predictions.
        
        Returns:
            np.ndarray: Predicted binary labels.
        """
        pred_probs = self.model.predict_proba(X)[:, 1]
        return (pred_probs >= self.threshold).astype(int)

    def evaluate(self, y_true, X):
        """
        Evaluates the SVM model on given data and prints evaluation metrics.
        
        Args:
            y_true (np.ndarray or pd.Series): True labels.
            X (np.ndarray or pd.DataFrame): Feature data to evaluate.
        
        Returns:
            dict: Dictionary of evaluation metrics (Accuracy, Precision, Recall, F1 Score).
        """
        y_pred = self.predict(X)

        # Calculate metrics
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred, average='weighted')
        recall = recall_score(y_true, y_pred, average='weighted')
        f1 = f1_score(y_true, y_pred, average='weighted')

        # Print metrics
        print("Evaluation Metrics:")
        print(f"  Accuracy: {accuracy:.2f}")
        print(f"  Precision: {precision:.2f}")
        print(f"  Recall: {recall:.2f}")
        print(f"  F1 Score: {f1:.2f}")

        # Confusion Matrix and Classification Report
        print("\nConfusion Matrix:")
        print(confusion_matrix(y_true, y_pred))
        print("\nClassification Report:")
        print(classification_report(y_true, y_pred))

        return {"Accuracy": accuracy, "Precision": precision, "Recall": recall, "F1 Score": f1}
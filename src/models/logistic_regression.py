from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score

class SklearnLogisticRegression:
    def __init__(self, C=1.0, max_iter=150, solver='lbfgs'):
        """Initializes the Logistic Regression model with sklearn's LogisticRegression."""
        self.model = LogisticRegression(C=C, max_iter=max_iter, solver=solver, random_state=42)

    def train(self, X_train, y_train):
        """Fits the model to the training data."""
        self.model.fit(X_train, y_train)

    def predict(self, X):
        """Predicts class labels for samples in X."""
        return self.model.predict(X)

    def evaluate(self, y_true, X):
        """Evaluates the model and returns precision, recall, and F1 score."""
        y_pred = self.predict(X)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        return {"Precision": precision, "Recall": recall, "F1 Score": f1}

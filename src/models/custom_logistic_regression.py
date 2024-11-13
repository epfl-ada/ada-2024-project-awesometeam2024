import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score

class CustomLogisticRegression:
    def __init__(self, gamma=0.1, lambda_=0.01, max_iters=150, threshold=1e-8):
        """Initializes hyperparameters for logistic regression."""
        self.gamma = gamma
        self.lambda_ = lambda_
        self.max_iters = max_iters
        self.threshold = threshold
        self.w = None

    def sigmoid(self, t):
        """Applies the sigmoid function element-wise."""
        return 1 / (1 + np.exp(-t))

    def calculate_gradient(self, y, tx):
        """Calculates the gradient for logistic regression with regularization."""
        pred = self.sigmoid(tx.dot(self.w))
        grad = tx.T.dot(pred - y) / y.shape[0]
        grad[1:] += self.lambda_ * self.w[1:]  # Regularize, excluding bias term
        return grad

    def predict(self, tx):
        """Generates binary predictions based on probability threshold 0.5."""
        pred_prob = self.sigmoid(tx.dot(self.w))
        return np.where(pred_prob >= 0.5, 1, 0)

    def calculate_loss(self, y, tx):
        """Calculates logistic loss with regularization."""
        pred = self.sigmoid(tx.dot(self.w))
        regularization = (self.lambda_ / 2) * np.sum(self.w[1:]**2)
        loss = -np.mean(y * np.log(pred + 1e-15) + (1 - y) * np.log(1 - pred + 1e-15)) + regularization
        return loss

    def fit(self, y_train, x_train, y_val, x_val):
        """Trains logistic regression using penalized gradient descent."""
        tx_train = np.c_[np.ones((x_train.shape[0], 1)), x_train]
        tx_val = np.c_[np.ones((x_val.shape[0], 1)), x_val]
        self.w = np.zeros((tx_train.shape[1], 1))
        f1_best = 0
        best_weights = self.w.copy()
        
        for _ in range(self.max_iters):
            loss = self.calculate_loss(y_train, tx_train)
            grad = self.calculate_gradient(y_train, tx_train)
            self.w -= self.gamma * grad

            # Validation performance
            y_val_pred = self.predict(tx_val)
            _, _, f1_score_val = precision_score(y_val, y_val_pred), recall_score(y_val, y_val_pred), f1_score(y_val, y_val_pred)
            if f1_score_val > f1_best:
                best_weights = self.w.copy()
                f1_best = f1_score_val

            # Check for convergence
            if np.linalg.norm(grad) < self.threshold:
                break
        
        self.w = best_weights  # Store best weights
        print(f"Best F1-score: {f1_best}")
        return f1_best

    def evaluate(self, y, tx):
        """Evaluates the model and returns precision, recall, and F1 score."""
        y_pred = self.predict(tx)
        precision = precision_score(y, y_pred)
        recall = recall_score(y, y_pred)
        f1 = f1_score(y, y_pred)
        return {"Precision": precision, "Recall": recall, "F1 Score": f1}
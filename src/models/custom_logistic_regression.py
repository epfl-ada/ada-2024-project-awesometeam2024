import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

class CustomLogisticRegression:
    def __init__(self, gamma=0.1, lambda_=0.01, max_iters=150, convergence_threshold=1e-8, threshold=0.5):
        """
        Initializes the Custom Logistic Regression model with gradient descent.

        Args:
            gamma (float): Learning rate for gradient descent.
            lambda_ (float): Regularization strength.
            max_iters (int): Maximum number of iterations for gradient descent.
            convergence_threshold (float): Threshold for convergence.
            threshold (float): Probability threshold for binary classification.
        """
        self.gamma = gamma
        self.lambda_ = lambda_
        self.max_iters = max_iters
        self.convergence_threshold = convergence_threshold
        self.threshold = threshold
        self.w = None

    def sigmoid(self, t):
        """Applies the sigmoid function element-wise."""
        return 1 / (1 + np.exp(-t))

    def calculate_gradient(self, y, tx):
        """
        Calculates the gradient for logistic regression with L2 regularization.
        
        Args:
            y (np.ndarray): Target values.
            tx (np.ndarray): Feature matrix with bias term.

        Returns:
            np.ndarray: Computed gradient vector.
        """
        pred = self.sigmoid(tx.dot(self.w))
        grad = tx.T.dot(pred - y) / y.shape[0]
        grad[1:] += self.lambda_ * self.w[1:]  # Exclude bias term from regularization
        return grad

    def calculate_loss(self, y, tx):
        """
        Computes the logistic loss with L2 regularization.
        
        Args:
            y (np.ndarray): Target values.
            tx (np.ndarray): Feature matrix with bias term.

        Returns:
            float: Computed loss value.
        """
        pred = self.sigmoid(tx.dot(self.w))
        regularization = (self.lambda_ / 2) * np.sum(self.w[1:] ** 2)
        loss = -np.mean(y * np.log(pred + 1e-15) + (1 - y) * np.log(1 - pred + 1e-15)) + regularization
        return loss

    def fit(self, y_train, x_train, y_val, x_val):
        """
        Trains logistic regression using gradient descent and tracks best F1 score on validation set.

        Args:
            y_train (np.ndarray): Training target values.
            x_train (np.ndarray): Training feature matrix.
            y_val (np.ndarray): Validation target values.
            x_val (np.ndarray): Validation feature matrix.

        Returns:
            float: Best F1 score obtained during training.
        """
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
            f1_score_val = f1_score(y_val, y_val_pred, average='weighted')
            if f1_score_val > f1_best:
                best_weights = self.w.copy()
                f1_best = f1_score_val

            # Check for convergence
            if np.linalg.norm(grad) < self.convergence_threshold:
                break
        
        self.w = best_weights  # Store best weights
        print(f"Best F1-score on validation set: {f1_best:.2f}")
        return f1_best

    def predict(self, tx):
        """
        Predicts binary labels based on the set probability threshold.

        Args:
            tx (np.ndarray): Feature matrix for predictions with bias term.

        Returns:
            np.ndarray: Predicted binary class labels.
        """
        pred_prob = self.sigmoid(tx.dot(self.w))
        return (pred_prob >= self.threshold).astype(int)

    def evaluate(self, y_true, tx):
        """
        Evaluates the model's performance with accuracy, precision, recall, and F1 score.
        
        Args:
            y_true (np.ndarray): True target values.
            tx (np.ndarray): Feature matrix for evaluation.

        Returns:
            dict: Evaluation metrics.
        """
        y_pred = self.predict(tx)
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred, average='weighted')
        recall = recall_score(y_true, y_pred, average='weighted')
        f1 = f1_score(y_true, y_pred, average='weighted')

        print(f"Accuracy: {accuracy:.2f}")
        print(f"Precision: {precision:.2f}")
        print(f"Recall: {recall:.2f}")
        print(f"F1 Score: {f1:.2f}")

        return {"Accuracy": accuracy, "Precision": precision, "Recall": recall, "F1 Score": f1}
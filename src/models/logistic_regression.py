from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import numpy as np
from sklearn.metrics import confusion_matrix, precision_recall_curve, roc_curve, auc, precision_score, recall_score, f1_score, accuracy_score
import plotly.graph_objects as go



class PredLogisticRegression:
    def __init__(self, C=1.0, max_iter=150, solver='lbfgs', threshold=0.5):
        """
        Initializes the Logistic Regression model.

        Args:
            C: Inverse of regularization strength; must be a positive float.
            max_iter: Maximum number of iterations for the solver.
            solver: Algorithm to use in the optimization problem.
            threshold: Probability threshold for binary classification.
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
            X_train: Training feature data.
            y_train: Target variable for training.
        """
        self.model.fit(X_train, y_train)

    def predict(self, X):
        """
        Predicts class labels for samples in X.

        Args:
            X Feature data for predictions.

        Returns:
            Predicted class labels.
        """
        if len(self.model.classes_) == 2:  # Binary classification
            return (self.model.predict_proba(X)[:, 1] >= self.threshold).astype(int)
        else:  # Multiclass classification
            return self.model.predict(X)

    def evaluate(self, y_true, X):
        """
        Evaluates the model's performance and returns accuracy, precision, recall, and F1 score.

        Args:
            y_true: True class labels.
            X: Feature data for evaluation.

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
    
    def plot_confusion_matrix_plotly(self, y_true, X,  file_name=None):
        """
        Generates an interactive confusion matrix using Plotly.

        Args:
            y_true: True class labels.
            X: Feature data for evaluation.
            model: Trained model to predict on X.
        """
        y_pred = self.predict(X)
        cm = confusion_matrix(y_true, y_pred)
        
        labels = [str(label) for label in self.model.classes_]
        z_text = [[str(val) for val in row] for row in cm]

        fig = ff.create_annotated_heatmap(
            z=cm,
            x=labels,
            y=labels,
            annotation_text=z_text,
            colorscale="Viridis"
        )

        fig.update_layout(
            title_text="Confusion Matrix",
            xaxis_title="Predicted",
            yaxis_title="Actual",
            margin=dict(t=50, l=50),
            font=dict(size=12)
        )
        if file_name:
            fig.write_html(file_name)
        fig.show()

    def plot_precision_recall_curve_plotly(self, y_true, X, file_name=None):
        """
        Generates an interactive precision-recall curve using Plotly.

        Args:
            y_true: True class labels.
            X: Feature data for evaluation.
            model: Trained model to predict probabilities on X.
        """
        probabilities = self.model.predict_proba(X)[:, 1]
        precision, recall, _ = precision_recall_curve(y_true, probabilities)

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=recall, y=precision, mode='lines', name='Precision-Recall Curve'))
        fig.update_layout(
            title="Precision-Recall Curve",
            xaxis_title="Recall",
            yaxis_title="Precision",
            font=dict(size=12),
            margin=dict(t=50, l=50)
        )
        if file_name:
            fig.write_html(file_name)
        fig.show()

    def plot_roc_curve_plotly(self, y_true, X, file_name=None):
        """
        Generates an interactive ROC curve using Plotly.

        Args:
            y_true: True class labels.
            X: Feature data for evaluation.
            model: Trained model to predict probabilities on X.
        """
        probabilities = self.model.predict_proba(X)[:, 1]
        fpr, tpr, _ = roc_curve(y_true, probabilities)
        roc_auc = auc(fpr, tpr)

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=fpr, y=tpr, mode='lines', name=f'ROC Curve (AUC = {roc_auc:.2f})'))
        fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines', name='Random Guess', line=dict(dash='dash')))

        fig.update_layout(
            title="Receiver Operating Characteristic (ROC) Curve",
            xaxis_title="False Positive Rate",
            yaxis_title="True Positive Rate",
            font=dict(size=12),
            margin=dict(t=50, l=50)
        )
        if file_name:
            fig.write_html(file_name)
        fig.show()


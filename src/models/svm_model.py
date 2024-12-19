from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix, roc_curve, auc
import plotly.figure_factory as ff
import plotly.graph_objects as go

class SVMModel:
    def __init__(self, kernel='rbf', C=1.0, gamma='scale', threshold=0.5):
        """
        Initializes the SVM model for classification.
        
        Args:
            kernel: Kernel type to be used in the algorithm ('linear', 'rbf', 'poly', etc.).
            C: Regularization parameter.
            gamma: Kernel coefficient for 'rbf', 'poly', and 'sigmoid'.
            threshold: Probability threshold for binary classification.
        """
        self.model = SVC(kernel=kernel, C=C, gamma=gamma, probability=True, random_state=42)
        self.threshold = threshold

    def train(self, X_train, y_train):
        """
        Trains the SVM model.
        
        Args:
            X_train: Training feature data.
            y_train: Training target labels.
        """
        self.model.fit(X_train, y_train)

    def predict(self, X):
        """
        Predicts binary labels for given feature data.
        
        Args:
            X: Feature data for predictions.
        
        Returns:
            Predicted binary labels.
        """
        pred_probs = self.model.predict_proba(X)[:, 1]
        return (pred_probs >= self.threshold).astype(int)

    def evaluate(self, y_true, X):
        """
        Evaluates the SVM model on given data and prints evaluation metrics.
        
        Args:
            y_true: True labels.
            X: Feature data to evaluate.
        
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
    
    def plot_confusion_matrix_plotly(self, y_true, X, file_name=None):
        """
        Generates an interactive confusion matrix using Plotly and optionally saves it as an HTML file.

        Args:
            y_true: True class labels.
            X: Feature data for evaluation.
            model: Trained model to predict on X.
            file_name: (Optional) File name to save the HTML plot.
        """
        y_pred = self.predict(X)
        cm = confusion_matrix(y_true, y_pred)

        labels = ["Non-Success", "Success"]
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


    def plot_roc_curve_plotly(self, y_true, X, file_name=None):
        """
        Generates an interactive ROC curve using Plotly and optionally saves it as an HTML file.

        Args:
            y_true: True class labels.
            X: Feature data for evaluation.
            model: Trained model to predict probabilities on X.
            file_name: (Optional) File name to save the HTML plot.
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

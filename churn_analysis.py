from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_churn_model(X_train, y_train, X_test, y_test):
    """
    Train a Random Forest model for churn prediction.
    Args:
        X_train (DataFrame): Training features.
        y_train (Series): Training labels.
        X_test (DataFrame): Testing features.
        y_test (Series): Testing labels.
    Returns:
        model (RandomForestClassifier): Trained model.
        report (str): Classification report.
    """
    # Train Random Forest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    return model, report

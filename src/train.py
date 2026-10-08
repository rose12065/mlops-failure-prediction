from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os


failure_mode = os.getenv("FAILURE_MODE", "none")

if failure_mode == "training":
    raise RuntimeError("Controlled training failure for experiment")


# Load dataset
data = load_iris()

X = data.data
y = data.target


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train model
model.fit(X_train, y_train)


# Make predictions
predictions = model.predict(X_test)


# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)


# Create models directory if it does not exist
os.makedirs("models", exist_ok=True)


# Save trained model
joblib.dump(model, "models/model.pkl")

print("Model saved successfully.")
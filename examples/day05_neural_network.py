"""Ngày 5: MLP đơn giản trên chữ số viết tay; không cần GPU."""
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
for units in (32, 64):
    model = make_pipeline(
        StandardScaler(),
        MLPClassifier(hidden_layer_sizes=(units,), max_iter=500, random_state=42)
    )
    model.fit(X_train, y_train)
    result = accuracy_score(y_test, model.predict(X_test))
    print(f'Hidden units: {units}; test accuracy: {result:.3f}')

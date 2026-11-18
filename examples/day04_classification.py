"""Ngày 4: Baseline vs ML. Cài đặt scikit-learn nếu Colab chưa có."""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
models = {
    'Baseline': DummyClassifier(strategy='most_frequent'),
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
}
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print('\n', name, 'accuracy:', round(accuracy_score(y_test, predictions), 3))
    print('Confusion matrix:\n', confusion_matrix(y_test, predictions))

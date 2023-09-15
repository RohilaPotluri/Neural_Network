import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

# importing the glass csv file
df = pd.read_csv('glass.csv')
X_train, X_test, Y_train, Y_test = train_test_split(df.drop("Type", axis=1), df["Type"], test_size=0.2)

# train model using the Naive_bayes
model = GaussianNB()
model.fit(X_train, Y_train)

# evaluating the model
score = model.score(X_test, Y_test)
print('Accuracy: %.3f' % score)

# generating the classification report
y_pred = model.predict(X_test)
report = classification_report(y_true=Y_test, y_pred=y_pred)
print(report)
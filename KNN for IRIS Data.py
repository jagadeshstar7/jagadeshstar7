##importing the necessary packages for the model
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#downloading iris data
iris = pd.read_csv("IRIS.csv")

iris.head()
iris.tail()
iris.isnull().sum()
iris.info()
iris.describe()

#seperating input and target
X = iris.iloc[:,:-1].values#to get only values without coloum names
Y = iris.iloc[:,-1].values

#train and test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,Y,train_size =0.8,test_size =  0.2,random_state = 0)

#preprocessing
from sklearn.preprocessing import MinMaxScaler
Scaler = MinMaxScaler()
Scaler.fit(x_train)

x_train = Scaler.transform(x_train)
x_test = Scaler.transform(x_test)

x_train.shape

from sklearn.neighbors import KNeighborsClassifier
Knn = KNeighborsClassifier(n_neighbors = 10)
Knn.fit(x_train,y_train)
y_pred = Knn.predict(x_test)


from sklearn.metrics import accuracy_score,confusion_matrix
cm = confusion_matrix(y_pred,y_test)
print(cm)

Accuracy = accuracy_score(y_pred,y_test)*100
print(Accuracy)


error = []

for i in range(1,119):
    Knn = KNeighborsClassifier(n_neighbors = i)
    Knn.fit(x_train,y_train)
    y_pred_i = Knn.predict(x_test)
    error.append(np.mean(y_pred_i != y_test))

plt.figure(figsize=(10, 5))   
plt.plot(range(1,119),error)
plt.title("Error Rate")
plt.xlabel("Jack")
plt.ylabel("Jandu")
plt.xlim(0,30)#for axis range


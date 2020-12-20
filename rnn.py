import numpy as np
import math
from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

def Angulos_a_posicion(cantidad):
    theta1=[]
    theta2=[]
    theta3=[]
    i=[]
    j=[]
    k=[]
    a=1
    while a <= cantidad:
        valor= np.random.uniform(-90,90)
        a+=1
        theta1.append(valor)
    a=1
    while a <= cantidad:
        valor= np.random.uniform(-90,90)
        a+=1
        theta2.append(valor)
    a=1
    while a <= cantidad:
        valor= np.random.uniform(-90,90)
        a+=1
        theta3.append(valor)
        
    for a,b,c in zip(theta1,theta2,theta3):
        valorx= 80*(math.cos(5*b/12)+math.cos(5*c/12))
        i.append(valorx)
        valory=80*(math.cos(5*b/12)+math.cos(5*c/12))*math.sin(21*a/40)
        j.append(valory)
        valorz=80*(math.sin(5*b/12)+math.sin(5*c/12))
        k.append(valorz)
    X=[theta1,theta2,theta3]
    y=[i,j,k]
    return X , y

X , y= Angulos_a_posicion(200)
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=42)
regr = MLPRegressor(random_state=42, max_iter=500).fit(X_train, y_train)
print(regr.predict(y_test[:2]))

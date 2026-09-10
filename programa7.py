#pip install scikit-learn

from sklearn.linear_model import LinearRegression

X = [[50], [70], [100], [150]]
y = [250, 350, 500, 750]

modelo = LinearRegression()

modelo.fit(X, y)

previsao = modelo.predict([[120]])

print(previsao)

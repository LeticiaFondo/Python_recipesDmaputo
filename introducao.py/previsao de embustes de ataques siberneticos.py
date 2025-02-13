import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Passo 1: Dados de exemplo
# Tempo de chamadas (em minutos) e valor monetário (em USD)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500, 600])

# Passo 2: Visualizar dados aleatórios de pessoas que já viveram situações similares
num_pessoas = np.random.randint(50, 100)
pessoas_similares = np.random.rand(num_pessoas) * 10  # Tempo aleatório em chamadas
plt.hist(pessoas_similares, bins=10, alpha=0.5, color='blue')
plt.title('Distribuição de Pessoas que Sofreram Ataques Cibernéticos')
plt.xlabel('Tempo em Chamadas (min)')
plt.ylabel('Número de Pessoas')
plt.show()

# Passo 3: Tipos de ataques cibernéticos mais usados (dados fictícios)
tipos_ataques = ['Phishing', 'Vishing', 'Smishing', 'Spoofing']
frequencias = [40, 30, 20, 10]  # Frequência fictícia

plt.bar(tipos_ataques, frequencias, color='orange')
plt.title('Tipos de Ataques Cibernéticos em Moçambique')
plt.xlabel('Tipo de Ataque')
plt.ylabel('Frequência')
plt.show()

# Passo 4: Treinamento do modelo
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(x_poly, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Passo 5: Exibir o conjunto de treinamento
print("Conjunto de Treinamento (X):")
print(X_train)
print("Conjunto de Treinamento (Y):")
print(y_train)

# Passo 6: Exibir o conjunto de testes
print("Conjunto de Testes (X):")
print(X_test)
print("Conjunto de Testes (Y):")
print(y_test)

# Passo 7: Ajustar o conjunto de dados
y_pred = model.predict(X_test)

# Passo 8: Verifique a relação R² do modelo
r2 = r2_score(y_test, y_pred)
print(f"R² do modelo: {r2:.2f}")

# Passo 9: Previsão futura
tempo_futuro = np.array([[11], [12], [13]]).reshape(-1, 1)  # Novos tempos
tempo_futuro_poly = poly.transform(tempo_futuro)
predicoes_futuras = model.predict(tempo_futuro_poly)
print("Predições futuras para valores monetários:")
print(predicoes_futuras)

# Visualização do ajuste
plt.scatter(x, y, color='red', label='Dados reais')
plt.scatter(X_test[:, 1], y_pred, color='blue', label='Predições')
plt.title('Ajuste do Modelo de Regressão Polinomial')
plt.xlabel('Tempo em Chamadas (min)')
plt.ylabel('Valor Monetário (USD)')
plt.legend()
plt.show()

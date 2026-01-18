import pandas as pd
import matplotlib.pyplot as plt

# 문턱 전압 (가정)
Vth = 1.2

# 데이터 로드
data = pd.read_csv("../data/IdVgs_measured.csv")

# Vgs > Vth 구간만 추출
on_region = data[data["Vgs"] > Vth]

# (Vgs - Vth)^2 계산
x = (on_region["Vgs"] - Vth) ** 2
y = on_region["Id"]

# 그래프
plt.figure()
plt.plot(x, y, marker='o')
plt.xlabel("(Vgs - Vth)^2")
plt.ylabel("Id")
plt.title("Id vs (Vgs - Vth)^2")
plt.grid(True)
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
data = pd.read_csv('data/IdVgs_measured.csv')

Vgs = data['Vgs'].values
Id  = data['Id'].values

# gm 계산 (수치 미분)
gm = np.gradient(Id, Vgs)

# 그래프
plt.figure()
plt.plot(Vgs, gm)
plt.xlabel('Vgs (V)')
plt.ylabel('gm (S)')
plt.title('Transconductance gm vs Vgs')
plt.grid()
plt.show()


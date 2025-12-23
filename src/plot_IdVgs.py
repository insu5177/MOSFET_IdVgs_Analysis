import pandas as pd
import matplotlib.pyplot as plt

# Load Id-Vgs data
data = pd.read_csv("data/IdVgs_measured.csv")

Vgs = data["Vgs"]
Id = data["Id"]

# Plot Id-Vgs curve
plt.figure()
plt.plot(Vgs, Id, marker='o')
plt.xlabel("Vgs (V)")
plt.ylabel("Id (mA)")
plt.title("MOSFET Id-Vgs Characteristic")
plt.grid(True)
plt.show()

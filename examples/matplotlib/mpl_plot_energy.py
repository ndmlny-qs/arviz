"""
Energy Plot
===========
"""
import matplotlib.pyplot as plt

import arviz as az

az.style.use("arviz-darkgrid")

data = az.load_arviz_data("centered_eight")
az.plot_energy(data, figsize=(12, 8))

plt.show()

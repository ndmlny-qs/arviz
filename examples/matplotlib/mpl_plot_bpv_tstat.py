"""
Bayesian p-value with T statistic Plot
======================================
"""
import matplotlib.pyplot as plt

import arviz as az

az.style.use("arviz-darkgrid")

data = az.load_arviz_data("regression1d")
az.plot_bpv(data, kind="t_stat", t_stat="0.5")

plt.show()

"""
Posterior Predictive Check Cumulative Plot
==========================================
"""
import matplotlib.pyplot as plt

import arviz as az

az.style.use("arviz-darkgrid")

data = az.load_arviz_data("non_centered_eight")
az.plot_ppc(data, alpha=0.3, kind="cumulative", figsize=(12, 6), textsize=14)

plt.show()

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from transep import transep

# set base path for input and output files, figures and observations
base_path = Path(__file__).parent
base_path_figs = base_path / "figures"
base_path_input = base_path / "input"
base_path_output = base_path / "output"
base_path_obs = base_path / "observations"

# load input data
file = base_path_input / 'd18O_in_mod.csv'
df_in_mod = pd.read_csv(file, sep="\t", skiprows=0, na_values=-9999,
                     parse_dates=True, index_col=0)
df_in_mod.index = pd.to_datetime(df_in_mod.index)
input_mod = df_in_mod['d18O'].bfill().ffill().values

# time steps
t = np.arange(1, len(input_mod) + 1)

# simulate with dispersion transfer function
output = transep.simulate(input_mod, transep.dispersion_function, 1, p_d=0.1, mtt=100)
output1 = transep.simulate_explicit(input_mod, transep.dispersion_function, 1, p_d=0.1, mtt=100)
df_output = pd.DataFrame(output, index=df_in_mod.index, columns=['d18O'])
df_output.columns = [
    ["per mille"],
    ["d18O"],
]
# write output to csv
file = base_path_output / "oxygen18_time_series_dispersion.csv"
df_output.to_csv(file, sep=";")

# simulate with exponential piston function
output = transep.simulate(input_mod, transep.exponential_piston_function, 1, mtt=10, eta=0.1)
output1 = transep.simulate_explicit(input_mod, transep.exponential_piston_function, 1, mtt=10, eta=0.1)
df_output = pd.DataFrame(output, index=df_in_mod.index, columns=['d18O'])
df_output.columns = [
    ["per mille"],
    ["d18O"],
]
# write output to csv
file = base_path_output / "oxygen18_time_series_exponential_piston.csv"
df_output.to_csv(file, sep=";")

# simulate with gamma transfer function
output = transep.simulate(input_mod, transep.gamma_function, 1, alpha=1, beta=10)
output1 = transep.simulate_explicit(input_mod, transep.gamma_function, 1, alpha=1, beta=10)
df_output = pd.DataFrame(output, index=df_in_mod.index, columns=['d18O'])
df_output.columns = [
    ["per mille"],
    ["d18O"],
]
# write output to csv
file = base_path_output / "oxygen18_time_series_gamma.csv"
df_output.to_csv(file, sep=";")

# simulate with linear reservoir transfer function
output = transep.simulate(input_mod, transep.linear_reservoir_function, 1, mtt=40)
output1 = transep.simulate_explicit(input_mod, transep.linear_reservoir_function, 1, mtt=40)
df_output = pd.DataFrame(output, index=df_in_mod.index, columns=['d18O'])
df_output.columns = [
    ["per mille"],
    ["d18O"],
]
# write output to csv
file = base_path_output / "oxygen18_time_series_linear_reservoir.csv"
df_output.to_csv(file, sep=";")

# simlate with parallel linear reservoir transfer function
output = transep.simulate(input_mod, transep.parallel_linear_reservoir_function, 1, mtt_slow=100, mtt_fast=10, frac_fast=0.1)
output1 = transep.simulate(input_mod, transep.parallel_linear_reservoir_function, 1, mtt_slow=100, mtt_fast=10, frac_fast=0.1)
df_output = pd.DataFrame(output, index=df_in_mod.index, columns=['d18O'])
df_output.columns = [
    ["per mille"],
    ["d18O"],
]
# write output to csv
file = base_path_output / "oxygen18_time_series_parallel_linear_reservoir.csv"
df_output.to_csv(file, sep=";")
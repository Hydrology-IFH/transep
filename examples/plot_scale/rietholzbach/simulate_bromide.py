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

# time steps
t = np.arange(1, 401)
years = np.arange(1997, 2007).tolist()
# generate input data
file = base_path_input / 'PRECIP.csv'
df_prec = pd.read_csv(file, sep="\t", skiprows=0, na_values=-9999,
                     parse_dates=True, index_col=0)
df_prec.index = pd.to_datetime(df_prec.index)

for year in years:
    # generate bromide input data
    df_prec_year = df_prec.loc[str(year):str(year+1)]
    df_in = pd.DataFrame(index=t, columns=['Br'])
    df_in['Br'] = 0.0
    i = 1
    # leaching into soil after 20 mm of rainfall
    while np.sum(df_prec_year.iloc[313:313+i, 0].values) <= 20:
        i += 1
    # add bromide injection
    df_in.iloc[:i, 0] = 25446/np.sum(df_prec_year.iloc[313:313+i, 0].values)
    cond = (df_prec_year.iloc[313:313+400, 0].values <= 0)
    df_in.loc[cond, 'Br'] = 0.0
    input = df_in['Br'].values
    df_in.columns = [
        ["mg/l"],
        ["Br"],
    ]
    df_in.to_csv(base_path_input / f"bromide_in_{year}.csv", sep=";")

    # simulate with dispersion transfer function
    output = transep.simulate(input, transep.dispersion_function, 1, p_d=0.1, mtt=100)
    output = output / 79.904  # convert from mg/l to mmol/l
    output1 = transep.simulate_explicit(input, transep.dispersion_function, 1, p_d=0.1, mtt=100)
    df_output = pd.DataFrame(output, index=df_in.index, columns=['Br'])
    df_output.columns = [
        ["mmol/l"],
        ["Br"],
    ]
    # write output to csv
    file = base_path_output / f"bromide_time_series_dispersion_{year}.csv"
    df_output.to_csv(file, sep=";")

    # simulate with exponential piston function
    output = transep.simulate(input, transep.exponential_piston_function, 1, mtt=10, eta=0.1)
    output = output / 79.904  # convert from mg/l to mmol/l
    output1 = transep.simulate_explicit(input, transep.exponential_piston_function, 1, mtt=10, eta=0.1)
    df_output = pd.DataFrame(output, index=df_in.index, columns=['Br'])
    df_output.columns = [
        ["mmol/l"],
        ["Br"],
    ]
    # write output to csv
    file = base_path_output / f"bromide_time_series_exponential_piston_{year}.csv"
    df_output.to_csv(file, sep=";")

    # simulate with gamma transfer function
    output = transep.simulate(input, transep.gamma_function, 1, alpha=1, beta=10)
    output = output / 79.904  # convert from mg/l to mmol/l
    output1 = transep.simulate_explicit(input, transep.gamma_function, 1, alpha=1, beta=10)
    df_output = pd.DataFrame(output, index=df_in.index, columns=['Br'])
    df_output.columns = [
        ["mmol/l"],
        ["Br"],
    ]
    # write output to csv
    file = base_path_output / f"bromide_time_series_gamma_{year}.csv"
    df_output.to_csv(file, sep=";")

    # simulate with linear reservoir transfer function
    output = transep.simulate(input, transep.linear_reservoir_function, 1, mtt=40)
    output = output / 79.904  # convert from mg/l to mmol/l
    output1 = transep.simulate_explicit(input, transep.linear_reservoir_function, 1, mtt=40)
    df_output = pd.DataFrame(output, index=df_in.index, columns=['Br'])
    df_output.columns = [
        ["mmol/l"],
        ["Br"],
    ]
    # write output to csv
    file = base_path_output / f"bromide_time_series_linear_reservoir_{year}.csv"
    df_output.to_csv(file, sep=";")

    # simlate with parallel linear reservoir transfer function
    output = transep.simulate(input, transep.parallel_linear_reservoir_function, 1, mtt_slow=100, mtt_fast=10, frac_fast=0.1)
    output = output / 79.904  # convert from mg/l to mmol/l
    output1 = transep.simulate(input, transep.parallel_linear_reservoir_function, 1, mtt_slow=100, mtt_fast=10, frac_fast=0.1)
    df_output = pd.DataFrame(output, index=df_in.index, columns=['Br'])
    df_output.columns = [
        ["mmol/l"],
        ["Br"],
    ]
    # write output to csv
    file = base_path_output / f"bromide_time_series_parallel_linear_reservoir_{year}.csv"
    df_output.to_csv(file, sep=";")
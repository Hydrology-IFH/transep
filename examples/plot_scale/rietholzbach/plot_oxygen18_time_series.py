from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

mpl.use("agg")
import matplotlib.pyplot as plt  # noqa: E402

mpl.rcParams["font.size"] = 8
mpl.rcParams["axes.titlesize"] = 8
mpl.rcParams["axes.labelsize"] = 9
mpl.rcParams["xtick.labelsize"] = 8
mpl.rcParams["ytick.labelsize"] = 8
mpl.rcParams["legend.fontsize"] = 8
mpl.rcParams["legend.title_fontsize"] = 8
sns.set_style("ticks")
sns.plotting_context(
    "paper",
    font_scale=1,
    rc={
        "font.size": 8.0,
        "axes.labelsize": 9.0,
        "axes.titlesize": 8.0,
        "xtick.labelsize": 8.0,
        "ytick.labelsize": 8.0,
        "legend.fontsize": 8.0,
        "legend.title_fontsize": 8.0,
    },
)


# set base path for input and output files, figures and observations
base_path = Path(__file__).parent
base_path_figs = base_path / "figures"
base_path_input = base_path / "input"
base_path_output = base_path / "output"
base_path_obs = base_path / "observations"

# load input data
file = base_path_input / 'd18O_in.csv'
df_in = pd.read_csv(file, sep="\t", skiprows=0, na_values=-9999,
                     parse_dates=True, index_col=0)
df_in.index = pd.to_datetime(df_in.index)
input = df_in['d18O'].fillna(0).values

file = base_path_input / 'PRECIP.csv'
df_prec = pd.read_csv(file, sep="\t", skiprows=0, na_values=-9999,
                     parse_dates=True, index_col=0)
df_prec.index = pd.to_datetime(df_prec.index)
input_prec = df_in.loc[df_prec['PREC'] > 0, 'd18O'].bfill().fillna(0).values

file = base_path_input / 'd18O_in_mod.csv'
df_in_mod = pd.read_csv(file, sep="\t", skiprows=0, na_values=-9999,
                     parse_dates=True, index_col=0)
df_in_mod.index = pd.to_datetime(df_in_mod.index)
input_mod = df_in_mod['d18O'].fillna(0).values

# load observations
file = base_path_obs / 'd18O_out.csv'
df_obs = pd.read_csv(file, sep="\t", skiprows=0, na_values=-9999,
                     parse_dates=True, index_col=0)
df_obs.index = pd.to_datetime(df_obs.index)
arr_obs = df_obs['d18O'].values

# time steps
t = np.arange(1, len(input) + 1)

models = ["dispersion", "exponential_piston", "gamma", "linear_reservoir", "parallel_linear_reservoir"]
for model in models:
    file = base_path_output / f"oxygen18_time_series_{model}.csv"
    df_output = pd.read_csv(file, sep=";", parse_dates=True, index_col=0, skiprows=1)
    output = df_output['d18O'].values
    fig, ax = plt.subplots(figsize=(4, 2))
    ax.plot(t, output, color='red', ls='--', label='benchmark', lw=0.8, alpha=0.5)
    ax.plot(t, arr_obs, lw=1, color='blue', ls='-', marker='o', markersize=1, label='observed')
    ax.set_xlim(0, len(t))
    ax.set_ylabel(r'$\delta_{18}O$ [per mille]')
    ax.set_xlabel('Time [days]')
    ax.legend(frameon=False)
    fig.tight_layout()
    file = base_path_figs / f"oxygen18_time_series_{model}.png"
    fig.savefig(file, dpi=300)

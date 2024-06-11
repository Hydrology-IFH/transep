# Modelling tracer transport with TRANSEP at the Rietholzbach lysimeter site

Code to simulate oxygen-18 and bromide transport using the TRANSEP model. Virtual experiments are conducted for bromide since precipitation data for the years 1991 and 1992 is not available.

Short description of files and folders:
- `input/`: contains precipitation data (`PRECIP.csv`; daily time steps), oxygen-18 of precipitation (`d18O_in.csv`; daily time steps), modified oxygen-18 of precipitation (`d18O_in_mod.csv`; daily time steps) according to Stumpp et al. (2009) and bromide injections of different years (`bromide_in_year.csv`; daily time steps)
- `observations/`: oxygen-18 of percolation (`d18O_out.csv`; daily time steps) and bromide breakthrough curve (`bromide_breakthrough.csv`; daily time steps and weekly time steps)
- `output/`: contains the model output as .csv-files
- `figures/`: contains the figures
- `simulate_bromide.py`: Python script to run the TRANSEP model for bromide
- `plot_bromide_time_series.py`: Python script to plot the simulated bromide time series
- `simulate_oxygen18.py`: Python script to run the TRANSEP model for oxygen-18
- `plot_oxygen18_time_series.py`: Python script to plot the simulated oxygen-18 time series

Workflow:
1. Run the simulation `python simulate_oxygen18.py`.
2. Plot the simulation results `plot_oxygen18_time_series.py`.
3. Run the simulation `python simulate_bromide.py`.
4. Plot the simulation results `plot_bromide_time_series.py`.

Bromide tracer experiment:
See Menzel and Demuth (1993)

Rietholzbach Lysimeter:
See Seneviratne et al. (2012) and Hirschi et al. (2017)

References:
Hirschi, M., Michel, D., Lehner, I., and Seneviratne, S. I.: A site-level comparison of lysimeter and eddy covariance flux measurements of evapotranspiration, Hydrol. Earth Syst. Sci., 21, 1809-1825, https://doi.org/10.5194/hess-21-1809-2017, 2017.

Menzel, L., and Demuth, N.: Tracerhydrologische Untersuchungen am Lysimeter Rietholzbach, Geographisches Institut ETH Zürich, Zurich, Switzerland, 24, 1993.

Seneviratne, S. I., Lehner, I., Gurtz, J., Teuling, A. J., Lang, H., Moser, U., Grebner, D., Menzel, L., Schroff, K., Vitvar, T., and Zappa, M.: Swiss prealpine Rietholzbach research catchment and lysimeter: 32 year time series and 2003 drought event, Water Resources Research, 48, https://doi.org/10.1029/2011wr011749, 2012.

Stumpp, C., Stichler, W., and Maloszewski, P.: Application of the environmental isotope δ18O to study water flow in unsaturated soils planted with different crops: Case study of a weighable lysimeter from the research field in Neuherberg, Germany, Journal of Hydrology, 368, 68-78, https://doi.org/10.1016/j.jhydrol.2009.01.027, 2009.
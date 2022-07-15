import numpy as np
from scipy.special import gamma


def convolution_integral(input, g, dtau, **kwargs):
    r"""Calculates convolution integral using fourier transformation

    .. math::

        C_{\text{out}}(t) = \int_{0}^{t} C_{\text{in}}(t-\tau) w(t-\tau) g(\tau) d\tau

    Args
    ----
    input : np.array
        input signal

    g : function
        transfer function

    dtau : int, float
        incremental time step

    Returns
    -------
    fout : np.array
        output signal
    """
    t = np.arange(1, len(input) + 1)
    gout = g(t, **kwargs)
    fout = np.convolve(input, gout, mode='same') * dtau

    return fout[::-1]


def convolution_integral_explicit(input, g, dtau, **kwargs):
    r"""Calculates explicit convolution integral

    .. math::

        C_{\text{out}}(t) = \int_{0}^{t} C_{\text{in}}(t-\tau) w(t-\tau) g(\tau) d\tau

    Args
    ----
    input : np.array
        input signal

    g : function
        transfer function

    dtau : int, float
        incremental time step

    Returns
    -------
    fout : np.array
        output signal
    """
    t = np.arange(1, len(input) + 1)
    gout = g(t, **kwargs)
    out = np.zeros(len(t))
    for i in range(1, len(t)):
        out[i:] = out[i:] + input[i] * gout[:-i]

    return out


def dispersion_function(tau, p_d=0.1, mtt=40):
    r"""Dispersive transfer function for dispersion model

    .. math::

        g(\tau) = \frac{1}{\tau \sqrt{4 \pi\left(P_{D}\right)^{*} \cdot \frac{\tau}{T_{m}}}} \exp \left[-\frac{\left(1-\frac{\tau}{T_{m}}\right)^{2}}{4\left(P_{D}\right)^{*} \frac{\tau}{T_{m}}}\right]

    Stumpp, C., Stichler, W., and Maloszewski, P.: Application of the
    environmental isotope δ18O to study water flow in unsaturated soils planted
    with different crops: Case study of a weighable lysimeter from the research
    field in Neuherberg, Germany, Journal of Hydrology, 368, 68-78,
    https://doi.org/10.1016/j.jhydrol.2009.01.027, 2009.

    Args
    ----
    tau : float, np.array
        time step

    p_d : float
        dispersion parameter

    mtt : float
        mean travel time

    Returns
    -------
    gout : float, np.array
        travel time distribution
    """
    gout = (1 / tau * np.sqrt(4*np.pi*p_d*(tau/mtt))) * np.exp(-(1 - (tau/mtt))**2 / (4*p_d*(tau/mtt)))

    return gout


def linear_reservoir_function(tau, mtt=40):
    r"""Linear reservoir transfer function for linear reservoir model

    .. math::

        g(\tau) = \frac{1}{\tau_{\mathrm{m}}} \exp \left(\frac{-\tau}{\tau_{\mathrm{m}}}\right)

    Seeger, S., and Weiler, M.: Reevaluation of transit time distributions,
    mean transit times and their relation to catchment topography,
    Hydrol. Earth Syst. Sci., 18, 4751-4771, https://doi.org/10.5194/hess-18-4751-2014, 2014.

    Args
    ----
    tau : float, np.array
        time step

    mtt : float
        mean travel time

    Returns
    -------
    gout : float, np.array
        travel time distribution
    """
    gout = (1 / mtt) * np.exp(-tau/mtt)

    return gout


def parallel_linear_reservoir_function(tau, mtt_slow=40, mtt_fast=10, frac_fast=0.1):
    r"""Parallel linear reservoir transfer function for paralle linear reservoir model

    .. math::

        g(\tau) = \frac{\phi}{\tau_{\mathrm{f}}} \exp \left(-\frac{\tau}{\tau_{\mathrm{f}}}\right)+\frac{1-\phi}{\tau_{\mathrm{s}}} \exp \left(-\frac{\tau}{\tau_{\mathrm{s}}}\right)

    Seeger, S., and Weiler, M.: Reevaluation of transit time distributions,
    mean transit times and their relation to catchment topography,
    Hydrol. Earth Syst. Sci., 18, 4751-4771, https://doi.org/10.5194/hess-18-4751-2014, 2014.

    Args
    ----
    tau : float, np.array
        time step

    mtt_slow : float
        mean travel time of slow reservoir

    mtt_fast : float
        mean travel time of fast reservoir

    frac_fast : float
        fraction of fast reservoir (value range is between 0 and 1)

    Returns
    -------
    gout : float, np.array
        travel time distribution
    """
    gout = (frac_fast / mtt_fast) * np.exp(-tau/mtt_fast) + (1 - frac_fast / mtt_slow) * np.exp(-tau/mtt_slow)

    return gout


def exponential_piston_function(tau, mtt=40, eta=1):
    gout = np.where(tau >= mtt * (1 - eta**(-1)), (eta/mtt) * np.exp(((-eta**tau)/mtt) + eta - 1), 0)

    return gout


def gamma_function(tau, alpha=1, beta=1):
    r"""Gamma transfer function for gamma model

    .. math::

        g(\tau) = \frac{\tau^{\alpha-1}}{\beta^{\alpha} \Gamma(\alpha)} \exp (-\tau / \beta)


    Seeger, S., and Weiler, M.: Reevaluation of transit time distributions,
    mean transit times and their relation to catchment topography,
    Hydrol. Earth Syst. Sci., 18, 4751-4771, https://doi.org/10.5194/hess-18-4751-2014, 2014.

    Args
    ----
    tau : float, np.array
        time step

    alpha : float
        scale parameter

    beta : float
        shape parameter

    Returns
    -------
    gout : float, np.array
        travel time distribution
    """
    gout = (tau**(alpha-1) / (beta**alpha) * gamma(alpha)) * np.exp(-tau/beta)

    return gout


def simulate(input, g, dtau, **kwargs):
    """Runs simulation of transport model

    Args
    ----
    input : np.array
        input signal

    g : function
        transfer function

    dtau : int, float
        incremental time step

    Returns
    -------
    fout : np.array
        output signal
    """
    out = convolution_integral(input, g, dtau, **kwargs)

    return out


def simulate_explicit(input, g, dtau, **kwargs):
    """Runs simulation of transport model

    Args
    ----
    input : np.array
        input signal

    g : function
        transfer function

    dtau : int, float
        incremental time step

    Returns
    -------
    fout : np.array
        output signal
    """
    out = convolution_integral_explicit(input, g, dtau, **kwargs)

    return out

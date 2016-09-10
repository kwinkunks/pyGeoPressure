"""routines to assist velocity data processing.
"""
import numpy as np


def bowers(v, obp, v0=5000, a=9.18448, b=0.764984):
    """
    Compute pressure using Bowers equation.

    Parameters
    ----------
    v : 1-d ndarray
        velocity array whose unit is m/s.
    obp : 1-d ndarray
        Overburden pressure whose unit is Pa.
    v0 : float, optional
        the velocity of unconsolidated regolith whose unit is ft/s.
    a : float, optional
        coefficient a
    b : float, optional
        coefficient b

    Notes
    -----
    .. math:: P = OBP - [\\frac{(V-V_{0})}{a}]^{\\frac{1}{b}}
    """
    ves = ((v * 3.2808300 - v0) / a)**(1.0 / b)
    pressure = obp - ves * 6894.75729
    return pressure


def eaton(v, vn, vesn, obp, a=0.785213, b=1.49683):
    """
    Compute pore pressure using Eaton equation.

    Parameters
    ----------
    v : 1-d ndarray
        velocity array whose unit is m/s.
    vn : 1-d ndarray
        normal velocity array whose unit is m/s.
    vesn : 1-d ndarray
        vertical effective stress under normal compaction array
        whose unit is m/s.
    obp : 1-d ndarray
        Overburden pressure whose unit is Pa.
    v0 : float, optional
        the velocity of unconsolidated regolith whose unit is ft/s.
    a : float, optional
        coefficient a
    b : float, optional
        coefficient b

    Notes
    -----
    .. math:: P = OBP - VES_{n}* a (\\frac{V}{V_{n}})^{b}
    """
    ves = vesn * a * (v / vn)**b
    pressure = obp - ves
    return pressure


def fillipino():
    pass


if __name__ == '__main__':
    pass

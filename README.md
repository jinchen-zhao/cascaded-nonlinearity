# Cascaded Nonlinearity

What does cascaded nonlinearity mean? We are cascading several $\chi_2$ nonlinear processes together to achieve a $\chi_3$ effect.

Why do we want to do this? This approach enables a high level of tunability of the $\chi_3$ process: we can not only change the magnitude of $\chi_3$, but also its sign! Recall from class that $\chi_3$ from materials can only be positive. However, we can realize a negative effective $\chi_3$ through cascaded nonlinearity.

These $\chi_2$ nonlinear processes need to be very inefficient to achieve this; i.e., they must have a very large phase mismatch, otherwise we will only observe a $\chi_2$ effect. We will use a highly phase-mismatched second harmonic generation (SHG) as an example. The intuition is rather simple: In phase-matched SHG, the fundamental wave is converted to the second harmonics with high efficiency. However, when the process is highly phase mismatched, the second harmonics will be converted back to the fundamental mode. This back action effectively leads to a nonlinear $\chi_3$ effect.

There are three main files:

- `Tutorial.ipynb`: The tutorial notebook as an introduction to cascaded nonlinearity. For illustrative purposes, we mainly have visualizations in this notebook, and the solver functions are in `CascadeNL.py`.
- `CascadeNL.py`: The nonlinear solvers for SHG and Kerr nonlinearity.
- `SanityCheck.ipynb`: A sanity check to compare with Boyd's textbook, Agrawal's textbook, and experimental papers to ensure the accuracy of the nonlinear solver in `CascadeNL.py`.

# Cascaded Nonlinearity

What does cascaded nonlinearity mean? We are cascading several $\chi^{(2)}$ nonlinear processes together to achieve a $\chi^{(3)}$ effect.

Why do we want to do this? This approach enables a high level of tunability of the $\chi^{(3)}$ process: we can not only change the magnitude of $\chi^{(3)}$, but also its sign! Recall from class that $\chi_3$ from materials can only be positive. However, we can realize a negative effective $\chi^{(3)}$ through cascaded nonlinearity.

These $\chi^{(2)}$ nonlinear processes need to be very inefficient to achieve this; i.e., they must have a very large phase mismatch, otherwise we will only observe a $\chi^{(2)}$ effect. We will use a highly phase-mismatched second harmonic generation (SHG) as an example. The intuition is rather simple: In phase-matched SHG, the fundamental wave is converted to the second harmonics with high efficiency. However, when the process is highly phase mismatched, the second harmonics will be converted back to the fundamental mode. This back action effectively leads to a nonlinear $\chi^{(3)}$ effect.

There are three main files:

- `Tutorial.ipynb`: The tutorial notebook as an introduction to cascaded nonlinearity. For illustrative purposes, we mainly have visualizations in this notebook, and the solver functions are in `CascadeNL.py`.
- `CascadeNL.py`: The nonlinear solvers for SHG and Kerr nonlinearity.
- `SanityCheck.ipynb`: A sanity check to compare with Boyd's textbook, Agrawal's textbook, and experimental papers to ensure the accuracy of the nonlinear solver in `CascadeNL.py`.

<img width="881" alt="Screenshot 2024-04-25 at 17 02 38" src="https://github.com/jinchen-zhao/cascaded-nonlinearity/assets/56393201/76de12f2-1cde-4df2-bd4b-7b1266a0a82f">

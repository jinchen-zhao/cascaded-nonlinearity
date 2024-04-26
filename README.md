# Cascaded Nonlinearity

What does cascaded nonlinearity mean? We are cascading several $\chi^{(2)}$ nonlinear processes together to achieve a $\chi^{(3)}$ effect.

Why do we want to do this? This approach enables a high level of tunability of the $\chi^{(3)}$ process: we can not only change the magnitude of $\chi^{(3)}$, but also its sign! Recall from class that $\chi^{(3)}$ from materials can only be positive. However, we can realize a negative effective $\chi^{(3)}$ through cascaded nonlinearity.

These $\chi^{(2)}$ nonlinear processes need to be very inefficient to achieve this; i.e., they must have a very large phase mismatch, otherwise we will only observe a $\chi^{(2)}$ effect. We will use a highly phase-mismatched second harmonic generation (SHG) as an example. The intuition is rather simple: In phase-matched SHG, the fundamental wave is converted to the second harmonics with high efficiency. However, when the process is highly phase mismatched, the second harmonics will be converted back to the fundamental mode. This back action effectively leads to a nonlinear $\chi^{(3)}$ effect.

There are three main files:

- `Tutorial.ipynb`: The tutorial notebook as an introduction to cascaded nonlinearity. For illustrative purposes, we mainly have visualizations in this notebook, and the solver functions are in `CascadeNL.py`.
- `CascadeNL.py`: The nonlinear solvers for SHG and Kerr nonlinearity.
- `SanityCheck.ipynb`: A sanity check to compare with Boyd's textbook, Agrawal's textbook, and experimental papers to ensure the accuracy of the nonlinear solver in `CascadeNL.py`.

<img width="911" alt="Screenshot 2024-04-25 at 18 18 33" src="https://github.com/jinchen-zhao/cascaded-nonlinearity/assets/56393201/8a72de74-562d-462e-b203-71de7e8a3e47">

### References

1. Bache, M. (2017). Cascaded nonlinearities for ultrafast nonlinear optical science and applications. DTU - Department of Photonics Engineering.


2. Jankowski, M., Langrock, C., Desiatov, B., Marandi, A., Wang, C., Zhang, M., Phillips, C. R., Lončar, M., & Fejer, M. M. (2020). Ultrabroadband nonlinear optics in nanophotonic periodically poled lithium niobate waveguides. Optica, 7(1), 40.

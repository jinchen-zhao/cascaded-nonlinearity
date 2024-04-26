import numpy as np
import matplotlib.pyplot as plt


def SHG(beta21 = 1, beta22 = 1, dbeta0 = 0, 
        length = 2e-5, nlLength1 = 5e-6, nlLength2 = 5e-6, 
        tMax = 15, tPrecision = 2**10, zPrecision = 2000):
    """
    Simulate the SHG process
    
    Arguments:
    beta21:      second order dispersion of pump, set to 1 since we are working in unit of dispersion length
    beta22:      second order dispersion of second harmonic
    dbeta0:      phase mismatch

    length:      length of crystal, in unit of dispersion length
    nlLength1:   nonlinear length of pump, in unit of dispersion length
    nlLength2:   nonlinear length of second harmonic, in unit of dispersion length
    
    tMax:        pulse width
    tPrecision:  precision of time axis
    zPrecision:  precision of position axis
    
    Return: Visualization of pump and signal evolution, and SHG efficiency
    """
    
    # Initialize time and position axis
    tau   = (2 * tMax / tPrecision) * np.arange(-tPrecision / 2, tPrecision / 2)
    omega = (-np.pi / tMax) * np.arange(-tPrecision / 2, tPrecision / 2)
    dz = length / zPrecision

    # Initialize pulses
    pumpTemp = 1/np.cosh(tau)
    signalTemp = pumpTemp * 0

    u1 = pumpTemp.copy()
    u2 = signalTemp.copy()
    total_energy = np.sum(np.abs(pumpTemp)**2)

    # Dispersion operator
    linear_operator1 = np.fft.fftshift(np.exp(0.5j * beta21 * omega**2 * dz))
    linear_operator2 = np.fft.fftshift(np.exp(0.5j * beta22 * omega**2 * dz))

    # Storage arrays for field evolution and energy conversion
    u1_evolution_time = np.zeros((zPrecision, tPrecision), dtype=complex)
    u2_evolution_time = np.zeros((zPrecision, tPrecision), dtype=complex)
    u1_evolution_freq = np.zeros((zPrecision, tPrecision), dtype=complex)
    u2_evolution_freq = np.zeros((zPrecision, tPrecision), dtype=complex)
    pump_energy_fraction = np.zeros(zPrecision)
    signal_energy_fraction = np.zeros(zPrecision)

    # Propagation loop
    for i in range(zPrecision):
        # Linear step (Fourier domain)
        u1_hat = np.fft.fft(u1) * linear_operator1
        u2_hat = np.fft.fft(u2) * linear_operator2
        u1 = np.fft.ifft(u1_hat)
        u2 = np.fft.ifft(u2_hat)

        # Nonlinear step (Time domain)
        u1 += dz * (1j / nlLength1) * np.conjugate(u1) * u2 * np.exp(-1j * dbeta0 * dz * i)
        u2 += dz * (1j / (nlLength2)) * u1**2 * np.exp(1j * dbeta0 * dz * i)

        # Store fields for visualization
        u1_evolution_time[i, :] = u1
        u2_evolution_time[i, :] = u2
        u1_evolution_freq[i, :] = np.fft.fftshift(np.abs(np.fft.fft(u1)))
        u2_evolution_freq[i, :] = np.fft.fftshift(np.abs(np.fft.fft(u2)))

        # Energy calculations
        pump_energy_fraction[i] = np.sum(np.abs(u1)**2) / total_energy
        signal_energy_fraction[i] = np.sum(np.abs(u2)**2) / total_energy

    # Visualization of field evolution and energy conversion
    fig, axs = plt.subplots(2, 3, figsize=(10,5))

    axs[0, 0].imshow(np.abs(u1_evolution_time), extent=[-1, 1, 1, 0], aspect='auto')
    axs[0, 0].set_title('Pump evolution')
    axs[0, 0].set_xlabel('Time')
    axs[0, 0].set_ylabel('Distance')
    axs[0, 0].locator_params(nbins=3)
    
    axs[0, 1].imshow(np.abs(u1_evolution_freq), extent=[-1, 1, 1, 0], aspect='auto')
    axs[0, 1].set_title('Pump evolution')
    axs[0, 1].set_xlabel('Frequency')
    axs[0, 1].set_ylabel('Distance')
    axs[0, 1].locator_params(nbins=3)

    axs[1, 0].imshow(np.abs(u2_evolution_time), extent=[-1, 1, 1, 0], aspect='auto')
    axs[1, 0].set_title('Signal evolution')
    axs[1, 0].set_xlabel('Time')
    axs[1, 0].set_ylabel('Distance')
    axs[1, 0].locator_params(nbins=3)

    axs[1, 1].imshow(np.abs(u2_evolution_freq), extent=[-1, 1, 1, 0], aspect='auto')
    axs[1, 1].set_title('Signal evolution')
    axs[1, 1].set_xlabel('Frequency')
    axs[1, 1].set_ylabel('Distance')
    axs[1, 1].locator_params(nbins=3)

    # Energy conversion plot
    axs[1, 2].plot(np.linspace(0, 1, zPrecision), pump_energy_fraction, label='Pump')
    axs[1, 2].plot(np.linspace(0, 1, zPrecision), signal_energy_fraction, label='Signal')
    axs[1, 2].plot(np.linspace(0, 1, zPrecision), pump_energy_fraction+signal_energy_fraction, label='Sum')
    axs[1, 2].set_title('Efficiency')
    axs[1, 2].set_xlabel('Distance')
    axs[1, 2].set_ylabel('Energy Conversion')
    axs[1, 2].legend(loc="center left", bbox_to_anchor=(1,0.5))
    axs[1, 2].locator_params(nbins=3)

    axs[0, 2].plot(np.linspace(-1, 1, tPrecision), np.abs(u1_evolution_time)[0], label='Initial pump')
    axs[0, 2].plot(np.linspace(-1, 1, tPrecision), np.abs(u1_evolution_time)[-1], label='Final pump')
    axs[0, 2].legend(loc="center left", bbox_to_anchor=(1,0.5))
    axs[0, 2].set_xlabel('Time')
    axs[0, 2].set_ylabel('Amplitude')
    axs[0, 2].locator_params(nbins=3)


    plt.tight_layout()
    plt.show()
    
    
def Kerr(beta2 = 1, gamma = 1, length = 2e-5, tMax = 15, tPrecision = 2**10, zPrecision = 2000):
    """
    Simulate the Kerr nonlinearity
    
    Arguments:
    beta2:       second order dispersion
    gamma:       nonlinear Kerr coefficient

    length:      length of crystal, in unit of dispersion length
    
    tMax:        pulse width
    tPrecision:  precision of time axis
    zPrecision:  precision of position axis
    
    Return: Visualization of pulse evolution
    """
    
    # Initialize time and position axis
    tau   = (2 * tMax / tPrecision) * np.arange(-tPrecision / 2, tPrecision / 2)
    omega = (-np.pi / tMax) * np.arange(-tPrecision / 2, tPrecision / 2)
    dz = length / zPrecision

    # Initialize fields
    pumpTemp = 1/np.cosh(tau)
    u = pumpTemp.copy()

    # Dispersion operator
    linear_operator = np.fft.fftshift(np.exp(0.5j * beta2 * omega**2 * dz))

    # Storage arrays for field evolution and energy conversion
    u_evolution_time = np.zeros((zPrecision, tPrecision), dtype=complex)
    u_evolution_freq = np.zeros((zPrecision, tPrecision), dtype=complex)

    # Propagation loop
    for i in range(zPrecision):
        # Linear step (Fourier domain)
        u_hat = np.fft.ifft(u) * linear_operator        
        u = np.fft.fft(u_hat)

        # Nonlinear step (Time domain)
        u = u * np.exp(1j * gamma * np.abs(u)**2 * dz)

        # Store fields for visualization
        u_evolution_time[i, :] = u
        u_evolution_freq[i, :] = np.fft.fftshift(np.abs(np.fft.fft(u)))


    # Visualization of field evolution and energy conversion
    fig, axs = plt.subplots(1, 2, figsize=(6,2.5))

    axs[0].imshow(np.abs(u_evolution_time), extent=[-1, 1, 1, 0], aspect='auto')
    axs[0].set_title('Pump evolution')
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Distance')
    axs[0].locator_params(nbins=3)


    axs[1].imshow(np.abs(u_evolution_freq), extent=[-1, 1, 1, 0], aspect='auto')
    axs[1].set_title('Pump evolution')
    axs[1].set_xlabel('Frequency')
    axs[1].set_ylabel('Distance')
    axs[1].locator_params(nbins=3)

    plt.tight_layout()
    plt.show()
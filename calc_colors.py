import numpy as np

def filt_val(filt, spectrum):
    """
    Determine filter curve magnitude and zero point for a spectrum
    given an input filter curve.

        Parameters:
            filt ([float,float]): filter curve information [wavelength,response]
            spectrum ([float,float]): observed or model spectrum [wavelength,flux]

        Returns:
            filt_mag (float): filter magnitude
            filt_mag_zero (float): filter magnitude zero point
    """

    # interpolate between the beginning and end of the filter
    nterp = np.interp(spectrum[:,0],filt[:,0],filt[:,1])
    # finish interpolation
    nterp_2 = nterp*spectrum[:,1]
    
    # add up all of those new sums
    sum = np.sum(nterp_2)
    # divide by sum
    filt_sum = sum / np.sum(nterp)
    
    # turn this into a magnitude
    filt_mag = -2.5*np.log10(filt_sum)

    # create wavelength array for interpolated spectrum
    wave = np.zeros(len(spectrum))
    for i in np.arange(1,len(spectrum)):
        wave[i] = 1./(spectrum[i,0]**2)

    # determine the zero point
    filt_mag_zero = -2.5*np.log10(np.sum(np.multiply(nterp,wave))/(np.sum(nterp)))

    return filt_mag, filt_mag_zero

def main():

    # read in filter curves
    b_filt = np.loadtxt("b.dat")
    v_filt = np.loadtxt("v.dat")
    r_filt = np.loadtxt("r.dat")

    # model or observed spectrum
    # [wavelength,flux]
    spectrum = np.loadtxt('RSG_binary_model.txt')

    # filter values
    b_filt_val,b_filt_val_zero = filt_val(b_filt,spectrum)
    v_filt_val,v_filt_val_zero = filt_val(v_filt,spectrum)
    r_filt_val,r_filt_val_zero = filt_val(r_filt,spectrum)

    # colors
    bv = (b_filt_val - v_filt_val) - (b_filt_val_zero - v_filt_val_zero)
    vr = (v_filt_val - r_filt_val) - (v_filt_val_zero - r_filt_val_zero)

    # magnitudes
    b = b_filt_val - b_filt_val_zero
    v = v_filt_val - v_filt_val_zero
    r = r_filt_val - r_filt_val_zero

    print(" b-v:",round(bv,2),"\n v-r:",round(vr,2))

if __name__ == "__main__":
    main()

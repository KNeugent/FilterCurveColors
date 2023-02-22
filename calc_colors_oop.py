import numpy as np

class Filter:
    """
    Instantiate the filter class.
    """
    # create instance variables for the name and filter curve
    def __init__(self, name, wavelength, response):
        self.name = name
        self.wavelength = wavelength
        self.response = response

class Magnitude:
    """
    Instantiate the magnitude class.
    """
    # create instance variables for the name, value, and zero point
    def __init__(self, value, zero_point):
        self.value = value
        self.zero_point = zero_point

    # Instance methods for value and zero point
    def description(self):
        return f"the magnitude is {self.value} and the zero point is {self.zero_point}"

class Spectrum:
    """
    Instantiate the spectrum class.
    """
    # create instance variables for the name, wavelength, and flux
    def __init__(self, name, wavelength, flux):
        self.name = name
        self.wavelength = wavelength
        self.flux = flux

def filt_val(Filter, Spectrum):
    """
    Determine filter curve magnitude and zero point for a spectrum
    given an input filter curve.

        Parameters:
            Filter (Filter object)
            Spectrum (Spectrum object)

        Returns:
            new_magnitude (Magnitude object)
    """

    # interpolate between the beginning and end of the filter
    nterp = np.interp(Spectrum.wavelength,Filter.wavelength,Filter.response)
    # finish interpolation
    nterp_2 = nterp*Spectrum.flux
    
    # add up all of those new sums
    sum = np.sum(nterp_2)
    # divide by sum
    filt_sum = sum / np.sum(nterp)
    
    # create wavelength array for interpolated spectrum
    wave = np.zeros(len(Spectrum.wavelength))
    for i in np.arange(1,len(Spectrum.wavelength)):
        wave[i] = 1./(Spectrum.wavelength[i]**2)

    # turn this into a magnitude
    mag = -2.5*np.log10(filt_sum)

    # determine the zero point
    mag_zero = -2.5*np.log10(np.sum(np.multiply(nterp,wave))/(np.sum(nterp)))

    new_magnitude = Magnitude(mag, mag_zero)

    return new_magnitude

def calc_color(Magnitude1, Magnitude2):
    """ 
    Return the color by subtracting magnitude2 from magnitude1

        Parameters:
            Magnitude1 (Magnitude Object)
            Magnitude2 (Magnitude Object)

        Returns:
            color (float)
    """

    color = (Magnitude1.value - Magnitude2.value) - (Magnitude1.zero_point - Magnitude2.zero_point)

    return color
    
def main():

    # read in filter curves
    b_filt = np.loadtxt("b.dat")
    v_filt = np.loadtxt("v.dat")
    r_filt = np.loadtxt("r.dat")

    # model or observed spectrum
    # [wavelength,flux]
    spectrum_input = np.loadtxt('RSG_binary_model.txt')

    # create Filter objects
    b_Filter = Filter("b",b_filt[:,0],b_filt[:,1])
    v_Filter = Filter("v",v_filt[:,0],v_filt[:,1])
    r_Filter = Filter("r",r_filt[:,0],r_filt[:,1])
    # create Spectrum object
    spec = Spectrum("RSG_binary",spectrum_input[:,0],spectrum_input[:,1])

    # get magnitudes from filter val equation
    b_Magnitude = filt_val(b_Filter,spec)
    v_Magnitude = filt_val(v_Filter,spec)
    r_Magnitude = filt_val(r_Filter,spec)

    # colors
    bv = calc_color(b_Magnitude,v_Magnitude)
    vr = calc_color(v_Magnitude,r_Magnitude)

    print("b-v:",round(bv,2),"\nv-r:",round(vr,2))

if __name__ == "__main__":
    main()

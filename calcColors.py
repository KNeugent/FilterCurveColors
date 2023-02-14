import numpy as np

def filtVal(filt, spectrum):
    """
    Determine filter curve magnitude and zero point for a spectrum
    given an input filter curve.

        Parameters:
            filt ([float,float]): filter curve information [wavelength,response]
            spectrum ([float,float]): observed or model spectrum [wavelength,flux]

        Returns:
            filtMag (float): filter magnitude
            filtMagZero (float): filter magnitude zero point
    """

    # interpolate between the beginning and end of the filter
    nterp = np.interp(spectrum[:,0],filt[:,0],filt[:,1])
    # finish interpolation
    nterp_2 = nterp*spectrum[:,1]
    
    # add up all of those new sums
    sum = np.sum(nterp_2)
    # divide by sum
    filtSum = sum / np.sum(nterp)
    
    # turn this into a magnitude
    filtMag = -2.5*np.log10(filtSum)

    # create wavelength array for interpolated spectrum
    wave = np.zeros(len(spectrum))
    for i in np.arange(1,len(spectrum)):
        wave[i] = 1./(spectrum[i,0]**2)

    # determine the zero point
    filtMagZero = -2.5*np.log10(np.sum(np.multiply(nterp,wave))/(np.sum(nterp)))

    return filtMag, filtMagZero

def main():

    # read in filter curves
    uFilt = np.loadtxt("u.dat")
    gFilt = np.loadtxt("g.dat")
    rFilt = np.loadtxt("r.dat")
    iFilt = np.loadtxt("i.dat")
    zFilt = np.loadtxt("z.dat")

    # model or observed spectrum
    # [wavelength,flux]
    spectrum = np.loadtxt('RSGbinaryModel.txt')

    # filter values
    uFiltVal,uFiltValZero = filtVal(uFilt,spectrum)
    gFiltVal,gFiltValZero = filtVal(gFilt,spectrum)
    rFiltVal,rFiltValZero = filtVal(rFilt,spectrum)
    iFiltVal,iFiltValZero = filtVal(iFilt,spectrum)
    zFiltVal,zFiltValZero = filtVal(zFilt,spectrum)

    # colors
    ug = (uFiltVal - gFiltVal) - (uFiltValZero - gFiltValZero)
    gr = (gFiltVal - rFiltVal) - (gFiltValZero - rFiltValZero)
    iz = (iFiltVal - zFiltVal) - (iFiltValZero - zFiltValZero)

    # magnitudes
    u = uFiltVal - uFiltValZero
    g = gFiltVal - gFiltValZero
    r = rFiltVal - rFiltValZero
    i = iFiltVal - iFiltValZero
    z = zFiltVal - zFiltValZero

    print(" u-g:",round(ug,2),"\n g-r:",round(gr,2),"\n i-z:",round(iz,2))

if __name__ == "__main__":
    main()

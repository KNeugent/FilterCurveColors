# Determining Colors from Filter Curves
This program determines the photometric colors of an astronomical object based on an input spectrum and filter curve file.

## Usage

The only imported package is `numpy`.

This code has been tested using `python 3.7.3` and `numpy 1.18.2`.

## Inputs

Currently the program works for SDSS `ugriz` filters and the `ugriz` filter curves are included in the repro. However, any filter curve can be used as long as the first column is wavelength (Angstrom) and the second column is the sensitivity. More filter curves can be found [here](http://svo2.cab.inta-csic.es/svo/theory/fps3/index.php).

A test spectrum is included (`RSG_binary_model.txt`), but again, any spectrum can be used as long as the first column contains the wavelength (Angstrom) and the second contains the flux.

## Outputs

Currently, the program simply prints the `u-g`, `g-r`, and `i-z` colors, but this can be easily expanded upon for other filter curve combinations and colors.

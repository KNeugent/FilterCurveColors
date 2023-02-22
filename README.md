# Determining Colors from Filter Curves
This program determines the photometric colors of an astronomical object based on an input spectrum and filter curve file.

## Usage

The only imported package is `numpy` for the non-OOP version of this code. In the OOP version of this code (see explaination below), the `unittest` package is also imported.

This code has been tested using `python 3.7.3` and `numpy 1.18.2`.

## Inputs

Currently the program works for Johnson `bvr` filters and the `bvr` filter curves are included in the repro. However, any filter curve can be used as long as the first column is wavelength (Angstrom) and the second column is the sensitivity. More filter curves can be found [here](http://svo2.cab.inta-csic.es/svo/theory/fps3/index.php).

A test spectrum is included (`RSG_binary_model.txt`), but again, any spectrum can be used as long as the first column contains the wavelength (Angstrom) and the second contains the flux.

## Outputs

Currently, the program simply prints the `b-v` and `v-r` colors, but this can be easily expanded upon for other filter curve combinations and colors.

## Object-Oriented Expansion and Unit Tests

While there was no need to make this code object-oriented, for practice I decided to convert the original Python code into OOP. This can be found in `calc_colors_oop.py`. My first six years of programming was in Java, so while I've had plenty of experience with OOP, I had never created objects in Python (OOP hasn't quite infiltrated astronomical programming yet).

To convert my original Python code to OOP, I first instantiated Filter, Magnitude, and Spectrum objects. I then created their respective instance variables and gave them appropriate instance methods. Finally, I edited the remaining code to use these new objects. While this certainly isn't the best example of OOP, it was fun to use a technique I hadn't practiced in a while.

I additionally added a very basic example of a unit test using the Python `unittest` package. To run the unit test, simply uncomment the `unittest.main()` line in the main method. While I hope to begin adding more unit tests to my code in the future, this was a simple place for me to practice the basics. 
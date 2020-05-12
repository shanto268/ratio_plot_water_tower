# Analysis of water levels and absorbed muon numbers 

This program analyzes how the water height in the water tank affects the absorption/scattering of cosmic muons.

Using data from the .txt files, and the Python Codes that can handle constraints in meters. The plots generated show minimum value of ratio against water level.

## Ratio Plots

!(pic)[ratio_constraint1.png]

!(pic)[ratio_constraint5.png]

!(pic)[ratio_constraint15.png]

!(pic)[ratio_constraint18.png]

## Interpretations:

For the suggested constraints [-5m , 5m] the intercept seems to be around 0.58 . The relationship seems to be like a decaying exponential except for the fact that the intercept is not 1. Will need to think if such a trend is feasible in this scenario.

The constraints are defined as the limiting space span of x and y. For example a constraing of [-5 meters to 5 meters] would only take entries the from the square made by the red lines shown below.

!(pic1)[MC2.jpg]

'''
we need :
pandas
numpy
scipy
statsmodels

with the permission from:
Seabold, Skipper, and Josef Perktold.
“Statsmodels: Econometric and statistical modeling with python.”
Proceedings of the 9th Python in Science Conference. 2010.

'''
import pandas as pd
import numpy as np
import statsmodels.api as sm

import statsmodels.formula.api as smf
import urllib.request
import requests
import json


#  Load data
# dat = sm.datasets.get_rdataset("https://data.cms.gov/resource/xbte-dn4t.csv").data

dat = urllib.request.urlopen("https://data.cms.gov/resource/xbte-dn4t.json").read()

# Fit regression model (using the natural log of one of the regressors)
results = smf.ols("Lottery ~ Literacy + np.log(Pop1831)", data=dat).fit()

# Inspect the results
print(results.summary())
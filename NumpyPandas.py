import numpy as np
import pandas as pd
#generate numpy array
anIntArray = np.random.randint(5, 72, 48)
#convert the array into pandas series
convertedSeries = pd.Series(anIntArray)
#display the desired position data from converted series
print("value at location 0: ", convertedSeries[0])
print("value at location 5: ", convertedSeries[5])
print("value at location 10: ", convertedSeries[10])
print("value at location 15: ", convertedSeries[15])
print("value at location 20: ", convertedSeries[20])

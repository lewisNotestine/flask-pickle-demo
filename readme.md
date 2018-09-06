# Demo: Pickled Scikit-Learn Models Used in a Flask App.

## Overview
This is a demo project intended to show how a pickled model (that was trained using a Jupyter notebook) can be extracted from its native environment and then put to work in a web app.

This API uses a simple linear regression model, estimated using a dataset found on Kaggle:
https://www.kaggle.com/harlfoxem/housesalesprediction/kernels

## Dependencies
* Recommend using with Anaconda (esp. on Windows)
* Dependencies are as noted in the `requirements.txt` file.

## Usage
The API has two methods, `/` (GET) and `/model` (POST).
The first is just a health check to make sure your API works.
The second is the method that actually applies the model.
The request body for this last request is structured as follows:

### Input
```
[
	[2000, 3.0, 3.0],
	[4000, 4.0, 4.0],
	[500, 1.0, 1.0]
]
```

The first element is the square footage. The second is quality of the view from the property, rated from 0 to 4. The third is the rating of the condition of the property, rated from 1 to 5.

### Output
The output of the API is returned as a price estimate in US Dollars, e.g.:
```
[781973.5926785413, 1526208.3288016743, 130384.2018653102]
```

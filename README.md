<h1>Australian Vehicle Price Prediction</h1>

![Alt text](img.png)

Exploratory Data Analysis (EDA), Data cleaning, feature extraction on 12 features and testing several ML models to predict the prices of Australian vehicles.

<h3>Built With</h3>

+ [Python](https://www.python.org/downloads/)
+ [MLFLOW](https://github.com/mlflow/mlflow)
+ [Flask](https://github.com/pallets/flask)
+ [GCP App engine deployment](https://console.cloud.google.com/appengine)
  
 <h3>About the Dataset</h3>

 [Australian Vehicle Prices Dataset - Kaggle.com](https://www.kaggle.com/datasets/nelgiriyewithana/australian-vehicle-prices)

This dataset contains the latest information on car prices in Australia for the year 2023. It covers various brands, models, types, and features of cars sold in the Australian market. It provides useful insights into the trends and factors influencing the car prices in Australia. The dataset includes information such as brand, year, model, car/suv, title, used/new, transmission, engine, drive type, fuel type, fuel consumption, kilometres, colour (exterior/interior), location, cylinders in engine, body type, doors, seats, and price. The dataset has over 16,000 records of car listings from various online platforms in Australia.

## How to run

+ STEP 01- Clone the repository

```bash
git clone https://github.com/dahshury/Australian-Vehicle-Price-Prediction
```

+ STEP 02- Create a conda environment after opening the repository and activate it

```bash
conda env create -f env.yaml
```

```bash
conda activate auscar
```

### To Run prediction using the pretrained model

run the following command in the terminal

```bash
python main.py
```

Now, open the following link in the browser

```bash
 localhost:8080
```

You can now input the data for the vehicle, and click predict for the result.

### To Run the training pipeline

Now, open the following link in the browser

```bash
 localhost:8080/train
```

### Results

Random Forest model results: 

RMSE: 10975.055615604264 

Accuracy:0.8220697023798103 

==============================

Decision Tree model results: 

RMSE: 12302.738100998016 

Accuracy:0.7764163696168624 

==============================

Ada Boost model results: 

RMSE: 16169.658896739993 

Accuracy:0.6137769735150234 

==============================

Gradient Boost model results: 

RMSE: 13216.418745091287 

Accuracy:0.7419736693988706 

==============================

XG Boost model results: 

RMSE: 10738.544642177703 

Accuracy:0.8296558201338788 

==============================

The best model is XGBoost, with the following scores:

+ Root Mean Square Error: 10738.544642177703
+ r2 score: 0.8296558201338788
+ Mean Absolute Error: 4791.962769375111

Possible improvements include (from better to worse):

+ Including the ['Title'] column, and extracting the trim out of the column for each model.
+ Gathering additional data from other datasets.
+ Fine-tuning the model using cross-validation and grid-search.

### Contact Me

[Linkedin](https://www.linkedin.com/in/dahshory/)

### Acknowledgements

Thanks to [Samir Gouda](github.com/SamirGouda) & [Omar Eldahshoury](github.com/omareldahshoury) for thier support.

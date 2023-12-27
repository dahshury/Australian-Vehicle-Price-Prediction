<h1>Australian Vehicle Price Prediction</h1>

![Alt text](img.png)

Based on 12 features, prediction of vehicle prices in Australia.

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

+ STEP 02- Create a conda environment after opening the repository (optional)

```bash
conda create -n auscar python=3.10 -y
```

```bash
conda activate auscar
```

+ STEP 03- install the requirements

```bash
pip install -r requirements.txt
```

### To Run prediction using the pretrained model

run the following command in the terminal

```bash
python main.py
```

Now, open the following link in the browser

```bash
 0.0.0.0:8080
```

You can now input the data for the vehicle, and click predict for the result.

### Results

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

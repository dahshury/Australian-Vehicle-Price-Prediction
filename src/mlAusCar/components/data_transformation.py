import pandas as pd
import numpy as np
import pandas as pd
from sklearn.compose import make_column_transformer, make_column_selector
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, FunctionTransformer
from mlAusCar.config.configuartion import DataTransformationConfig

class DataTransformation:
    def __init__(self,
                    config: DataTransformationConfig):
        self.config = config
    
    def transform_data(self):    
        
        # Loading the data:
        csv_path = self.config.csv_path
        df = pd.read_csv(csv_path)

        # Most of the missing values aren't within columns we care about or are few. Safe to drop them
        df.dropna(inplace=True)

        # Location extraction by state to reduce the number of features
        df['State'] = df['Location'].str.extract(r'\, (\w+\-?\w+)')

        # Dropping unnecessary columns
        df.drop(columns=['Brand', 'Car/Suv', 'Title', 'ColourExtInt', 'Location'], axis=1, inplace=True)

        # Extracting fuel consumption number of liters per 100 km
        df['FuelConsumption'] = df['FuelConsumption'].str.extract(r'(\d+\.?\d*) L.*')

        # Extracting engine displacement in L
        df['Engine'] = df['Engine'].str.extract(r'(\d+\.?\d*) L.*')

        # Extracting cylinder count
        df['CylindersinEngine'] = df['CylindersinEngine'].str.extract(r'(\d+) \w+.*')

        # Extracting number of doors
        df['Doors'] = df['Doors'].str.extract(r'(\d+) Doors')

        # Extracting number of seats
        df['Seats'] = df['Seats'].str.extract(r'(\d+) Seats')

        # detecting non-numeric values  in the numeric columns
        numeric_cols = ['Year', 'Kilometres', 'Price', 'Engine', 'FuelConsumption', 'CylindersinEngine', 'Doors', 'Seats']
        for column in numeric_cols:
            nan = {}
            for i, price in zip(df.index, df[column]):
                
                try:
                    float(price)
                    
                except:
                    nan[i] = price 
                    
            # removing non-numeric rows
            df.drop(list(nan.keys()), inplace=True)

        # Detecting missing data in the object columns
        categorical_columns = df.select_dtypes(include='object').columns

        missing = ['-', '0']
        for column in categorical_columns:
            nan = {}
            for i, val in zip(df.index, df[column]):
                # Sometimes the values are 0 for electric cars in FuelConsumption, we keep those
                if not ((df['FuelType'][i] == 'Electric') & (val == '0')):
                    if val in missing:
                        nan[i] = val
                    
            # Removing object columns
            df.drop(list(nan.keys()), inplace=True)

        # type conversion
        for col in numeric_cols:
            try:
                df[col] = df[col].astype(int)
            except:
                df[col] = df[col].astype(float)
                
        # renaming
        df.rename(columns={'Kilometres': 'Kilometers',
                        'Engine': 'Engine Displacement(L)',
                        'FuelConsumption': 'FuelConsumption(L)/100km'}, inplace=True)

        # Reselecting
        numeric_cols = df.select_dtypes(exclude='object').columns
        categorical_columns = df.select_dtypes(include='object').columns

        # Data Modeling:

        # Apparently, we would benefit indeed from logging the price
        df['Price'] = df["Price"].apply(np.log)

        # splitting into train-test sets
        X = df.drop(columns = ['Price'], axis =1)
        y = df['Price']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

        # Transformation pipelines
        log_pipeline = make_pipeline(
            FunctionTransformer(func=np.log, feature_names_out='one-to-one'),
            StandardScaler()
        )

        cat_pipeline = make_pipeline(
            OneHotEncoder(handle_unknown='ignore')
        )

        num_pipeline = make_pipeline(
            StandardScaler()
        )

        preprocessing = make_column_transformer(
            (num_pipeline, make_column_selector(dtype_include=np.number)),
            (cat_pipeline, make_column_selector(dtype_include=object))
        )

        return X_train, y_train, X_test, y_test, log_pipeline, preprocessing
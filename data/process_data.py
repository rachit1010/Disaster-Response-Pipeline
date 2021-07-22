 # Import all the relevant libraries
import sys
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
 
def load_data(messages_filepath, categories_filepath):
    """
    Load, merge messages and categories datasets
    
    inputs or Arguments:
    messages_filepath -> Filepath for csv file containing messages dataset.
    categories_filepath -> Filepath for csv file containing categories dataset.
    
     
    Output:
        df -> Combined data containing messages and categories
    """
    #load messages dataset
    messages = pd.read_csv(messages_filepath)
    
    #load categories dataset
    categories = pd.read_csv(categories_filepath)
    
    #Merge messages and categories dataset
    df = pd.merge(messages,categories,on='id')
    return df 

def clean_categories_data(df):
    """
    Cleaning Categories Data Function and removing duplicates
    
    Arguments:
        df -> Dataframe, containing merged data from messages and categories dataset
    Outputs:
        df -> Cleaned data which was provided in df dataframe as Arguments or input
    """
    
    # Split the categories and create dataframe for individual category
    categories = df['categories'].str.split(';',expand=True)
    
    #Fix the categories columns name
    row = categories.iloc[[1]]
    
    category_colnames = [category_name.split('-')[0] for category_name in row.values[0]]
    
    #Rename columns to categories
    categories.columns = category_colnames
    
    for column in categories:
        # Setting value to last character of string
        categories[column] = categories[column].str[-1]
        #Typecasting
        categories[column] = categories[column].astype(np.int)
    
    #Drop the categories from dataframe
    df = df.drop('categories',axis=1)
    
    #Concatenate the dataframe with new categories
    df = pd.concat([df,categories],axis=1)
    
    #Drop the duplicates
    df = df.drop_duplicates()
    
    # Remove rows with a  value of 2 from df
    df = df[df['related'] != 2]
    
    return df

def save_data(df, database_filename):
    """
    Save Data into SQLite Database
    
    Arguments:
        df: Contains cleaned data from messages and categories dataset
        database_filename: Filename for destination database
        
    Output: None    
    """
    
    engine = create_engine('sqlite:///'+ database_filename)
    table_name = database_filename.replace(".db","") + "_table"
    
    #removes table from database if same name file of database do exist
    df.to_sql(table_name, engine, index=False, if_exists='replace')

def main():
    """
    Main function performs three primary function here:
        1) Load Messages Data along with Categories
        2) Clean Categories Data
        3) Save Data to SQLite Database
    """
    
    
    # Execute the ETL pipeline if the count of arguments is matching to 4
    if len(sys.argv) == 4:

        # Extract the parameters in relevant variable
        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading messages data from {} ...\nLoading categories data from {} ...'
              .format(messages_filepath, categories_filepath))
        
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning categories data..')
        df = clean_categories_data(df)
        
        print('Saving data to DB : {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else: # Display the message if user provided some undesired input or parameters:
        print("Please provide the parameters correctly: \nSample Script Execution:\n\
> Please provide the paths of messages and categories files \n\
Arguments Description: \n\
1) Path to the CSV file containing messages (e.g. disaster_messages.csv)\n\
2) Path to the CSV file containing categories (e.g. disaster_categories.csv)\n\
3) Path to SQLite destination database (e.g. disaster_response_db.db)")

if __name__ == '__main__':
    main()

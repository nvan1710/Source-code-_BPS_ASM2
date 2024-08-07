import pandas as pd
import os
import matplotlib.pyplot as plt

def menu_options():
    print("")    
    print("----------Choose an option----------")
    print("| 1: Read .CSV Data                 |")
    print("| 2: Check the data overview        |")
    print("| 3: Check for empty values         |")
    print("| 4: Check for duplicate values     |")
    print("|---------Clean data option---------|")
    print("| 5: Delete empty data              |")
    print("| 6: Delete duplicate data          |")
    print("| 7: Delete negative number data    |")
    print("| 8: Delete special characters data |")
    print("|-----------Visualization-----------|")
    print("| 9: Plot Data                      |")
    print("|-----------------------------------|\n")


def data_action(option, file_name):
    data = pd.read_csv(file_name)
    if option == 1:
        print(data)
    elif option == 2:
        print(data.info())
    elif option == 3:
        print(data.isnull().sum())
    elif option == 4:
        print(data.duplicated().sum())
    elif option == 5:
        cleaned_data = data.dropna()
        save_path = save_cleaned_data(cleaned_data, file_name)
        print(f"Data after removing empty values saved to: {save_path}")
    elif option == 6:
        cleaned_data = data.drop_duplicates()
        save_path = save_cleaned_data(cleaned_data, file_name)
        print(f"Data after removing duplicate values saved to: {save_path}")
    elif option == 7:
        column_name = input("Enter the column name containing negative numeric data to be processed (Ex: Age): ")
        cleaned_data = data[data[column_name] >= 0]
        save_path = save_cleaned_data(cleaned_data, file_name)
        print(f"Data after removing negative numeric values data to: {save_path}")
    elif option == 8:
        column_name = input("Enter the column name containing special characters data to be processed (Ex: FirstName): ")
        special_characters_pattern = r'[^a-zA-Z0-9\s]'
        mask = data[column_name].str.contains(special_characters_pattern, na=False)
        cleaned_data = data[~mask]
        save_path = save_cleaned_data(cleaned_data, file_name)
        print(f"Data after removing special characters data saved to: {save_path}")
    elif option == 9:
        plot_data(data)
    else:
        print("Invalid Option")


def save_cleaned_data(cleaned_data, original_file_name):
    directory = os.path.dirname(original_file_name)
    base_name = os.path.basename(original_file_name)
    new_file_name = f"cleaned_{base_name}"
    save_path = os.path.join(directory, new_file_name)
    cleaned_data.to_csv(save_path, index=False)
    return save_path


def plot_data(data):
    print("---------Choose the type of plot:--------")
    print("|  1: Bar Plot                           |")
    print("|  2: Line Plot                          |")
    print("|  3: Pie Chart                          |")
    print("|----------------------------------------|\n")
    plot_type = int(input("Enter plot type number: "))

    if plot_type == 1:
        table_name_bar = input("Enter the table name for Bar Plot: ")
        column_x = input("Enter the column name for X-axis: ")
        column_y = input("Enter the column name for Y-axis (optional, leave blank for counts): ")
        if column_y:
            data.groupby(column_x)[column_y].sum().plot(kind='bar')
        else:
            data[column_x].value_counts().plot(kind='bar')
        plt.title(table_name_bar)
        plt.xlabel(column_x)
        plt.ylabel(column_y if column_y else 'Count')
        plt.show()

    elif plot_type == 2:
        table_name_line = input("Enter the table name for Line Plot: ")
        column_x = input("Enter the column name for X-axis: ")
        column_y = input("Enter the column name for Y-axis: ")
        data.plot(x=column_x, y=column_y, kind='line')
        plt.title(table_name_line)
        plt.xlabel(column_x)
        plt.ylabel(column_y)
        plt.show()

    elif plot_type == 3:
        table_name_pie = input("Enter the table name for Pie Chart: ")
        column = input("Enter the column name for pie chart: ")
        data[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title(table_name_pie)
        plt.ylabel('')
        plt.show()

    else:
        print("Invalid plot type")


def main():
    menu_options()
    option_input = int(input("Enter option: "))
    csv_file_name = input("Enter csv file name (Ex: name_file.csv): ")
    data_action(option_input, csv_file_name)
    
if __name__ == '__main__':
    main()

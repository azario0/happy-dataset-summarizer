import pandas as pd
import sys
import argparse

def generate_report(filename, output_file='report.txt', include_describe=False):
    try:
        # Read the CSV file
        df = pd.read_csv(filename)
    except Exception as e:
        print(f"Error reading the file: {e}")
        return
    
    report = ""
    # Get the list of columns
    columns = df.columns
    report += f"The columns of the dataset : \n{columns}\n\n"
    
    # Include the first three rows of the dataset
    report += "First three rows of the dataset:\n"
    report += df.head(3).to_string() + "\n\n"
    
    # Get unique values for categorical columns (object data types)
    object_dtypes = df.select_dtypes(include='object')
    for column in object_dtypes.columns:
        unique_values = df[column].unique()
        num_unique = len(unique_values)
        report += f"Unique values for column '{column}' (Count: {num_unique}):\n"
        if num_unique <= 5:
            report += f"{unique_values}\n"
        else:
            report += f"Displaying first 5 of {num_unique} unique values:\n"
            report += f"{unique_values[:5]}\n"
        report += "------------------------------\n"
    
    # Check for null values
    null_counts = df.isnull().sum()
    columns_with_nulls = null_counts[null_counts > 0]
    if columns_with_nulls.empty:
        report += "No null values in the dataset\n\n"
    else:
        report += f"Null columns : \n{columns_with_nulls}\n\n"
    
    # Conditionally include descriptive statistics
    if include_describe:
        try:
            description = df.describe().round(2)
            if not description.empty:
                report += f"Descriptive statistics:\n{description}\n"
            else:
                report += "No numerical columns to describe.\n"
        except Exception as e:
            report += f"Error generating descriptive statistics: {e}\n"
    
    # Write the report to a text file
    with open(output_file, 'w') as file:
        file.write(report)
    print(f"Report written to {output_file}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Generate a dataset report.')
    parser.add_argument('filename', type=str, help='Path to the input CSV file.')
    parser.add_argument('-d', '--describe', action='store_true', help='Include descriptive statistics in the report.')
    parser.add_argument('-o', '--output', type=str, default='report.txt', help='Path to the output report file.')
    args = parser.parse_args()
    
    # Call the generate_report function with the parsed arguments
    generate_report(args.filename, output_file=args.output, include_describe=args.describe)

if __name__ == '__main__':
    main()
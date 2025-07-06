import pandas as pd

# --- Step 1: Define the name of your HTML file ---
html_filename = 'result_data_table.html' # Make sure this file exists in the same folder

# --- Step 2: Read the HTML content from the file ---
try:
    with open(html_filename, 'r', encoding='utf-8') as f:
        html_content = f.read()
    print(f"Successfully read the file '{html_filename}'.")
except FileNotFoundError:
    print(f"Error: The file '{html_filename}' was not found.")
    print("Please make sure the HTML file is in the same directory as the script.")
    exit() # Stop the script if the file doesn't exist

# --- Step 3: Let pandas read the HTML content ---
# pd.read_html can directly parse the string variable we just created.
tables = pd.read_html(html_content)

# Select the first table found (index 0)
df = tables[0]

# --- Step 4: Clean the data (optional but recommended) ---
# Your table has two empty columns that we can drop.
# Pandas will likely name them 'Unnamed: 0' and 'Unnamed: 8'.
# We check if these columns exist before trying to drop them to avoid errors.
columns_to_drop = [col for col in ['Unnamed: 0', 'Unnamed: 8'] if col in df.columns]
if columns_to_drop:
    df_cleaned = df.drop(columns=columns_to_drop)
    print("Cleaned up unnecessary columns.")
else:
    df_cleaned = df # No columns to drop, use the original DataFrame
    print("No unnecessary columns to clean.")


# --- Step 5: Save the cleaned table to a CSV file ---
output_filename = 'race_results.csv'
df_cleaned.to_csv(output_filename, index=False, encoding='utf-8', sep=';')


print("\n--- Final Cleaned Data (first 5 rows) ---")
print(df_cleaned.head())
print(f"\n\nSuccessfully saved the cleaned table to '{output_filename}'")
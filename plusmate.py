# -*- coding: utf-8 -*-
"""PlusMate.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HCwRnpgMIG-3gN5p6R8nJVCMqchV0jgy
"""

import pandas as pd

class PandaAIAgent:
    def __init__(self, csv_path):
        """
        Initialize the Panda AI Agent with a dataset.
        :param csv_path: Path to the CSV file.
        """
        try:
            self.df = pd.read_csv(csv_path)
            print("Dataset loaded successfully!")
        except Exception as e:
            print(f"Error loading dataset: {e}")

    def show_head(self, n=5):
        """Display first n rows of the dataset."""
        return self.df.head(n)

    def get_columns(self):
        """List all column names."""
        return self.df.columns.tolist()

    def describe_data(self):
        """Show statistical summary of the dataset."""
        return self.df.describe()

    def query_data(self, column_name, value):
        """
        Query rows based on a condition.
        :param column_name: Column to filter on.
        :param value: Value to filter for.
        """
        if column_name in self.df.columns:
            result = self.df[self.df[column_name] == value]
            if result.empty:
                return "No matching records found."
            return result
        else:
            return f"Column '{column_name}' does not exist."

    def custom_query(self, query):
        """
        Run a custom query using pandas query method.
        :param query: Query string.
        """
        try:
            result = self.df.query(query)
            if result.empty:
                return "No matching records found."
            return result
        except Exception as e:
            return f"Invalid query: {e}"

    def summary(self):
        """Summarize the dataset in terms of shape and info."""
        info = str(self.df.info())
        shape = self.df.shape
        return f"Dataset contains {shape[0]} rows and {shape[1]} columns.\n\nInfo:\n{info}"


# Example usage
if __name__ == "__main__":
    # Path to CSV file
    csv_file = "meddate.csv"
    agent = PandaAIAgent(csv_file)

    # Sample interactions
    print("First 5 rows:")
    print(agent.show_head())

    print("\nColumns in dataset:")
    print(agent.get_columns())

    print("\nStatistical summary:")
    print(agent.describe_data())

    print("\nQuery example (adjust column and value as needed):")
    print(agent.query_data("column_name", "desired_value"))

    print("\nCustom query example:")
    print(agent.custom_query("age > 30"))  # Example assuming 'age' column
from util import get_logger
import pandas as pd
from llm import OpenAIChat
import uuid
import os

logger = get_logger(__name__)


class sgRNALibraryReader:
    def __init__(self):
        self.ROOT = "resources/"
        self.library = {}

    def _process_txt(self, filename):
        if filename not in self.library:

            if not os.path.exists(self.ROOT + "/" + filename):
                self.library[filename] = []
                return

            self.library[filename] = pd.read_csv(
                self.ROOT + "/" + filename, delimiter="\t"
            )
 
    def parse_knockout_library(self, system, species):
        f_sys = {"SpCas9": "SP", "SaCas9": "SA", "enCas12a": "EN"}.get(system, "")
        f_spec = {"human": "human", "mouse": "mouse"}.get(species, "")
        filename = f"KO_{f_sys}_{f_spec}.txt"
        return self.library[filename]



sgRNA_library_reader = sgRNALibraryReader()

filenames = [
    "KO_EN_human.txt",
    "KO_EN_mouse.txt",
    "KO_SA_human.txt",
    "KO_SA_mouse.txt",
    "KO_SP_human.txt",
    "KO_SP_mouse.txt",
]

for filename in filenames:
    sgRNA_library_reader._process_txt(filename)


def subset_value(df, column_name, values):
    """
    Subset the rows where the specified column matches any of the given values.

    Parameters:
    df (pd.DataFrame): The DataFrame to subset.
    column_name (str): The name of the column to match.
    values (list): A list of values to match in the specified column.

    Returns:
    pd.DataFrame: A subset of the original DataFrame with rows where the column matches any of the values.
    """
    temp_column = df[column_name].astype(str).str.lower()
    values = [val.lower() for val in values]
    return df[temp_column.isin(values)]


def sort_table(df, column_name, ascending=True):
    """
    Sort the DataFrame based on values in the specified column.

    Parameters:
    df (pd.DataFrame): The DataFrame to sort.
    column_name (str): The name of the column to sort by.
    ascending (bool): Whether to sort in ascending order (default is True).

    Returns:
    pd.DataFrame: The sorted DataFrame.
    """
    return df.sort_values(by=column_name, ascending=ascending)


def get_top_n_rows(df, n):
    """
    Get the top N rows of the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to get the top N rows from.
    n (int): The number of top rows to return.

    Returns:
    pd.DataFrame: The top N rows of the DataFrame.
    """
    return df.head(n)


def subset_between(df, column_name, x=None, y=None):
    """
    Subset the rows where the specified column's values are between x and y (inclusive).
    If x is None, it subsets only based on y. If y is None, it subsets only based on x.

    Parameters:
    df (pd.DataFrame): The DataFrame to subset.
    column_name (str): The name of the column to match.
    x (str or int or float, optional): The lower bound value. Defaults to None.
    y (str or int or float, optional): The upper bound value. Defaults to None.

    Returns:
    pd.DataFrame: A subset of the original DataFrame with rows where the column's values are between x and y.
    """
    if x is not None and y is not None:
        return df[(df[column_name] >= x) & (df[column_name] <= y)]
    elif x is not None:
        return df[df[column_name] >= x]
    elif y is not None:
        return df[df[column_name] <= y]
    else:
        raise ValueError("At least one of x or y must be provided.")


def extract_info(user_input, prompt_template, df):
    try:
        dataframe = df
        prompt = prompt_template.format(user_message=user_input)
        print(prompt)
        result = OpenAIChat.chat(prompt, use_GPT4_turbo=True)
        print(result)
        for item in result["Actions"]:
            function = item["called_function"]
            print(function)
            if function == "subset_value":
                column_name = item["column_name"]
                values = [val.strip() for val in item["matching_value"].split(",")]
                dataframe = subset_value(dataframe, column_name, values)
            if function == "sort":
                column_name = item["column_name"]
                ascending = item["ascending"]
                if ascending == "TRUE":
                    dataframe = sort_table(dataframe, column_name, ascending=True)
                else:
                    dataframe = sort_table(dataframe, column_name, ascending=False)
            if function == "get":
                num_rows = dataframe.shape[0]
                n = int(item["n"])
                print(n)
                if num_rows == 0:
                    print("error")
                if num_rows < n:
                    n = num_rows
                dataframe = get_top_n_rows(dataframe, n)
            if function == "subset_between":
                column_name = item["column_name"]
                x = None
                y = None
                if x != "NA":
                    x = int(item["x"])
                if y != "NA":
                    y = int(item["y"])
                dataframe = subset_between(df, column_name, x=x, y=y)
        return dataframe, ""
    except Exception as ex:
        print(ex)
        print("could not extract relevant info")
        dataframe = pd.DataFrame()
        return dataframe, ""

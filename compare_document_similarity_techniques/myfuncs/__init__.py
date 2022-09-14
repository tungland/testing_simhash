import pandas as pd, numpy as np, re
from copy import copy
from spacy.lang.nb.stop_words import STOP_WORDS

def deduplicate(df : pd.DataFrame) -> pd.DataFrame :
    """Remove duplicates from distance values. Also removes distance to the object themselves.

    :param df: dataframe with distance values
    :type df: pd.DataFrame
    :return: deduplicated distance values
    :rtype: pd.DataFrame
    """
    df = copy(df)
    count = 1
    for _, row in df.iterrows():
        for c in range(count):
            row.values[c] = np.nan
        count += 1
    return df

def my_tokenizer(text : str) -> list :
    """Simple tokenizer

    :param text: text to tokenize
    :type text: str
    :return: list of tokens
    :rtype: list
    """
    text = re.sub("\W", " ", text)
    lst = text.split(" ")
    clst = []
    for e in lst:
        if e != '':
            if e not in STOP_WORDS:
                e = e.lower()
                clst += [e]
    return clst


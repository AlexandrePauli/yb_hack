

import numpy
import pandas as pd


def lambda_handler(event, context):
    response = pd.DataFrame()
    print(response.text)
    return response.text


if __name__ == "__main__":
    main('', '')

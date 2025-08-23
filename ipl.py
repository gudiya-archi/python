import pandas as pd
import numpy as np

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRIaxEzb-Qy5D5usrLZlH98aVh-EmUxyAtFYj35oaIy8U6BVTCp8rBR_M3b3fHnCgz1zroEgpkz-OAu/pub?output=csv"
matches = pd.read_csv(ipl_matches)

print(matches.head())
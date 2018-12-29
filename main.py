import sys
import pandas
import numpy as np


#Reading ratings file:
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings_df = pandas.read_csv('ratings.dat', sep='::', names=r_cols,
 encoding='latin-1', engine = 'python')

 #Reading users file:
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users_df = pandas.read_csv('users.dat', sep='::', names=u_cols,
 encoding='latin-1', engine = 'python')


 #Reading items file:
i_cols = ['movie id', 'movie title']
movies_df = pandas.read_csv('movies.dat', sep='::', names=i_cols,
 encoding='latin-1', engine = 'python')


if(__name__ == "__main__"):
    print("Done ! ")
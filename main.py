import sys
import pandas
import numpy as np



def PopularItems():
    #Reading ratings file:
    r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
    ratings_df = pandas.read_csv('ratings.dat', sep='::', names=r_cols,
    encoding='latin-1', engine='python')

    #Reading users file:
    u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
    users_df = pandas.read_csv('users.dat', sep='::', names=u_cols,
    encoding='latin-1', engine='python')

    #Reading items file:
    i_cols = ['movie_id', 'movie_title', 'zab']
    movies_df = pandas.read_csv('movies.dat', sep='::', names=i_cols,
    encoding='latin-1', engine='python')

    #Hack because of the dataset
    del movies_df['zab']

    movie_id_sup3 = ratings_df.loc[ratings_df['rating'] >= 3] #keep only the movies that have better than average rating
    movie_id_sup3_count = movie_id_sup3['movie_id'].value_counts() #count number of reviews for movies

    result = pandas.DataFrame({'movie_id':movie_id_sup3_count.index, 'count':movie_id_sup3_count.values})

    mean_rating = movie_id_sup3.groupby(['movie_id'], as_index=False)['rating'].mean()
    #print(mean_rating['movie_id'].loc[mean_rating['movie_id'] == 2858], mean_rating['rating'])

    top_10_movies = result[:20] #Keep only the best 20 movies

    merged_rating = pandas.merge(top_10_movies, mean_rating, on=['movie_id'], how = 'inner')

    merged_rating['coefficient'] = merged_rating['rating'] * merged_rating['count']


    merged_df_withRating = pandas.merge(merged_rating, movies_df, on=['movie_id'], how='inner')

    #Merge dataframe on movie id to grav the movie title
    merged_df = pandas.merge(top_10_movies, movies_df, on=['movie_id'], how='inner')

    print(merged_df_withRating['movie_title'])
    print(merged_df['movie_title'])





if(__name__ == "__main__"):
    PopularItems()
    print("Done ! ")
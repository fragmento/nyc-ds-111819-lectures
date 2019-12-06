import pandas as pd
import mysql.connector
import config
import requests
import json


# fucntion to make a pandas df from a mysql query

def make_df(cursor, query):
    cursor.execute(query)
    result = cursor.fetchall()
    df = pd.DataFrame(result)
    df.columns = [x[0] for x in cursor.description]
    return(df)


def exe_query(cursor, query):
    cursor.execute(query)


def connect_db(db_name):
    cnx = mysql.connector .connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=db_name
    )


def yelp_call(url, offset):

    client_id = config.client_id
    # api_key = config.api_key

    headers = {'Authorization': 'Bearer {}'.format(config.api_key), }

    # what type of business do you want to search
    term = 'diners'

    # where do you want to perform this search
    location = 'Bedford-Stuyvesant'

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': 50,
        'offset': offset}

    response = requests.get(url, headers=headers, params=url_params)
    data = json.loads(response.text)

    return data


def parse_results(results):
    # create a container to hold our parsed data
    listdata = []

    # loop through our business and parse each individual business
    for business in results:
        biz_tuple = (business['id'],
                     business.get('name', None),
                     business.get('review_count', None),
                     business.get('price', None),
                     business.get('rating', None))
        listdata.append(biz_tuple)
    return listdata


# def get_data(cursor,url, offset):
#     # counter that will update the 'offset' value
#     total_result = []
#     #data = yelp_call(url, offset)
#     for i in range(offset, 1000, 50):
#         data = yelp_call(url, i)
#         data_parced = parse_results(data['businesses'])
#         cursor.execute( """INSERT INTO businesses
#         (id, name, review_count, price, rating)
#          VALUES (%s, %s, %s, %s, %s)""" )

        # total_result.append(data_parced)

    return total_result


def db_insert(cnx, cursor, parsed_results):
    # your code to insert and commit the results
    # I would create the connection and cursor outside of this function and
    # then pass it through
    return None


def got_review(list_id):
    headers = {'Authorization': 'Bearer {}'.format(config.api_key), }
    total_list = []
    for x in range(len(list_id)):
        new_url = 'https://api.yelp.com/v3/businesses/' + \
            list_id[x][0] + '/reviews'
        response = requests.get(new_url, headers=headers)
        data = response.json()
        review = data['reviews']
        reviews = [list_id[x][0]]
        for i in range(len(data['reviews'])):
            text_review = review[i]['text']
            reviews.append(text_review)
        total_list.append(tuple(reviews))


def get_review(list_id):
    headers = {'Authorization': 'Bearer {}'.format(config.api_key), }
    total_list = []
    for x in range(len(list_id)):
        new_url = 'https://api.yelp.com/v3/businesses/' + \
            list_id[x][0] + '/reviews'
        response = requests.get(new_url, headers=headers)
        data = response.json()
        review = data['reviews']
        total_review_tuble = []

        for i in range(len(data['reviews'])):
            rev_tup = (buz_id[x][0],
               rev_1['reviews'][i].get('id', None),
               rev_1['reviews'][i].get('rating', None),
               rev_1['reviews'][i].get('time_created', None),
               rev_1['reviews'][i].get('text', None))
            total_review_tuble.append(rev_tup)
        total_list.append(tuple(reviews))
     return(total_list)

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


def get_data(url, offset):
    # counter that will update the 'offset' value
    total_result = []
    data = yelp_call(url, offset)
    for i in range(offset, data['total'], 50):
        data = yelp_call(url, i)
        data_parced = parse_results(data['businesses'])
        total_result.append(data_parced)
    return total_result


def db_insert(cnx, cursor, parsed_results):
    # your code to insert and commit the results
    # I would create the connection and cursor outside of this function and
    # then pass it through
    return None

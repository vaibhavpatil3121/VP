import pandas as pd
from streamlit import *
import streamlit as st
import pandas as pd
import pymongo
from pymongo import MongoClient

client= MongoClient("mongodb://vaibhav_patil:Shree23121@localhost:27017/?authMechanism=DEFAULT&directConnection=true")

# db1 = client.TwitterScrapping
#
# collection_main = db1.Project
#
# df = pd.DataFrame(list(collection_main.find()))
#
# df1 = df.drop(['_id'], axis=1)


client = pymongo.MongoClient("localhost", 27017)

db = client.TwitterScrapping

collection= db.Project

host = "localhost"
port = 27017
username = "vaibhav_patil"
password = "Shree@3121"

# @st.experimental_singleton
# def init_connection():
#     return pymongo.MongoClient(**st.secrets["mongo"])
#
# client = init_connection()

#Pull data from the collection.
#Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def get_data():
    db = client.mydb
    items = db.mycollection.find()
    items = list(items)  # make hashable for st.experimental_memo
    return items

items = get_data()

# Print results.
for item in items:
    st.write(f"{item['name']} has a :{item['pet']}:")

def main():
    st.title('Search Twitter Scrapped data')
    search = st.text_input('Enter search words:')

if __name__ == '__main__':
     main()

     Button = st.button("Search")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

st.download_button(
        label="Download data as CSV",
        data='mahi',
        file_name='large_df.csv',
        mime='text/csv'
    )

#st.date_input(label="select date range",value=(datetime(2022,1,1),datetime(2025,1,1)))

start_date = st.date_input("Start Date", value=pd.to_datetime("2021-01-31", format="%Y-%m-%d"))
end_date = st.date_input("End Date", value=pd.to_datetime("today", format="%Y-%m-%d"))

    # convert the dates to string
start = start_date.strftime("%Y-%m-%d")
end = end_date.strftime("%Y-%m-%d")

#st.table(series.loc[start:end])
#
#     # [mongo]
#     # host = "localhost"
#     # port = 27017
#     # username = "xxx"
#     # password = "xxx"
#     # # To convert to a string based IO:
#     # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     # st.write(stringio)
#     #
#     # # To read file as string:
#     # string_data = stringio.read()
#     # st.write(string_data)
#     #
#     # # Can be used wherever a "file-like" object is accepted:
#     # dataframe = pd.read_csv(uploaded_file)
#     # st.write(dataframe)
#
# @st.cache
# def convert_df(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv('C:\\Users\\Daksh\\PycharmProjects\\pythonProject\\new').encode('utf-8')
#
# new=('C:\\Users\\Daksh\\PycharmProjects\\pythonProject\\app.py')
# csv = convert_df(new)
# data = 'C:\\Users\\Daksh\\PycharmProjects\\pythonProject\\app.py'

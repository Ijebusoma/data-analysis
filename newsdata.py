#!/usr/bin/env python
import psycopg2
DBNAME = "news"


def execute_query(query): #function to execute all the queries
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        db.close()
        return results
    except BaseException: #in case something goes wrong
        print("Error while perfoming database operation")


def get_articles():
    query = """select title,count(title) as views from articles,
                 log where log.path like concat('%', articles.slug)
                 group by articles.title, articles.author
                 order by views desc limit 3;"""
    articles = execute_query(query) #executes the popular article query
    for article in articles: #loop through the results fetched from the database
        print ("Article name:{}, views:{}".format(article[0], article[1])) #print output


def get_authors():
    query = """select authors.name, count(articles.author) as views from articles,authors,
            log where log.path like concat('%',articles.slug)
            and articles.author = authors.id
            group by authors.name
            order by views desc;"""
    authors = execute_query(query)
    for author in authors:
        print("{}".format(author[0])) #loop through and print out author names


def get_request():
    query = """select to_char(date,'Mon DD YYYY') AS date, err_perc
    from error_rate where err_perc > 1.0"""
    data = execute_query(query)
    for i in data:
        print("On {}, Error percent was {}".format(i[0], i[1]))
if __name__ == '__main__':
    print("------------Most Popular 3 articles by views----------")
get_articles()
print("-----------Most Popular Authors--------------")
get_authors()
print("----------Day with much error rate----------")
get_request()



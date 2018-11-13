"""
FSND - Log Analysis Project

@author: AdeebTwait
"""



import psycopg2

# Write the queries
articles_query = '''
          SELECT a.title, COUNT(*) AS views 
          FROM articles AS a JOIN log AS l
          ON CONCAT('/article/', a.slug) = l.path
          GROUP BY a.title
          ORDER BY views DESC
          LIMIT 3;
          
'''

authors_query = '''
          SELECT au.name, COUNT(*) AS views
          FROM articles AS ar 
          JOIN authors AS au
               ON au.id = ar.author
          JOIN log AS l
               ON CONCAT('/article/', ar.slug) = l.path
          GROUP BY au.name
          ORDER BY views DESC;
'''


error_query = '''
            SELECT total_req.day, (total_err.num/total_req.num)*100 AS ErrorPercentage
            FROM total_req 
            JOIN total_err
            ON total_req.day = total_err.day
            WHERE (total_err.num/total_req.num)*100 > 1;
'''


DB_NAME = "news"


def execute_query(query):
    try:
        db = psycopg2.connect(database=DB_NAME)
        cur = db.cursor
        cur.execute(query)
        result = cur.fetchall()
        db.close()
        return result
    except psycopg2.DatabaseError as error:
        print(error)


def top_articles():
    execute_query(articles_query)

def top_authors():
    execute_query(authors_query)

def error_day():
    execute_query(error_query)








if __name__ == "__main__":
    print('\n' + "**************************************")
    top_articles()
    top_authors()
    error_day()
    print("**************************************" + '\n')
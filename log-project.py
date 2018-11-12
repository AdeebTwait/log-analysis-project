import psycopg2

query1 = '''
          SELECT a.title, COUNT(*) AS views 
          FROM articles AS a JOIN log AS l
          ON CONCAT('/article/', a.slug) = l.path
          GROUP BY a.title
          ORDER BY views DESC
          LIMIT 3;
          
'''

query2 = '''
          SELECT au.name, COUNT(*) AS views
          FROM articles AS ar 
          JOIN authors AS au
               ON au.id = ar.author
          JOIN log AS l
               ON CONCAT('/article/', ar.slug) = l.path
          GROUP BY au.name
          ORDER BY views DESC;
'''


query3 = '''
            SELECT total_req.day, (total_err.num/total_req.num)*100 AS ErrorPercentage
            FROM total_req 
            JOIN total_err
            ON total_req.day = total_err.day
            WHERE (total_err.num/total_req.num)*100 > 1;
'''


if __name__ == "__main__":

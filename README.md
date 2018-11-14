CREATE VIEW total_req as
            SELECT count(*)::numeric AS num, TO_CHAR(time, 'Month DD,YYYY') AS day
            FROM log
            GROUP BY day;
            

CREATE VIEW total_err as
            SELECT count(*)::numeric AS num, TO_CHAR(time, 'Month DD,YYYY') AS day
            FROM log
            WHERE status != '200 OK'
            GROUP BY day;
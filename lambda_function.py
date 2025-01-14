'''import os
import MySQLdb

def get_db_connection():
    return MySQLdb.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        passwd=os.environ['DB_PASSWORD'],
        db=os.environ['DB_NAME']
    )
'''
def lambda_handler(event, context):
    try:
        '''
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT NOW()")
            result = cursor.fetchone()
        conn.close()
        '''
        
        return {
            'statusCode': 200,
            'body': f'Database connection successful! Current time: {result[0]}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error connecting to database: {str(e)}'
        }

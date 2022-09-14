from influxdb import InfluxDBClient

def main():
    
    '''Instantiate a connection to the InfluxDB.'''

    host = 'localhost'
    port = 8086

    dbname = 'gizmo'
    query = 'select * from gizmo_new'

    client = InfluxDBClient(host='localhost', port=8086, database = 'gizmo')

    print('Querying data: ' + query)
    result = client.query(query)

    for point in result.get_points():
        print(point)

if __name__ == '__main__':
    main()

# Start Zookeeper
sudo bin/zookeeper-server-start.sh config/zookeeper.properties 

#Start Kafka-Server
sudo bin/kafka-server-start.sh config/server.properties

#Add Mysql Connect Properties in following path
.
├── bin
├── config
├── connectors
├── libs
├── LICENSE
├── licenses
├── logs
├── mysql-connector.properties
├── NOTICE
└── site-docs

#In mysql-connector.properties add appropriate configurations

        name=live_data_1
        connector.class=io.confluent.connect.jdbc.JdbcSourceConnector

        # Connection settings
        connection.url=jdbc:mysql://localhost:3306/kafka_db
        connection.user=root
        connection.password=1234

        # Table settings
        mode=incrementing
        incrementing.column.name=unique_id
        table.whitelist=cricket_match_data_live_1

        # Topic settings
        topic.prefix=mysql_live_
        tasks.max=3


#Start kafka connect 
sudo bin/connect-standalone.sh config/connect-standalone.properties mysql-connector.properties 

# Check status of connector
curl http://localhost:8083/connectors/live_data_1/status


#Successfull connection will give the following output

{
  "name": "live_data_1",
  "connector": {
    "state": "RUNNING",
    "worker_id": "127.0.1.1:8083"
  },
  "tasks": [
    {
      "id": 0,
      "state": "RUNNING",
      "worker_id": "127.0.1.1:8083"
    }
  ],
  "type": "source"
}

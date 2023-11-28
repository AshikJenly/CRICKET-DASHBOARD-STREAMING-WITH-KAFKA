# Cricket Dashboard Streaming with Kafka

## Tools Used

- **Operating System**
  - Ubuntu

- **Programming Languages**
  - Python

- **Big Data Tools**
  - Kafka

- **Database**
  - MySQL

- **Other Libraries**
  - StreamLit

## Project Architecture
[docs.odg](https://github.com/AshikJenly/CRICKET-DASHBOARD-STREAMING-WITH-KAFKA/files/13490269/docs.odg)


## How to Execute the Project

1. **Start Zookeeper:**
    ```bash
    sudo bin/zookeeper-server-start.sh config/zookeeper.properties
    ```

2. **Start Kafka-Server:**
    ```bash
    sudo bin/kafka-server-start.sh config/server.properties
    ```

3. **Add MySQL Connect Properties in the following path (Custom path is also okay, add that path in upcoming steps):**
    ```
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
    ```

4. **In `mysql-connector.properties`, add appropriate configurations:**
    ```properties
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
    ```

5. **Start Kafka Connect:**
    ```bash
    sudo bin/connect-standalone.sh config/connect-standalone.properties mysql-connector.properties
    ```

6. **Check the status of the connector:**
    ```bash
    curl http://localhost:8083/connectors/live_data_1/status
    ```

    Successful connection will give the following output:
    ```json
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
    ```

## Sample Output
![Screenshot from 2023-11-27 22-31-30](https://github.com/AshikJenly/CRICKET-DASHBOARD-STREAMING-WITH-KAFKA/assets/116492348/302a0dd2-5df8-44fe-8632-15586899a6a5)

![Screenshot from 2023-11-27 22-32-28](https://github.com/AshikJenly/CRICKET-DASHBOARD-STREAMING-WITH-KAFKA/assets/116492348/915a955f-1ee1-40df-8d6e-7b8b5033d98a)
![Screenshot from 2023-11-27 22-45-01](https://github.com/AshikJenly/CRICKET-DASHBOARD-STREAMING-WITH-KAFKA/assets/116492348/52793e12-6bc4-49bf-8ba9-f1c5b595f041)

![Screenshot from 2023-11-27 22-45-21](https://github.com/AshikJenly/CRICKET-DASHBOARD-STREAMING-WITH-KAFKA/assets/116492348/81cfb0ec-815f-4fb0-adfe-3865840080b9)




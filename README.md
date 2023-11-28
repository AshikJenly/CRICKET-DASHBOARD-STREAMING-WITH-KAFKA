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

![Project Architecture](docs/docs.odg)

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

![Sample Output 1](<Screenshot from 2023-11-27 22-31-30.png>)
![Sample Output 2](<Screenshot from 2023-11-27 22-32-28.png>)
![Sample Output 3](<Screenshot from 2023-11-27 22-45-01.png>)
![Sample Output 4](<Screenshot from 2023-11-27 22-45-21.png>)

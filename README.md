### src

- https://github.com/MarMaksk/kafka-cluster/tree/main
- https://habr.com/ru/companies/slurm/articles/717066/
- https://developer.confluent.io/get-started/python/?_ga=2.92745119.32664500.1702735601-1019688679.1702735601&_gl=1*nso63a*_ga*MTAxOTY4ODY3OS4xNzAyNzM1NjAx*_ga_D2D3EGKSGD*MTcwMjczNTYwMC4xLjEuMTcwMjczNTYwMy41Ny4wLjA.#kafka-setup
- https://stackoverflow.com/questions/53586130/kafka-topic-creation-timed-out-waiting-for-a-node-assignment

### commands

- **Topic info:** `sh kafka-topics.sh --describe --topic MyTestTopic --bootstrap-server localhost:29092`
- **Send message to the topic:** `sh kafka-console-producer.sh --topic MyTestTopic --bootstrap-server localhost:29092`
- **Read messages from topic:** `sh kafka-console-consumer.sh --topic MyTestTopic --bootstrap-server localhost:29092 --from-beginning --group my_group`
- **Reset offsets for the group:** `sh kafka-consumer-groups.sh --bootstrap-server localhost:29092 --group my_group --reset-offsets --to-earliest --topic MyTestTopic --execute`
- **Show offsets for the group:** `sh kafka-consumer-groups.sh --bootstrap-server localhost:29092 --group my_group --describe`

    

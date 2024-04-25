#!/usr/bin/env python
import pika, sys, os, json
from pymongo import MongoClient

def main():
    client = MongoClient("mongodb://mongodb:27017")
    db = client.StudentManagement
    collection = db.students

    connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='update_data', durable=True)

    def update_data(ch, method, properties, body):
        data = json.loads(body)
        filter_query = {"srn": data["srn"]}  # Assuming 'srn' is the unique identifier
        update_query = {"$set": {"name": data["name"], "section": data["section"]}}  # Update fields as needed
        result = collection.update_one(filter_query, update_query)
        
        if result.modified_count == 1:
            print(f"[x] Updated record for SRN: {data['srn']}")
        else:
            print(f"[!] Failed to update record for SRN: {data['srn']}")

    channel.basic_consume(queue="update_data", on_message_callback=update_data, auto_ack=True)

    print('[*] Update Data: Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()

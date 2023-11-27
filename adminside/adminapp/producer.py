# amqps://iggiivmd:W-MSVEIraHIRql_MsV720W7f3GPuQCEc@puffin.rmq2.cloudamqp.com/iggiivmd

import pika, json

params = pika.URLParameters('amqps://iggiivmd:W-MSVEIraHIRql_MsV720W7f3GPuQCEc@puffin.rmq2.cloudamqp.com/iggiivmd')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    print('bbbbbbbbbb')
    assert isinstance(method, str), "Method must be a string"
    properties = pika.BasicProperties(content_type='application/json',
                                      delivery_mode=2) 
    channel.basic_publish(exchange='', routing_key='user',
                          body=json.dumps(body), properties=properties)

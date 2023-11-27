
import pika, json

params = pika.URLParameters('amqps://iggiivmd:W-MSVEIraHIRql_MsV720W7f3GPuQCEc@puffin.rmq2.cloudamqp.com/iggiivmd')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    print('hgerjdghlgub')
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', \
    body=json.dumps(body), properties=properties) 


# def consume_response():
#     method_frame, header_frame, body = channel.basic_get(queue='admin_response', auto_ack=True)
#     if method_frame:
#         response_data = json.loads(body)
#         return response_data
#     return None
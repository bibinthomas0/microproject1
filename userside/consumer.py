import pika, json, os, django
from django.http import JsonResponse
from requests import Response
# from userss.api.views import PostListingView
# from rest_framework.views import APIView


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "userside.settings")
django.setup()
params = pika.URLParameters('amqps://iggiivmd:W-MSVEIraHIRql_MsV720W7f3GPuQCEc@puffin.rmq2.cloudamqp.com/iggiivmd')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='user')


def callback(ch, method, properties, body):
    print('Received in Django microservice')
    print(body)
    data = json.loads(body)
    print('Added a comment')
    # api_view = PostListingView.as_view()
    # request = APIView().initialize_request(None)
    # response = Response(data)
    # final_response = api_view(request)

channel.basic_consume(queue='user', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
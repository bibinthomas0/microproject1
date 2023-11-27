import pika, json, os, django




os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adminside.settings")
django.setup()

from django.http import JsonResponse
from adminapp.models import Adminpost,Likedetails
from adminapp.api.views import ProductViewSet
from adminapp.producer import publish


params = pika.URLParameters('amqps://iggiivmd:W-MSVEIraHIRql_MsV720W7f3GPuQCEc@puffin.rmq2.cloudamqp.com/iggiivmd')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')




def callback(ch, method, properties, body):
    print('Received in admin')
    data = json.loads(body)
    print('hhhhhhhh',properties.content_type)
    if properties.content_type == 'product_request':
        product_viewset = ProductViewSet()
        data = product_viewset.list(request=None)
        print(data.data)
        publish(body = data.data,method='posts_reponse')
    elif properties.content_type == 'add_like':
        print(data['post'])
        k = data['post']
        user = data['user']
        post = Adminpost.objects.get(id=k)
        post.Total_likes = (post.Total_likes)+1
        post.save()
        Likedetails.objects.create(post=post,user=user)
        print("like added")
        
        
# def publish_response(data):
#     print('Publishing response to admin_response')
#     properties = pika.BasicProperties(content_type='application/json')
#     channel.basic_publish(exchange='', routing_key='admin_response', body=json.dumps(data), properties=properties)
    
    
channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
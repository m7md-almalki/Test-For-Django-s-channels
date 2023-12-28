from django.shortcuts import render
from django.views import View


from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your views here.


class home(View):
    def get(self, request):
        return render(request=request , template_name="chat/home.html")





class sender(View):
    def get(self, request):
        return render(request=request , template_name="chat/sender.html")



    def post(self, request):
        input_value = request.POST["input_value"]

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            '{}'.format("test"),
            {
                'type': 'chat_message',
                'message': input_value
            }
        )
        
        return render(request=request , template_name="chat/sender.html")
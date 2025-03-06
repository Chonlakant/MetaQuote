from rest_framework.decorators import api_view
from rest_framework.response import Response

from cryptoarchive.users.tasks import save_exchange_list


@api_view(['POST'])
def receive_post_request(request) -> Response:
    if request.method == 'POST':
        save_exchange_list.delay(request.data)
        return Response({"message": "Get some data", "data": request.data}, status=200)

from rest_framework.decorators import api_view
from rest_framework.response import Response

from cryptoarchive.users.tasks import save_exchange_list
from cryptoarchive.users.tasks import save_swap_transaction


@api_view(["POST"])
def receive_post_request(request) -> Response:
    save_exchange_list.delay(request.data)
    return Response({"message": "Get some data", "data": request.data}, status=200)


@api_view(["POST"])
def receive_swap_transaction(request) -> Response:
    save_swap_transaction.delay(request.data)
    return Response({"message": "Get some data", "data": request.data}, status=200)

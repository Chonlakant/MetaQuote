import typing as typ

from celery import shared_task

from ..exchanges.api.serializers import ExchangeSerializer


@shared_task()
def save_exchange_list(list_data: typ.List[typ.Dict]):
    for exchange in list_data:
        serializer = ExchangeSerializer(data=exchange)
        serializer.is_valid(raise_exception=False)
        serializer.save()
    return True

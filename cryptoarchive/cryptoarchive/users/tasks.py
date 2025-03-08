from celery import shared_task

from cryptoarchive.exchanges.api.serializers import ExchangeSerializer
from cryptoarchive.exchanges.api.serializers import SwapTransactionSerializer
from cryptoarchive.exchanges.models import Exchange
from cryptoarchive.exchanges.models import SwapTransaction

ModelType = type[Exchange] | type[SwapTransaction]
SerializerType = type[ExchangeSerializer] | type[SwapTransactionSerializer]


def generic_bulk_create(
    list_data: list[dict],
    model: ModelType,
    serializer: SerializerType,
):
    exchange_to_create = []
    for exchange_data in list_data:
        serializer_instance = serializer(data=exchange_data)
        if serializer_instance.is_valid():
            exchange_to_create.append(
                model(
                    **serializer_instance.validated_data,
                ),
            )
    if exchange_to_create:
        model.objects.bulk_create(exchange_to_create)
    return True


@shared_task()
def save_exchange_list(list_data: list[dict]):
    """Save a list of exchange data to the database using bulk_create."""
    return generic_bulk_create(list_data, Exchange, ExchangeSerializer)


@shared_task()
def save_swap_transaction(list_data: list[dict]):
    """Save a list of SwapTransaction to the database using bulk_create."""
    return generic_bulk_create(list_data, SwapTransaction, SwapTransactionSerializer)

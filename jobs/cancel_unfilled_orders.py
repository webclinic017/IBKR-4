from ibkr.models import CancelOrder

from modules import common


@common.job("Cancel Unfilled Orders")
def do() -> None:
    CancelOrder.all_unfilled_orders()


if __name__ == "__main__":
    do()

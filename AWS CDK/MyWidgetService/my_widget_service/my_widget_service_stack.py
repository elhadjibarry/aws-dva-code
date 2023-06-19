from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from . import widget_service

class MyWidgetServiceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        widget_service.WidgetService(self, "Widgets")

        # example resource
        # queue = sqs.Queue(
        #     self, "MyWidgetServiceQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

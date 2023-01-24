from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_s3 as s3,
    aws_s3_notifications as s3n,
    aws_lambda_event_sources as lambda_event_sources,
    aws_lambda as lambda_,
    aws_lambda_python_alpha as python_lambda_
)
from constructs import Construct

class PythonCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        my_lambda = lambda_.Function(
            self, 'HelloHandler',
            runtime=lambda_.Runtime.PYTHON_3_8,
            code=lambda_.Code.from_asset('lambda'),
            handler='index.handler',
        )

        # my_lambda = python_lambda_.PythonFunction(self, "HelloHandler2",
        #     entry="lambda",
        #     runtime=lambda_.Runtime.PYTHON_3_8,
        # )

        # example resource
        # queue = sqs.Queue(
        #     self, "PythonCdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        # sqs_event_source = lambda_event_sources.SqsEventSource(queue)
        # my_lambda.add_event_source(sqs_event_source)

        # bucket = s3.Bucket(self, "MyEncryptedBucket",
        #     encryption=s3.BucketEncryption.KMS
        # )
        # bucket.add_event_notification(s3.EventType.OBJECT_CREATED, s3n.SqsDestination(queue))

        # bucket_event_source = lambda_event_sources.S3EventSource(bucket,
        #     events=[s3.EventType.OBJECT_CREATED, s3.EventType.OBJECT_REMOVED],
        # )
        # my_lambda.add_event_source(bucket_event_source)

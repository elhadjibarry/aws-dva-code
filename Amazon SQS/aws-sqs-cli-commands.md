## AWS SQS CLI Commands

aws sqs list-queues

aws sqs send-message --queue-url https://sqs.us-east-1.amazonaws.com/291934546285/my-std-queue --message-body test-message-1 --delay-seconds 10

aws sqs receive-message --queue-url https://sqs.us-east-1.amazonaws.com/291934546285/my-std-queue --wait-time-seconds 10

aws sqs send-message --queue-url https://sqs.us-east-1.amazonaws.com/291934546285/my-std-queue --message-body test-long-short-polling
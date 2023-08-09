trap 'printf "\n"' DEBUG

sudo yum install jq -y

AccountId=$(aws sts get-caller-identity | jq -r .Account)
labdatabucket=$(aws s3api list-buckets --query "Buckets[?contains(Name, 'labdatabucket')]" | jq -r .[].Name)
KeyId=$(aws kms list-aliases --region us-east-1 --query "Aliases[?contains(AliasName,'S3EncryptionKey')]" | jq -r .[].TargetKeyId)

aws s3api put-bucket-encryption \
--bucket $labdatabucket \
--server-side-encryption-configuration '{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "aws:kms", "KMSMasterKeyID": "arn:aws:kms:us-east-1:${AccountId}:alias/S3EncryptionKey"}}]}'

truncate -s 1M 1mTestFile
ll -h

aws s3 cp 1mTestFile s3://$labdatabucket/ --sse-kms-key-id $KeyId --sse=aws:kms

labdatabucket=$(aws s3api list-buckets --query "Buckets[?contains(Name, 'labdatabucket')]" | jq -r .[].Name)
aws s3api get-bucket-policy --bucket $labdatabucket | jq -r .Policy | jq . > policy.json

aws s3api put-bucket-policy --policy file://policy.json --bucket $labdatabucket

truncate -s 10M 10mTestFile
ll -h

aws s3 cp 10mTestFile s3://$labdatabucket/

aws s3 cp 10mTestFile s3://$labdatabucket/ --sse-kms-key-id $KeyId --sse=aws:kms

aws s3 cp s3://$labdatabucket/10mTestFile downloadTest
ll -h

sha512sum 10mTestFile
sha512sum downloadTest


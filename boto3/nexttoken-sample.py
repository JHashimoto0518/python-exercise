import sys
import boto3

# usage:
# python3 nexttoken-sample.py <profile_name>
#
# output:
# {'logGroups': [], 'ResponseMetadata': {'RequestId': 'ee66ee68-729e-4f15-804d-1b4c372e085f', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'ee66ee68-729e-4f15-804d-1b4c372e085f', 'content-type': 'application/x-amz-json-1.1', 'content-length': '16', 'date': 'Mon, 04 Mar 2024 22:59:05 GMT'}, 'RetryAttempts': 0}}
# end first response
# start next token loop

profile_name = sys.argv[1]

session = boto3.Session(region_name="ap-southeast-1", profile_name=profile_name)
client = session.client("logs")
response = client.describe_log_groups()

print(response)
print("end first response")

print("start next token loop")
while "nextToken" in response:
    response = client.describe_log_groups(nextToken=response["nextToken"])
    print(response)

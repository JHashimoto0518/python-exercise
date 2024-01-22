import boto3

client = boto3.client("logs")
response = client.describe_log_groups()

print(response)
print("end first response")
print("Next token: " + response["nextToken"])

print("start next token loop")
while "nextToken" in response:
    response = client.describe_log_groups(nextToken=response["nextToken"])
    print(response)

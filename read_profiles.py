import klaviyo
import json

f = open('credentials.json')
klaviyo_credentials = json.load(f)
pub_token = klaviyo_credentials['public_token']
pri_token = klaviyo_credentials['private_token']
f.close()

client = klaviyo.Klaviyo(public_token=pub_token, private_token=pri_token)

# to get all lists
my_lists = client.lists()

print(my_lists)
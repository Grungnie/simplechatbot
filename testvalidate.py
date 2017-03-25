import requests

openid_metadata_url = "https://login.botframework.com/v1/.well-known/openidconfiguration"
openid_metadata = requests.get(openid_metadata_url)
print(openid_metadata.text)

valid_signing_keys_url = openid_metadata.json()["jwks_uri"]
valid_signing_keys = requests.get(valid_signing_keys_url)
print(valid_signing_keys.text)



# 1. The token was sent in the HTTP Authorization header with “Bearer” scheme
# 2. The token is valid JSON that conforms to the JWT standard (see references)
# 3. The token contains an issuer claim with value of https://api.botframework.com
# 4. The token contains an audience claim with a value equivalent to your bot’s Microsoft App ID.
# 5. The token has not yet expired. Industry-standard clock-skew is 5 minutes.
# 6. The token has a valid cryptographic signature with a key listed in the OpenId keys document retrieved in step 1, above.

# If any fail return 403

import json
import boto3
import qrcode
import io
import base64

# Initialize a session using Amazon S3
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Parse the URL from the event
    body = json.loads(event['body'])
    url = body['url']
    
    # Generate QR code
    img = qrcode.make(url)
    img_bytes = io.BytesIO()
    img.save(img_bytes)
    img_bytes = img_bytes.getvalue()
    
    # Generate a unique filename
    filename = url.split("://")[1].replace("/", "_") + '.png'
    
    # Upload the QR code to the S3 bucket
    s3.put_object(Bucket='py-qr-code-generator', Key=filename, Body=img_bytes, ContentType='image/png', ACL='public-read')
    
    # Generate the URL of the uploaded QR code
    location = s3.get_bucket_location(Bucket='py-qr-code-generator')['LocationConstraint']
    region = '' if location is None else f'{location}'
    qr_code_url = f"https://s3-{region}.amazonaws.com/{'py-qr-code-generator'}/{filename}"
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'QR code generated and uploaded to S3 bucket successfully!', 'qr_code_url': qr_code_url})
    }


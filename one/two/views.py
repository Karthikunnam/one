from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def welcome_view(request):
    return render(request, 'a.html')
def first_view(request):
    return render(request, 'three.html')    


# payments/views.py


def p_view(request):
    if request.method == 'POST':
        # Access form data
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        upi_id = request.POST.get('upi_id')
        public_message_to_sns()

        
        # Print form data to console
        print("Name:", name)
        print("Mobile Number:", mobile_number)
        print("UPI ID:", upi_id)
        
        # Implement logic to send payment request
        
        return render(request, 'three.html')  # Redirect to success page
    else:
        return render(request, 'three.html') 




import boto3

def public_message_to_sns():
    topic_arn = "arn:aws:sns:ap-south-1:767397686043:first"

# Region name where the SNS topic resides
    region_name = "ap-south-1"
    aws_access_key_id = "AKIA3FLDXNMNSHZBF7HZ"
    aws_secret_access_key = "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"
    # Initialize SNS client with the specified region and credentials
    sns_client = boto3.client(
        'sns',
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # Publish message to SNS topic
    message="Registartion successful"
    try:
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message
        )
        print("Message published successfully:", response)
    except Exception as e:
        print("Failed to publish message:", str(e))






    
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def welcome_view(request):
    return render(request, 'a.html')
def first_view(request):
    return render(request, 'two.html')  
def second_view(request):
    return render(request, 'three.html')

def third_view(request):
    return render(request, 'four.html')
    

# payments/views.py


def third_view(request):
    if request.method == 'POST':
        # Access form data
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        upi_id = request.POST.get('upi_id')
        
        # Print form data to console
        print("Name:", name)
        print("Mobile Number:", mobile_number)
        print("UPI ID:", upi_id)
        public_message_to_sns()
        # Implement logic to send payment request
        
        return render(request, 'four.html')  # Redirect to success page
    else:
        return render(request, 'four.html')   




import boto3

def public_message_to_sns():
    # Initialize SNS client with the specified region and credentials
    sns_client = boto3.client(
        'sns',
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # Publish message to SNS topic
    try:
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message
        )
        print("Message published successfully:", response)
    except Exception as e:
        print("Failed to publish message:", str(e))

# Assigning the message to the variable
message = "New registration arrived"

# ARN of your SNS topic
topic_arn = "arn:aws:sns:ap-south-1:767397686043:first"

# Region name where the SNS topic resides
region_name = "ap-south-1"
aws_access_key_id = "AKIA3FLDXNMNSHZBF7HZ"
aws_secret_access_key = "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"

public_message_to_sns()


# Call the function with the message, topic ARN, region name, and credentials
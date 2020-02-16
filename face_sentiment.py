import boto3
import csv


def face_recognizer():
    with open('aws/credentials.csv', 'r') as input:
        next(input)
        reader = csv.reader(input)
        for line in reader:
            access_key_id = line[0]
            secret_access_key = line[1]

    photo = 'smile_guy.jpg'

    client = boto3.client('rekognition',
                          aws_access_key_id = access_key_id,
                          aws_secret_access_key = secret_access_key,
                          region_name='us-east-2'
                          )

    response = client.detect_faces(Image={'S3Object': {
        'Bucket': 'face-pictures',
        'Name': photo
    }},
        Attributes=['ALL']
    )

    for key, value in response.items():
        if key == 'FaceDetails':
            for people_attributes in value:
                print(people_attributes)
                print("---")

    return None


if __name__ == '__main__':
    face_recognizer()

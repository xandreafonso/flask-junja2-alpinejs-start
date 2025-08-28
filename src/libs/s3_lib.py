import os
import boto3
from botocore.exceptions import ClientError
from typing import Optional, Dict, Any, Union, BinaryIO
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class S3Client:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
            region_name=os.environ['AWS_DEFAULT_REGION'],
            endpoint_url=os.environ.get('AWS_S3_ENDPOINT')
        )
        self.bucket_name = os.environ['AWS_BUCKET_NAME']

    def upload_file_to_bucket(
        self,
        key: str,
        file_content: Union[bytes, str, BinaryIO],
        content_type: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        try:
            extra_args = {}
            
            if content_type:
                extra_args['ContentType'] = content_type
                
            if metadata:
                extra_args['Metadata'] = metadata

            if isinstance(file_content, str):
                file_content = file_content.encode('utf-8')
            
            if isinstance(file_content, bytes):
                from io import BytesIO
                file_content = BytesIO(file_content)

            response = self.s3_client.upload_fileobj(
                file_content,
                self.bucket_name,
                key,
                ExtraArgs=extra_args
            )

            head_response = self.s3_client.head_object(Bucket=self.bucket_name, Key=key)
            
            return {
                'success': True,
                'ETag': head_response.get('ETag')
            }
        except ClientError as error:
            logger.error(f"Error on upload S3 object: {error}")
            raise error

    def generate_presigned_upload_url(
        self,
        key: str,
        expires_in: int = 3600
    ) -> str:
        return self.s3_client.generate_presigned_url(
            'put_object',
            Params={'Bucket': self.bucket_name, 'Key': key},
            ExpiresIn=expires_in
        )

    def generate_presigned_download_url(
        self,
        download_name: str,
        key: str,
        expires_in: int = 3600
    ) -> str:
        return self.s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': self.bucket_name,
                'Key': key,
                'ResponseContentDisposition': f'attachment; filename="{download_name}"'
            },
            ExpiresIn=expires_in
        )

    def generate_presigned_url_object(
        self,
        key: str,
        expires_in: int = 3600
    ) -> str:
        return self.s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': self.bucket_name, 'Key': key},
            ExpiresIn=expires_in
        )

    def get_object(self, key: str) -> bytes:
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=key)
            
            if 'Body' not in response:
                raise Exception("Objeto não encontrado")
                
            return response['Body'].read()
        except ClientError as error:
            logger.error(f"Error on get S3 object: {error}")
            raise error

    def persist_object(self, key: str, object_file_path: str) -> None:
        try:
            self.s3_client.download_file(self.bucket_name, key, object_file_path)
        except ClientError as error:
            logger.error(f"Error persisting S3 object: {error}")
            raise error

    def delete_object(self, key: str) -> bool:
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=key)
            return True
        except ClientError as error:
            logger.error(f"Error on delete S3 object: {error}")
            raise error

    def delete_directory(self, prefix: str) -> Dict[str, Any]:
        try:
            normalized_prefix = prefix if prefix.endswith('/') else f"{prefix}/"
            
            paginator = self.s3_client.get_paginator('list_objects_v2')
            pages = paginator.paginate(Bucket=self.bucket_name, Prefix=normalized_prefix)
            
            total_deleted = 0
            
            for page in pages:
                if 'Contents' not in page or not page['Contents']:
                    continue
                    
                objects_to_delete = [{'Key': obj['Key']} for obj in page['Contents']]
                
                if objects_to_delete:
                    delete_response = self.s3_client.delete_objects(
                        Bucket=self.bucket_name,
                        Delete={
                            'Objects': objects_to_delete,
                            'Quiet': False
                        }
                    )
                    
                    total_deleted += len(objects_to_delete)
            
            return {
                'success': True,
                'total_deleted': total_deleted
            }
        except ClientError as error:
            logger.error(f"Error on delete S3 directory: {error}")
            raise error



s3 = S3Client()

if __name__ == "__main__":
    # Upload a file
    # result = s3.upload_file_to_bucket(
    #     key="test/example.txt",
    #     file_content=b"Hello, World!",
    #     content_type="text/plain"
    # )
    
    # Generate presigned URLs
    # upload_url = s3.generate_presigned_upload_url("test/upload.txt")
    # download_url = s3.generate_presigned_download_url("myfile.txt", "test/example.txt")
    
    # Get object
    # content = s3.get_object("test/example.txt")
    
    # Delete object
    # s3.delete_object("test/example.txt")
    
    # Delete directory
    # s3.delete_directory("test")
    
    pass
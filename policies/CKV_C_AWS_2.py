from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class UnencryptedS3Bucket(BaseResourceCheck):
    def __init__(self):
        name = "Ensure S3 bucket is encrypted at rest"
        id = "CKV_C_AWS_2"
        supported_resources = ['aws_s3_bucket']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
    def scan_resource_conf(self, conf):
        if 'server_side_encryption_configuration' not in conf.keys():
            return CheckResult.FAILED
        
        return CheckResult.PASSED
        
scanner = UnencryptedS3Bucket()
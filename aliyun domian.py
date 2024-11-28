import time
import sys

from alibabacloud_domain20180129.client import Client as Domain20180129Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_domain20180129 import models as domain_20180129_models
from alibabacloud_tea_util import models as util_models


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> Domain20180129Client:
        """
        使用AK&SK初始化账号Client
        @return: Client
        @throws Exception
        """
        # 填入您的阿里云Access Key ID和Access Key Secret
        ALIBABA_CLOUD_ACCESS_KEY_ID = ""
        ALIBABA_CLOUD_ACCESS_KEY_SECRET = ""

        config = open_api_models.Config(
            access_key_id=ALIBABA_CLOUD_ACCESS_KEY_ID,
            access_key_secret=ALIBABA_CLOUD_ACCESS_KEY_SECRET
        )
        # 设置Endpoint
        config.endpoint = 'domain.aliyuncs.com'
        return Domain20180129Client(config)

    @staticmethod
    def check_domain_availability(domain_name: str) -> str:
        client = Sample.create_client()
        check_domain_request = domain_20180129_models.CheckDomainRequest(
            domain_name=domain_name
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = client.check_domain_with_options(check_domain_request, runtime)
            avail = getattr(response.body, 'avail', None)
            if avail == 1:
                return f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {domain_name} - 可以注册"
            else:
                return f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {domain_name} - 不可注册"
        except Exception as e:
            return f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {domain_name} - 查询异常 - {e}"


if __name__ == '__main__':
    domain_name = '261111.xyz'
    while True:
        result = Sample.check_domain_availability(domain_name)
        print(result)
        time.sleep(0.5)

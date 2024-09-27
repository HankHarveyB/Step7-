import string
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.tmt.v20180321 import tmt_client, models 
SecretId = "<替换为你自己的腾讯云ID>"
SecretKey = "<替换为你自己的腾讯云Key>"

def string_lengthLimit(input_string):
    # 使用下划线分割字符串
    parts = input_string.split('_')
    
    # 如果字符串总长度大于24
    if len(input_string) > 24:
        # 取每个部分的前4个字符
        parts = [part[:4] for part in parts]
        # 重新拼接成新的字符串
        input_string = '_'.join(parts)
        
    # 如果仍然大于24，则取每个部分的前3个字符
    if len(input_string) > 24:
        parts = [part[:3] for part in parts]
        input_string = '_'.join(parts)
        # 如果仍然大于24，则取每个部分的前2个字符
    if len(input_string) > 24:
        parts = [part[:2] for part in parts]
        input_string = '_'.join(parts)
    if len(input_string) > 24:
        parts = [part[:1] for part in parts]
        input_string = '_'.join(parts)
    
    return input_string




def process_string(text:string):
        # 删除字符串中的#
        text = text.replace('#', '')
        text=text.replace('>', '_M_')
        text=text.replace('<', '_L_')
        # 检查字符串是否以数字开头
        if text and text[0].isdigit():
            # 获取开头的数字部分
            number_part = ''
            while text and text[0].isdigit():
                number_part += text[0]
                text = text[1:]
            # 返回处理后的字符串
            return (text.strip() + '_' + number_part).lstrip('_')
        else:
            return text.strip().lstrip('_')

class Translator:
    def __init__(self, from_lang, to_lang):
        self.from_lang = from_lang
        self.to_lang = to_lang

    def translate(self, text):
        try: 
            cred = credential.Credential(SecretId, SecretKey)
            httpProfile = HttpProfile()
            httpProfile.endpoint = "tmt.tencentcloudapi.com"

            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = tmt_client.TmtClient(cred, "ap-beijing", clientProfile) 

            req = models.TextTranslateRequest()
            req.SourceText = text
            req.Source = self.from_lang
            req.Target = self.to_lang
            req.ProjectId = 0

            resp = client.TextTranslate(req) 
            return resp.TargetText

        except TencentCloudSDKException as err: 
            return err
    

if __name__ == '__main__':
    # translator = Translator(from_lang="en", to_lang="zh")
    # print(translator.translate("Hello, world!"))
    
    # input_string = "1#_hello world"
    # output = process_string(input_string)
    # print(output)  # 输出: hello_world_123
    # name = "Alice"
    # age = 30

    # greeting = f"Hello, my name is {name}.\nI am {age} years old."
    # print(greeting)
    

    input_str = "abcdefgh_ijklmnop_qrstuvwx_yz0123_12"
    output_str = string_lengthLimit(input_str)
    print(output_str)

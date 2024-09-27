import string
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.tmt.v20180321 import tmt_client, models 
SecretId = "<�滻Ϊ���Լ�����Ѷ��ID>"
SecretKey = "<�滻Ϊ���Լ�����Ѷ��Key>"

def string_lengthLimit(input_string):
    # ʹ���»��߷ָ��ַ���
    parts = input_string.split('_')
    
    # ����ַ����ܳ��ȴ���24
    if len(input_string) > 24:
        # ȡÿ�����ֵ�ǰ4���ַ�
        parts = [part[:4] for part in parts]
        # ����ƴ�ӳ��µ��ַ���
        input_string = '_'.join(parts)
        
    # �����Ȼ����24����ȡÿ�����ֵ�ǰ3���ַ�
    if len(input_string) > 24:
        parts = [part[:3] for part in parts]
        input_string = '_'.join(parts)
        # �����Ȼ����24����ȡÿ�����ֵ�ǰ2���ַ�
    if len(input_string) > 24:
        parts = [part[:2] for part in parts]
        input_string = '_'.join(parts)
    if len(input_string) > 24:
        parts = [part[:1] for part in parts]
        input_string = '_'.join(parts)
    
    return input_string




def process_string(text:string):
        # ɾ���ַ����е�#
        text = text.replace('#', '')
        text=text.replace('>', '_M_')
        text=text.replace('<', '_L_')
        # ����ַ����Ƿ������ֿ�ͷ
        if text and text[0].isdigit():
            # ��ȡ��ͷ�����ֲ���
            number_part = ''
            while text and text[0].isdigit():
                number_part += text[0]
                text = text[1:]
            # ���ش������ַ���
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
    # print(output)  # ���: hello_world_123
    # name = "Alice"
    # age = 30

    # greeting = f"Hello, my name is {name}.\nI am {age} years old."
    # print(greeting)
    

    input_str = "abcdefgh_ijklmnop_qrstuvwx_yz0123_12"
    output_str = string_lengthLimit(input_str)
    print(output_str)

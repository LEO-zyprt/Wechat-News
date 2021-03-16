import json
import requests

# https://work.weixin.qq.com/api/doc/10013
# https://programmer.ink/think/using-python-to-send-enterprise-wechat-messages.html

class Wechat_Info():
    def __init__(self):
        self.partyID = ''
        self.corpID = 'wwb735785ea07b0f16'
        self.secret = 'FWr1feHfgW790h8BeeKsb3IddQOC6ZVQjBOupVtdgM8'
        self.agentID = '1000002'
        self.token = None
        self.pic = None
        self.Touser ='ZhangYu'   

    def __get_token(self, corpid, secret):
        Url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        Data = {
            "corpid": corpid,
            "corpsecret": secret
               }
        r = requests.get(url=Url, params=Data)
        token = r.json()['access_token']
        return token

    def send_message(self, message):
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(
            self.__get_token(self.corpID, self.secret))
        data = {
            "touser": self.Touser,
            "msgtype": "text",
            "agentid": self.agentID,
            "text": {
                "content": message
            },
            "safe": "0"
        }
        result = requests.post(url=url, data=json.dumps(data))
        return result.text

if __name__ == '__main__':
    wechat_info = Wechat_Info()
    result = wechat_info.send_message('python测试')
    print(result)


    

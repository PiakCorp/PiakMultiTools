import requests, json

keyCap = json.load(open('config.json', 'r'))['captcha_key']

def payload(service:str="capsolver.com", proxy:str=None, user_agent:str=None) -> None:
    p = {
        "clientKey":keyCap,
        "task": {
            "websiteURL":"https://discord.com/",
            "websiteKey":"4c672d35-0701-42b2-88c3-78380b0db560",
        }
    }
    if service == "capsolver.com": 
        p['appId']="E68E89B1-C5EB-49FE-A57B-FBE32E34A2B4"
        p['task']['type'] = "HCaptchaTurboTask"
        p['task']['proxy'] = proxy 
        p['task']['userAgent'] = user_agent
    if service == "capmonster.cloud": 
        p['task']['type'] = "HCaptchaTask"
        p['task']['proxyType'] = "http"
        p['task']['proxyAddress'] = proxy.split("@")[1].split(":")[0]
        p['task']['proxyPort'] = proxy.split("@")[1].split(":")[1]
        p['task']['proxyLogin'] = proxy.split("@")[0].split(":")[0]
        p['task']['proxyPassword'] = proxy.split("@")[0].split(":")[1]
    return p

def payload2(service:str="capsolver.com", proxy:str=None, user_agent:str=None) -> None:
    p = {
        "clientKey":keyCap,
        "task": {
            "websiteURL":"https://discord.com/",
            "websiteKey":"f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34",
        }
    }
    if service == "capsolver.com": 
        p['appId']="E68E89B1-C5EB-49FE-A57B-FBE32E34A2B4"
        p['task']['type'] = "HCaptchaTurboTask"
        p['task']['proxy'] = proxy 
        p['task']['userAgent'] = user_agent
    if service == "capmonster.cloud": 
        p['task']['type'] = "HCaptchaTask"
        p['task']['proxyType'] = "http"
        p['task']['proxyAddress'] = proxy.split("@")[1].split(":")[0]
        p['task']['proxyPort'] = proxy.split("@")[1].split(":")[1]
        p['task']['proxyLogin'] = proxy.split("@")[0].split(":")[0]
        p['task']['proxyPassword'] = proxy.split("@")[0].split(":")[1]
    return p

def payload3(service:str="capsolver.com", proxy:str=None, user_agent:str=None) -> None:
    p = {
        "clientKey":keyCap,
        "task": {
            "websiteURL":"https://discord.com/",
            "websiteKey":"76edd89a-a91d-4140-9591-ff311e104059",
        }
    }
    if service == "capsolver.com": 
        p['appId']="E68E89B1-C5EB-49FE-A57B-FBE32E34A2B4"
        p['task']['type'] = "HCaptchaTurboTask"
        p['task']['proxy'] = proxy 
        p['task']['userAgent'] = user_agent
    if service == "capmonster.cloud": 
        p['task']['type'] = "HCaptchaTask"
        p['task']['proxyType'] = "http"
        p['task']['proxyAddress'] = proxy.split("@")[1].split(":")[0]
        p['task']['proxyPort'] = proxy.split("@")[1].split(":")[1]
        p['task']['proxyLogin'] = proxy.split("@")[0].split(":")[0]
        p['task']['proxyPassword'] = proxy.split("@")[0].split(":")[1]
    return p

class Solver():
    def __init__(self, proxy:str, siteKey:str, siteUrl:str) -> None:
        self.debug = False

        self.proxy = proxy

        self.siteKey = siteKey
        self.siteUrl = siteUrl

        self.log(f'Solving Captcha, SiteKey: {self.siteKey} | SiteUrl: {self.siteUrl}')

    def log(self, txt:str) -> None:
        if self.debug: print(txt)

    def solveCaptcha(self) -> str:
        r = requests.post(f"https://api.capsolver.com/createTask",json=payload("capsolver.com",self.proxy,'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'))
        try:
            if r.json().get("taskId"):
                taskid = r.json()["taskId"]
            else:
                return None
        except:
            return None
        while True:
            try:
                r = requests.post(f"https://api.capsolver.com/getTaskResult",json={"clientKey":keyCap,"taskId":taskid})
                if r.json()["status"] == "ready":
                    key = r.json()["solution"]["gRecaptchaResponse"]
                    return key
                elif r.json()['status'] == "failed":
                    return None
            except:
                return None
    
    def solveCaptcha2(self) -> str:
        r = requests.post(f"https://api.capsolver.com/createTask",json=payload2("capsolver.com",self.proxy,'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'))
        try:
            if r.json().get("taskId"):
                taskid = r.json()["taskId"]
            else:
                return None
        except:
            return None
        while True:
            try:
                r = requests.post(f"https://api.capsolver.com/getTaskResult",json={"clientKey":keyCap,"taskId":taskid})
                if r.json()["status"] == "ready":
                    key = r.json()["solution"]["gRecaptchaResponse"]
                    return key
                elif r.json()['status'] == "failed":
                    return None
            except:
                return None
    
    def solveCaptcha3(self) -> str:
        r = requests.post(f"https://api.capsolver.com/createTask",json=payload3("capsolver.com",self.proxy,'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'))
        try:
            if r.json().get("taskId"):
                taskid = r.json()["taskId"]
            else:
                return None
        except:
            return None
        while True:
            try:
                r = requests.post(f"https://api.capsolver.com/getTaskResult",json={"clientKey":keyCap,"taskId":taskid})
                if r.json()["status"] == "ready":
                    key = r.json()["solution"]["gRecaptchaResponse"]
                    return key
                elif r.json()['status'] == "failed":
                    return None
            except:
                return None

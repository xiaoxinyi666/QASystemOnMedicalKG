import werobot
import os
from tuling import visit_tuling
from baidu import visit_baidu
from chatbot_graph import ChatBotGraph
token = os.getenv("token", "XTiw5QAnhO3NOPiYS5AUyQvxOdKI")
robot = werobot.WeRoBot(token=token)
handler = ChatBotGraph()

# @robot.text
# def home(message,session):
#     if "百度百科" in message.content:
#         session['百度百科']=True
#         return "欢迎使用百度百科,例如；长沙学院的地址是什么？ 输入“退出” 退出词条"
#     if session['百度百科']:
#         if "退出" not in message.content:
#             return visit_baidu(message.content)
#         else:
#             session['百度百科'] = False
#             return "退出百度百科"
#     return visit_tuling(message.content)

@robot.text
def home(message,session):
    if "健康助手" in message.content:
        session['健康助手']=True
        return "欢迎使用健康助手,例如；感冒了不应该吃什么？ 输入“退出” 退出健康助手"
    if session['健康助手']:
        if "退出" not in message.content:
            return handler.chat_main(message.content)
        else:
            session['健康助手'] = False
            return "退出健康助手"
    return visit_tuling(message.content)

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()

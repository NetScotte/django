from datetime import datetime
import logging
import json

logging.basicConfig(level=logging.INFO)
MESSAGEFILE = 'liuyan.json'


# 产生一条信息，返回信息的字典形式
def produce_message(user, title, content):
    logging.info("produce message")
    message = {}
    message['time'] = str(datetime.today())
    message['user'] = user
    message['title'] = title
    message['content'] = content
    return message


# 获取所有信息，列表形式
def get_message():
    m = json.load(open(MESSAGEFILE,'r'))
    return m


# 保存信息，将列表类的content覆写到文件
def save_message(content):
    if not isinstance(content,list):
        print("wrong type contenct in save_message")
        return None
    json.dump(content, open(MESSAGEFILE, 'w'))


# 添加一条信息
def add_file(message):
    logging.info("add message to file")
    if not isinstance(message, dict):
        print("wrong parameters: {0} type {1}".format(message, type(message)))
        return None
    content=get_message()
    content.append(message)
    json.dump(content, open(MESSAGEFILE, 'w'))
    logging.info("success add message to file")

def del_resource(id):
    if not isinstance(id,int):
        print("wrong type id in del_resource")
        return None
    m = get_message()
    m.pop(id)
    save_message(m)

if __name__ == "__main__":
    # m = produce_message("hym", 'haolei', '说好累是我的习惯')
    # add_file(m)
    # for i in get_message():
    #     print(i)
    del_resource(3)

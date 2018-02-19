from datetime import datetime
import logging
import json

logging.basicConfig(level=logging.INFO)
USERFILE = 'user.json'
# 产生一条信息，返回信息的字典形式
def create_user(user, passwd, label):
    logging.info("create user recorde")
    message = {}
    message['time'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    message['user'] = user
    message['passwd'] = passwd
    message['label'] = label
    return message


# 获取所有信息，列表形式
def get_user():
    m = json.load(open(USERFILE, 'r'))
    return m

# 获取字典的序列
def get_dictTarget(name):
    m=get_user()
    for i in m:
        if i['user'] == name:
            return i
            break
    logging.info("no such id in get_dictTarget")
    return None

# 保存信息，将列表类的content覆写到文件
def save_user(content):
    if not isinstance(content,list):
        logging.info("wrong type contenct in save_message")
        return None
    json.dump(content, open(USERFILE, 'w'))


# 添加一条信息
def add_file(user):
    logging.info("add user to file")
    if not isinstance(user, dict):
        logging.info("wrong parameters: {0} type {1}".format(user, type(user)))
        return None
    content=get_user()
    content.append(user)
    json.dump(content, open(USERFILE, 'w'))
    logging.info("success add message to file")

# 删除用户,此ID为用户在列表中的位置
def del_user(target):
    m = get_user()
    m.remove(target)
    save_user(m)

if __name__ == "__main__":
    # user1=create_user('lfy','123456','积极')
    # user2=create_user('hym','123123','懒散')
    # add_file(user1)
    # add_file(user2)
    # print(get_user())
    print(get_user())
    get_dictTarget('lfy')
import os
import configparser
from Config import get_path_info

path = get_path_info.get_path()
config_path = os.path.join(path, 'server.ini')
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')

#读取配置文件，获取配置文件的数据
class ReadCconfig():

    def get_http(self, name):

        value = config.get('HTTP', name)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    def get_mysql(self, name):
        value = config.get('DATABASE', name)
        return value

read_config = ReadCconfig()

if __name__ == "__main__":
    print("http中baseurl的值为：", ReadCconfig().get_http('baseurl'))
    print("email中off_on的开关为：", ReadCconfig().get_email('on_off'))
import os

def get_path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path

if __name__ == "__main__":
    print("测试路径是OK的", '\n', get_path())
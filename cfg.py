import os
import re
import time
import json

config_path = "./config"
if not os.path.exists(config_path):
    os.mkdir(config_path)


def check_windows_path(path):
    paths = path.split("\\")  # ['C:', 'Users', 'Administrator', 'Downloads']
    print(path)
    if len(paths) < 2:  # path: 'C:'
        return False
    for i in range(len(paths)):
        if paths[i] == "":  # 文件夹名不能为空
            return False
        if len(paths[i]) > 224:  # 文件夹名长度不能超过 224，具体和系统有关
            return False
        if i > 0:  # 盘符之后开始
            if ":" in paths[i]:  # 文件夹名不能有冒号（:）
                return False
            else:
                s = paths[i].strip()
                if s != paths[i]:  # 文件夹名前后不会有空格
                    return False
                dirs1 = paths[i].split("/")  # 文件夹名不会有 /
                if len(dirs1) > 1:
                    return False
        else:
            if ":" not in paths[i]:  # 盘符后应该跟着冒号（:）
                return False
            elif " " in paths[i]:  # 盘符名中不能有空格
                return False
            else:
                dirs2 = paths[i].split(":")  # i = 'C:'
                if len(dirs2) != 2:  # 长度应该为 2
                    return False
                if not re.search(
                    "[a-zA-Z]", dirs2[0]
                ):  # 盘符应为英文字母，不区分大小写
                    return False
    valid_strs = ["?", "/", "|", "<", ">", "*", '"']
    for valid_str in valid_strs:
        if valid_str in paths:  # 绝对路径中不能有以上列表中的字符
            return False
    return True


# 获取全部配置
def get_cfg_list():
    cfg_name_list: list[str] = []
    for name in os.listdir(config_path):
        name = name.strip()
        path = os.path.join(config_path, name)
        if os.path.isfile(path) and name.endswith(".json"):
            cfg_name_list.append(name.removesuffix(".json"))
    return cfg_name_list


def save_cfg(name: str = "", src_path: str = "", out_list: list[dict] = []):
    name = name.strip()
    if name == "":
        name = str(int(time.time()))
    src_path = src_path.strip()
    if not os.path.exists(src_path):  # or
        return "原路径不存在"
    if not os.path.isdir(src_path):
        return "非目录路径"

    path = os.path.join(config_path, name + ".json")
    repteat_index = 1
    while os.path.exists(path):
        path = os.path.join(config_path, name + "(%d).json" % repteat_index)
        repteat_index += 1
    for out in out_list:
        out_path = out.get("out_path", "")
        if not check_windows_path(out_path):
            return "输出路径非法"
        code_type = out.get("code_type", "json")
        if code_type not in ["json"]:
            return "不支持该类型"
    cfg_data = {
        "src_path": src_path,
        "out_list": out_list,
    }

    file = open(path, "w")
    file.write(json.dumps(cfg_data, indent=4))
    file.close()


def del_cfg(name: str):
    path = os.path.join(config_path, name + ".json")
    if os.path.exists(path):
        os.remove(path)


def load_cfg(name: str) -> dict:
    name = name.strip()
    path = os.path.join(config_path, name + ".json")
    if not os.path.exists(path):
        return
    with open(path, "r") as f:
        return json.load(f)


def get_code_type_list() -> list[str]:
    return ["json"]

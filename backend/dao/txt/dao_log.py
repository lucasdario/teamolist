from backend.dao.txt.txt_utils import read_logs_from_txt_file, write_log_to_txt_file


def write_log(content: str):
    write_log_to_txt_file(content)
    

def read_logs() -> list:
    log_list = read_logs_from_txt_file()
    return log_list

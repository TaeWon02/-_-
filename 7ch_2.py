import os
def read_folder(path):
    output=os.listdir(path)
    for item in output:
        if os.path.isdir(item):
            read_folder(path+"/"+item)
            #무슨 뜻인지 모르겠다. 경로를 path폴더 안의 item항목으로 한 듯
        else:
            print("파일: ", item)
read_folder(".")
#.을 왜 매개변수로 주는 것일까
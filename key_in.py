dictionary={
    "name": "7D건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}
key=input(">접근하고자 하는 키 입력: ")
if key in dictionary:
    print(dictionary[key])
else:
    print("없는 키")
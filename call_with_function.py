def power(item):
    return item**2
def under_3(item):
    return item<3
list_input_a=[1, 2, 3, 4, 5]
#map은 리스트의 요소를 함수에 대입하고 결과들을 리스트로 만들어 출력해준다
output_a=map(power, list_input_a)
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()
#filter는 리스트의 요소를 함수에 대입하고 결과인 불값이 참인 요소들로만
#리스트롤 만들어 출력해준다
output_b=filter(under_3, list_input_a)
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))

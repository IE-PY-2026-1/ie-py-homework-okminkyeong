# 파일이름 : 60251781 옥민경 파이썬 3차과제
# 작 성 자 : 옥민경

#[3차 과제] 갓생 살기: 투두 메이트 시스템
#전역 변수 선언(프로그램 전체에서 관리할 투두리스트 데이터)
todo_list = []
completed_count = 0  #완료된 할 일 개수를 추적하는 전역 변수

def input_todo():
    """1. 할 일을 입력받아 전역 리스트 추가하는 함수"""
    print("\n--- [새로운 할 일 추가] ---")
    task = input('추가할 할 일을 입력하세요: ')

    if task == "":
        print("경고: 내용을 입력해야 합니다.")
    else:
        todo_list.append({"task": task, "done": False})
        print(f"성공: '{task}' 항목이 추가되었습니다.")

def show_todos(todos):
    """2. 현재 투두 리스트를 출력하는 함수(매개변수 전달 조건 충족)"""
    print("\n--- [현재 투두 리스트 보기] ---")
    if not todos:
        print("아직 등롣된 할 일이 없습니다.")
        return
    
    for i in range(len(todos)):
        item = todos[i]

        if item["done"] == True:
            status = "[완료]"
        else:
            status = "[미완료]"

        print(f"{i + 1}. {status} {item['task']}") 

def complete_todo():
    """3. 할 일을 완료 처리하고 완료 카운트를 올리는 함수"""
    global completed_count

    print("\n--- [할 일 완료하기] ---")
    if not todo_list:
        print("완료 처리할 항목이 없습니다.")
        return 0

    for i in range(len(todo_list)):
        item = todo_list[i]
        if item["done"] == True:
            status = "[완료]"
        else:
            status = "[미완료]"
        print(f"{i + 1}. {status} {item['task']}")

    choice_input = input("완료할 항목의 번호를 선택하세요: ")

    target_index = -1
    for i in range(len(todo_list)):
        if choice_input == str(i + 1):
            target_index = i

    if target_index != -1:
        selected_item = todo_list[target_index]
        if selected_item["done"] == False:
            selected_item["done"] = True
            completed_count += 1
            print(f"성공: '{selected_item['task']}' 항목을 완료했습니다.")
            return 1
        else:
            print("경고: 이미 완료된 항목입니다.")
            return 0
    else:
        print("경고: 올바른 변호를 선택해주세요.")
        return 0
    

while True:
    print("\n===============================")
    print(f" Todo Mate (오늘 완료: {completed_count}개) ")
    print("===============================")
    print("1. 할 일 입력")
    print("2. 투두 조회")
    print("3. 할 일 완료")
    print("4. 프로그램 종료")
    print("===============================")

    menu = input("원하는 메뉴 번호를 입력하세요: ")

    if menu == "1":
        input_todo()

    elif menu == "2":
        show_todos(todo_list)

    elif menu == "3":
        result= complete_todo()

    elif menu == "4":
        print("\n프로그램을 종료합니다.")
        break
    
    else:
        print("경고: 잘못된 입력입니다. 1번부터 4번 사이의 숫자를 입력해주세요.")
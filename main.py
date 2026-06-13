#파일 이름 : 60251781 옥민경 파이썬 4차 과제
#작성자 : 옥민경

#[4차 과제] 갓생 살기: 투두 메이트 시스템

todo_list = [
    [1, "파이썬 4차 과제 제출하기", "미완료", 5],
    [2, "깃허브 리포지토리 커밋 확인", "미완료", 4]
]
current_id = 3

def input_todo():
    """1. 할 일을 입력받아 이중 리스트에 append로 누적하는 함수"""
    global current_id
    print("\n---[새로운 할 일 추가]---")
    task = input("추가할 할 일을 입력하세요: ").strip()

    if task == "":
        print("경고: 내용을 입력해야 합니다.")
        returb
    
    try:
        priority = int(input("우선순위를 입려하세요 (1~5 숫자): "))
        if priority < 1 or priority > 5:
            print("범위를 벗어나 기본값 3으로 설정합니다.")
            priority = 3
    except ValueError:
        print("오류: 숫자가 입력되지 않아 우선순위가 기본값 3으로 자동 지정됩니다. (예외처리 1)")
        priority = 3

    todo_list.append([current_id, task, "미완료", priority])
    print(f"성공: '{task}' 항목이 추가되었습니다.")
    current_id += 1

def show_todos(todos):
    """2. 이중 리스트에 담긴 데이터를 이중 순회하여 표 형태로 깔끔하게 출력하는 함수"""
    print("\n---[현재 투두 리스트 보기]---")
    if not todos:
        print("아직 등록된 할 일이 없습니다.")
        return
    print("_"*65)
    print(f"{'ID':<5}, {'할 일 내용':<30}, {'상태':<10}, {'우선순위':<8}")
    print("_"*65)

    for item in todos:
        row_str = ""
        for idx, val in enumerate(item):
            if idx == 0:
                row_str += f"{val:<5}"
            elif idx == 1:
                row_str += f"{val:<30}"
            elif idx == 2:
                row_str += f"{val:<10}"
            elif idx == 3:
                row_str += f"{'★' * val:<8}"
        print(row_str)
print("_" * 65)

def save_to_file():
    """3. open() / with open()을 사용하여 데이터를 파일에 저장(Write)하는 함수"""
    filename = 'todo_storage.txt'
    print("\n--- [데이터 파일 저장] ---")

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("ID,할일내용,완료여부,우선순위\n")
            for row in todo_list:
                line = f"{row[0]}, {row[1]}, {row[2]}, {row[3]}\n"
                f.write(line)
        print(f"성공: '{filename}' 파일에 안전하게 저장되었습니다!")
    except Exception:
        print("오류: 파일에 데이터를 쓰는 도중 입출력 에러가 발생했습니다.")

def main():
    while True:
        print("\n========================================")
        print("투두리스트(To-Do List) 관리 시스템 V4.0")
        print("========================================")
        print(" 1. 할 일 입력")
        print(" 2. 투두 조회 (이중 순회)")
        print(" 3. 파일 저장 (텍스트 저장)")
        print(" 4. 프로그램 종료")
        print("========================================")

        try:
            menu = int(input("원하는 메뉴 번호를 입력하세요: "))
        except ValueError:
            print("오류: 메뉴 번호는 숫자로만 입력하셔야 합니다! (예외처리2)")
            continue

        if menu == 1:
            input_todo()
        elif menu == 2:
            show_todos(todo_list)
        elif menu == 3:
            save_to_file()
        elif menu == 4:
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 1~4 사이의 번호를 입력해주세요.")

if __name__ == '__main__':
    main()        
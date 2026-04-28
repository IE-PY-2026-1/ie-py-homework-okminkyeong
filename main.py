# 파일이름 : 60251781 옥민경 파이썬 2차과제
# 작 성 자 : 옥민경

#[2차 과제] 갓생 살기: 투두 메이트 시스템
#1. 변수 및 리스트 초기화
user_name = input("사용자 이름을 입력하세요: ")
total_goal_count = 0
done_count = 0
focus_time = 0.0
todo_data = []

#2. 반복문(for)을 이용한 데이터 입력
print(f'{user name}님의 오늘의 기록을 시작합니다')
categories = ['학업', '운동','취미']

for category in  categories:
  val = int(input(f'[{category]] 완료한 할 일 개수를 입력하세요:'))
  todo_data.append(val)

# 데이터 조작 
total_count = sum(todo_data)
task_count = len(todo_data)
best_recored = max(todo_data)
todo_data.sort(reverse=True)

#연산자 활용 및 성취도 계산
#가중치 예시: (완료 개수 * 10) + (집중 시간 * 2)
focus_time = float(input('오늘의 총 집중 시가(시간 단위)을 입력하세요: '))
achievement_score = (total_done * 15.5) + (focus_time * 5.0)

#복합 대입 연산자 활용
bonus_score = 0
bonus_score += 5

final_score = achievement_score + bonus_score

5. 제어구조
print(f'{useer_name}님의 최종 분석 결과)

if final_score >= 90:
    grade = 'S (갓생 마스터)'
    if total_done >= 5 and focus time >= 3.0:
      print('[특별칭호: 전설의 몰입러] 부여')
elif final_score >= 70:
      grade = 'A(성실한 노력파)'
elif final_score >= 50:
      grade = 'B(평범한 하루)'
else:
    grade = 'F (재충전 필요)'

#6
print(f'최종 성취 점수: {final_score:.2f}점')
print(f'당신의 오늘 등급은 [{grade}] 입니다.')
      


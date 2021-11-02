#import first  # first 모듈을 가져옴

print('second.py __name__:', __name__)  # __name__ 변수 출력



#자기 파일 내에서 실행하면 __name__ == "__main__"
#import 시키면 파일명 출력
from pathlib import Path

# ------------------------------------------------
# 1. 경로의 상태보기
print(Path.cwd())           #현재 디텍토리
print(Path.home())


# ----------------------------------------------------
# 2. 경로(파일) 생성시간 알아보기
p1 = Path('Ex03_createPath.py')
tm = p1.stat().st_ctime
print(tm)

from datetime import datetime               #datetime이라는 모듈 뽑아내기
print(datetime.fromtimestamp(tm))


# ------------------------------------------------
# 3. 디렉토리 생성
# p1 = Path('imsi')       #imsi 폴더 생성
# p1.mkdir(exist_ok=True)                 #없으면 만들고 있으면 통과(에러 발생X)


# p2 = Path('temp2/test2/abc')
# p2.mkdir(parents=True)                  #부모 자식간의 경로로 만들어주세요

# ------------------------------------------------
# 4. 파일 생성



# ------------------------------------------------
#  5. 경로 제거
p3 = Path('temp2')
p3.rmdir()



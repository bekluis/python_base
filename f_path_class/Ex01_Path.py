"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path


# (1) 해당 경로와 하위 목록들 확인
p = Path('c:\Windows9')
# p = Path('..')


print(p)
print(p.resolve())
print('-'*50)

child = []
# for x in p.iterdir():
#     if x.is_dir():
#         child.append(x)

child = [ x for x in p.iterdir() if x.is_dir() ]        # 컴프리핸션
print(child)
# print('-'*50)



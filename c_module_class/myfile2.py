
# 1. 전체 임포트
import mypackage.mymodule

print('날씨는 ', mypackage.mymodule.get_weather())


# 2. 필요한 것만 임포트
from mypackage import mymodule
print('날씨는',mymodule.get_weather())
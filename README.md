# DBteamproject
DB팀 프로젝트 입니다.  
commit massage 는 "(add/remove) + 기능이름"으로 부탁드립니다.  

# 서지원 - 21.11.12 22:14 - 커밋사항입니다. 
- main.py 및 ui와 기능 디렉토리를 추가하였습니다.  
- 디렉토리별 설명은 아래와 같습니다.  
./main.py 
  - 실행용 파일입니다.
  - app = QApplication(sys.argv) 으로 pyqt앱을 생성합니다.
  - myWindow는 ui전환을 위한 global변수 입니다. 이후 기능에서 이 변수를 참조 및 변경하여 ui를 변경합니다.
  - sys.exit(app.exec_())로 app의 실행 및 프로그램 종료를 동시에 실행합니다.

./ui/
  - ui저장용 디렉토리입니다.
  - 모든 기능들의 ui는 이 디렉토리에 저장후 import하여 사용합니다.

./(기능이름)/(기능이름).py
  - 기능구현용 디렉토리
  - 각 기능은 main디렉토리의 하위에 디렉토리의 형태로 저장합니다.
  - 이후 form_class = uic.loadUiType("./ui/(기능이름).ui")[0] 의 형태로 ui를 불러옵니다.
  - class WindowClass(QMainWindow, form_class) 으로 각 기능별 ui에 대한 기능을 정의합니다.
  - 자세한 구현은 소스파일의 login 과 register 기능 구현 소스 코드를 참조하시면 됩니다.  

위키독스 Pyqt 관련도서 입니다. 참고바랍니다.
https://wikidocs.net/21849
https://wikidocs.net/21950

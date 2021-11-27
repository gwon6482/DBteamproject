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

./ui/(기능이름).ui
  - ui저장용 디렉토리입니다.
  - 모든 기능들의 ui는 이 디렉토리에 저장후 import하여 사용합니다.

./(기능이름)/(기능이름).py
  - 기능구현용 디렉토리
  - 각 기능은 main디렉토리의 하위에 디렉토리의 형태로 저장합니다.
  - 이후 form_class = uic.loadUiType("./ui/(기능이름).ui")[0] 의 형태로 ui를 불러옵니다.
  - class WindowClass(QMainWindow) 으로 각 기능별 ui에 대한 기능을 정의합니다.
  - 자세한 구현은 소스파일의 login 기능 구현 소스 코드를 참조하시면 됩니다.  

위키독스 Pyqt 관련도서 입니다. 참고바랍니다.  
https://wikidocs.net/21849  
https://wikidocs.net/21950  

youTube 관련자료 입니다.  
https://www.youtube.com/watch?v=yPgQ0N6gdhI  

개발 순서는
1. QtDesigner 로 ui개발 -> pyuic5를 이용해 .py파일로 변환  
2. .py파일을 생성하여 ui와 연결 및 필요 메소드 구현
3. start(기능이름)() 함수를 통하여 이전 ui와 연결  
순서로 하시면 편하실거라 생각합니다.  


# 서지원 - 21.11.15 16:25 - 커밋사항입니다.
ui를 py로 변경하여 기능에 직접 import하는 방식으로 변경하였습니다.
코드 참고 바랍니다.

DBconnect.py를 추가하였습니다. 
모든 sql사용 함수는 이 파일에 정의하고 다른 기능에서 import하여 사용하느걸로 하겠습니다.  

ui디렉토리는 실제 컴파일시 사용하지는 않지만 추후 ui수정을 위한 저장소로 활용합니다.  
  
# 서지원 - 21.11.18 00:11 - 커밋사항입니다.  
Register 기능을 추가하였습니다.  
Login 기능과 DB기능을 연결하여 로그인 확인이 가능합니다. - 추후 프로필 페이지와 연결합니다.  
DBconnect에 로그인 확인 및 회원가입과 관련된 함수를 추가하였습니다.  
DBconnect에 팝업 메세지 출력 함수를 추가하였습니다.

# 정진우 - 21.11.21 18:03 - 커밋사항입니다.
브랜치 inventory생성 (재고사항 확인 및 수정용)
1. DBconnect.py - result변수 통해 쿼리성공시 결과값 반환하도록 수정
2. InventoryPage.py 생성 - 쿼리 통해 재고볼수 있음, 재고 추가 버튼통해 추가가능

추후 구현할 것
1. 재고값 수정기능 추가
2. 중복검색기능추가
3. 쿼리결과에 따른 결과(팝업메시지)구현

# 정진우 - 21.11.27 11:16 - 커밋사항입니다.
1. Inventory.py - 삭제,추가기능 구현
2. PurchaseList.py 생성 - 판매목록 볼수 있음.

"""
Google Colaboaratory (for LightCBM and big data handling)
- 구글 클라우드에서 구동되는 가상컨테이너
- 주피터 노트북과 매우 유사한 환경 제공, 다만 직접적으로 OS를 붙일 수 없으니 개인 계정의 구글 드라이브를 통해 (Colab Notebook VM에서) 데이터 파일 접근 가능하게 함
- Colab과 Google Drive 모두 클라우드 환경이므로 연동을 위한 인증 및 Network directory 마운트가 필요하다

1. 구글 드라이브 선택 
    - data 디렉토리  : 소스파일 업로드 장소
    - Colab Notebooks 디렉토리 : 콜랩에 올린/작성한 노트북이 저장되는 곳
2. 구글 코랩 접속
    - 파이썬 새 노트북 작성
    - 기존 로컬의 (주피터)노트북 업로드 → Colab Notebooks 에 저장된다.
3. 구글 콜랩과 구글 드라이브 연동을 위한 인증 및 네트워크 마운트 

    ```python
    # 유저 인증, 네트워크 마운트
    from google.colab import auth
    auth.authenticate_user()

    from google.colab import drive
    drive.mount('/content/drive')
    ```

    ```python
    # 연동 후 자신의 google drive에 있는 data directory 확인
    !cd "/content/drive/My Drive/data";
    ```

    ```python
    # 기타 환경 정보 확인
    # cat : concatenate 파일이름을 인자로 받아서 그 내용을 쭉 이어주는 역할 
    # cat [옵션] [파일명]
    !cat /proc/meminfo;cat / proc/cpuinfo
    ```

"""
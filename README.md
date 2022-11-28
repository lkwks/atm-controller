### 1. The instruction to run this app

You can run this app with **Python**. Just enter the command below into your computer's terminal window.

```
% python main.py
```



### 2. 코드에 관한 설명

1\) 전체적인 프로그램의 flow는 `main.py` 파일에 다음과 같이 구현했다.

    (1) 프로그램 실행 시 가장 먼저 카드에 관한 정보를 입력 받는다.

    (2) PIN 번호를 입력 받는다. 

    (3) 그 PIN 번호가 유효할 때, 그 카드 정보에 해당하는 계좌 목록을 보여주고 그 중 기능을 수행할 계좌를 입력 받는다.

    (4) 수행할 세 기능(잔고확인, 입금, 출금) 중 하나를 입력 받는다.

    (5) 입력한 기능에 해당하는 동작을 수행한다. 

2\) 각 기능에 해당하는 세부 코드 구현은 `atm_control.py` 파일 안에 구현된 `atmObj` 클래스의 메서드로서 구현했다. `atmObj` 클래스의 메서드가 대부분의 작업을 수행하도록 구현했으며, 이외에도 다음 작업의 경우 다른 파일의 다른 클래스를 이용해 구현했다.

- 화면에 출력할 내용이 있다면 `atm_view.py` 파일에 구현된 `atmViewObj` 클래스의 메서드로 관련 내용을 전달하여 출력하도록 구현했다.

- DB에 관한 처리는 `db_connection.py` 파일의 `dbObj` 클래스의 메서드에 관련 내용을 전달하여 처리하도록 구현했다.

- PIN의 유효성은 `bankAPI.py` 파일의 `checkPIN()` 함수를 호출하여 확인하도록 했는데, 일단은 항상 `True` 값을 리턴하도록 임시로 구현했다.



### 3. 구현 과정에서 느낀 점


- JS로는 이 정도 사이즈의 프로그램을 많이 개발해봐 전체적인 개발 과정이 크게 낯설거나 어려운 점은 없었지만, 그래도 파이썬으로는 처음 해보는 것이라 낯설게 느낀 점이 있었다.

- 실제 업무 환경에서 만약 이와 같은 문제를 풀어야 하는 상황이 있고 이 코드보다 더 나은 정답 코드가 있다 할 때, 그 정답은 어떤 점에서 이것보다 더 '낫다'라고 할 수 있는지 그 기준이 궁금하다는 생각이 들었다.

- 처음으로 파이썬 프로그램을 만들면서 타입 힌트를 사용해봤는데, VS Code에서 굉장히 사용하기 편했고 덕분에 개발 시간이 크게 단축될 수 있었다. 굉장히 유용하다고 느꼈고 앞으로 자주 사용하게 될 것 같다.

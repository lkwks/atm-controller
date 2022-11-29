import sqlite3
from typing import List, Any

# 사용돼야 할 테이블
# 사용자별 카드정보, 계좌 정보, 계좌 잔고
# 카드 정보를 기본키로 하는 테이블 하나, 계좌를 기본키로 하는 테이블 하나. 총 두 개 사용. 카드 정보 - 계좌 번호라는 엔티티, 계좌 번호 - 잔고라는 엔티티.


class dbObj:
    

    def __init__(self) -> None:
        pass

    def open(self) -> None:
        self.__conn__: sqlite3.Connection = sqlite3.connect('./atm.db')
        self.__cursor__: sqlite3.Cursor = self.__conn__.cursor()
        self.__checkIfNoTable__()

    def __checkIfNoTable__(self) -> None:
        self.__cursor__.execute('SELECT COUNT(*) FROM sqlite_master Where name = "CustomerInfo"')
        result: Any = self.__cursor__.fetchone()
        if result[0] != 1:
            self.__cursor__.execute('CREATE TABLE CustomerInfo(CardInfo INTEGER, Account INTEGER, FOREIGN KEY(Account) REFERENCES AccountInfo(Account))')

        self.__cursor__.execute('SELECT COUNT(*) FROM sqlite_master Where name = "AccountInfo"')
        result = self.__cursor__.fetchone()
        if result[0] != 1:
            self.__cursor__.execute('CREATE TABLE AccountInfo(Account INTEGER PRIMARY KEY, Balance INTEGER)')
        
        
    def getAccounts(self, cardInfo: int) -> List[int]:
        self.__cursor__.execute('SELECT Account FROM CustomerInfo WHERE CardInfo = ?', (cardInfo,))
        result: List[int] = [item[0] for item in self.__cursor__.fetchall()]
        return result

    def close(self) -> None:
        self.__conn__.close()

    def getBalance(self, account: int) -> int:
        self.__cursor__.execute('SELECT Balance FROM AccountInfo WHERE Account = ?', (account,))
        result: Any = self.__cursor__.fetchone()
        return result[0]

    def deposit(self, **kwargs: int) -> None:
        self.__cursor__.execute('BEGIN')

        try:
            self.__cursor__.execute('SELECT Balance FROM AccountInfo WHERE Account = ?', (kwargs["account"],))
            result: int = self.__cursor__.fetchone()[0] + kwargs["deposit"]
            self.__cursor__.execute('UPDATE AccountInfo SET Balance = ? WHERE Account = ?', (result, kwargs["account"],))
            self.__cursor__.execute('COMMIT')
        except Exception as e:
            print("error during deposit", kwargs)
            self.__cursor__.execute('ROLLBACK')
            raise Exception(e)
        
    def withdraw(self, **kwargs: int) -> None:
        self.__cursor__.execute('BEGIN')

        try:
            self.__cursor__.execute('SELECT Balance FROM AccountInfo WHERE Account = ?', (kwargs["account"],))
            result: int = self.__cursor__.fetchone()[0] - kwargs["withdraw"]
            if result < 0: 
                raise Exception("insufficient balance")
            self.__cursor__.execute('UPDATE AccountInfo SET Balance = ? WHERE Account = ?', (result, kwargs["account"],))
            self.__cursor__.execute('COMMIT')
        except Exception as e:
            print("error during withdraw", kwargs)
            self.__cursor__.execute('ROLLBACK')
            raise Exception(e)
        

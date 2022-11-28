from db_connection import dbObj
from atm_view import atmViewObj
from typing import List

class atmObj:
    __cardInfo__: int
    __dbObj__: dbObj
    __viewObj__: atmViewObj

    def __init__(self) -> None:
        self.__dbObj__ = dbObj()
        self.__viewObj__ = atmViewObj()
    
    def dbOpen(self) -> None:
        self.__dbObj__.open()

    def dbClose(self) -> None:
        self.__dbObj__.close()

    def getCardInfo(self) -> int:
        self.__cardInfo__ = self.__viewObj__.renderGetCardInfo()
        return self.__cardInfo__
    
    def getPIN(self) -> int:
        return self.__viewObj__.renderGetPIN()

    def getAccountSelection(self) -> None:
        accounts: List[int] = self.__dbObj__.getAccounts(self.__cardInfo__)
        while True:
            chosenAcc: int = self.__viewObj__.renderAccounts(accounts)
            if chosenAcc in accounts:
                self.__chosenAccount__ = chosenAcc
                break

    def getPageSelection(self) -> str:
        while True:
            chosenPage: str = self.__viewObj__.renderPageSelection()
            if chosenPage in ("balance", "deposit", "withdraw"):
                break
        return chosenPage

    def showBalance(self) -> None:
        balance: int = self.__dbObj__.getBalance(self.__chosenAccount__)
        self.__viewObj__.renderBalance(balance)

    def showDeposit(self) -> None:
        deposit: int = self.__viewObj__.renderDeposit()

        try:
            self.__dbObj__.deposit(account = self.__chosenAccount__, deposit = deposit)
            self.__viewObj__.showMessage("deposit succeed")
        except Exception as e:
            self.__viewObj__.showMessage("deposit failed; "+ str(e))


    def showWithdraw(self) -> None:
        withdraw: int = self.__viewObj__.renderWithdraw()

        try: 
            self.__dbObj__.withdraw(account = self.__chosenAccount__, withdraw = withdraw)
            self.__viewObj__.showMessage("withdraw succeed")
        except Exception as e:
            self.__viewObj__.showMessage("withdraw failed; "+ str(e))
        


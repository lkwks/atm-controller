from typing import List

class atmViewObj:
    def __init__(self) -> None:
        pass

    def __inputBox__(self, boxText: str) -> int:
        while True:
            box: str = input(boxText)
            if box.isdigit(): return int(box)

    def renderGetCardInfo(self) -> int:
        return self.__inputBox__("Type your card info as integer. card info for test is 4612378: ")

    def renderGetPIN(self) -> int:
        return self.__inputBox__("Type your PIN: ")

    def renderAccounts(self, accounts: List[int]) -> int:
        print("\nYour accounts are:")
        for account in accounts:
            print(account)
        return self.__inputBox__("Type one of your accounts: ")

    def renderPageSelection(self) -> str:
        print("\nMenu: ")
        for detail in ("balance", "deposit", "withdraw"):
            print(detail)
        return input("Type what to do: ")

    def renderBalance(self, balance: int) -> None:
        print("\nThe balance of your account is: " + str(balance))

    def renderDeposit(self) -> int:
        return self.__inputBox__("Type the amount to deposit: ")

    def renderWithdraw(self) -> int:
        return self.__inputBox__("Type the amount to withdraw: ")

    def showMessage(self, msg: str) -> None:
        print(msg)


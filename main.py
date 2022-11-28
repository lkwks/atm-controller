
'''
 사용자가 (1)카드를 넣고 (2)PIN 번호를 넣고 (3)계좌를 선택하면 (4)잔고 확인/입급/출금을 선택할 수 있는 ATM을 구현하라.
- 함수, 메서드, 클래스만으로 구현해라. 제3자가 UI단을 구현할 수 있는 코드를 남겨놔라.
'''

from atm_control import atmObj
from bankAPI import checkPIN

if __name__ == "__main__":

    atmController = atmObj()
    atmController.dbOpen()

    while True:
        card_info: int = atmController.getCardInfo()
        pin: int = atmController.getPIN()
        if checkPIN(card_info, pin) == False: break
        atmController.getAccountSelection()
        page_selection: str = atmController.getPageSelection()

        if page_selection == "balance":
            atmController.showBalance()
        elif page_selection == "deposit":
            atmController.showDeposit()
        elif page_selection == "withdraw":
            atmController.showWithdraw()


    atmController.dbClose()
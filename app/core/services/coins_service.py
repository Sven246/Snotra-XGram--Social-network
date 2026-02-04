from app.extensions import db
from app.core.models.coin_transaction import CoinTransaction
from app.core.models.user import User
from datetime import datetime

class CoinsService:

    @staticmethod
    def add_coins(user: User, amount: int, description: str):
        user.coins_balance += amount

        tx = CoinTransaction(
            user_id=user.id,
            amount=amount,
            type="income",
            description=description
        )

        db.session.add(tx)
        db.session.commit()

    @staticmethod
    def remove_coins(user: User, amount: int, description: str):
        if user.coins_balance < amount:
            return False

        user.coins_balance -= amount

        tx = CoinTransaction(
            user_id=user.id,
            amount=-amount,
            type="expense",
            description=description
        )

        db.session.add(tx)
        db.session.commit()
        return True

from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import Enum
from uuid import UUID, uuid4


class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


@dataclass
class Transaction:
    amount: Decimal
    description: str
    category: str
    transaction_type: TransactionType
    user_id: UUID
    date: datetime = field(default_factory=datetime.now)
    id: UUID = field(default_factory=uuid4)

    def is_expense(self) -> bool:
        return self.transaction_type == TransactionType.EXPENSE

    def is_valid_amount(self) -> bool:
        return self.amount > Decimal("0")

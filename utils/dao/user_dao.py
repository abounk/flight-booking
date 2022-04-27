from sqlalchemy.orm.session import Session
from models.user import User
from utils.dao.dao_base import Dao


class UserDao(Dao):

    def get_user_by_id(self, id: int) -> User:
        """Get user by id.

        Args:
            id (int): User's ID.

        Returns:
            User: User with specified ID.
        """
        return self.session.query(User).filter(User.id == id)[0]

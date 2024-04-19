from pydantic import BaseModel


class UserDTO(BaseModel):
    user_id: int
    username: str
    email: str

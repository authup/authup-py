from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from authup.domains.constants import DomainType
from authup.domains.types_base import DomainEventBaseContext


class Realm(BaseModel):
    id: Optional[str]
    name: str
    description: Optional[str] = None
    built_in: bool = False
    created_at: str = datetime.now().isoformat()
    updated_at: str = datetime.now().isoformat()


class RealmEventContext(DomainEventBaseContext):
    type: str = f"{DomainType.REALM}"
    data: Realm


class RealmCreate(Realm):
    pass


class RealmUpdate(Realm):
    updated_at = datetime.now().isoformat()
    pass

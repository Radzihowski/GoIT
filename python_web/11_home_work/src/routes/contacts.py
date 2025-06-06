from typing import List
from pprint import pprint

from fastapi import APIRouter, HTTPException, Depends, status
# from sqlalchemy.orm import Session
from src.schemas.contacts import ContactRequest, ContactResponse
from src.services.contacts import ContactService

router = APIRouter(prefix='/contacts', tags=["contacts"])

@router.post("/", response_model=ContactResponse)
async def create_contact(body: ContactRequest):
    service = ContactService()
    response = await service.create_contact(body)
    return response



# @router.get("/", response_model=List[TagResponse])
# async def read_tags(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     tags = await repository_tags.get_tags(skip, limit, db)
#     return tags

#
# @router.get("/{tag_id}", response_model=TagResponse)
# async def read_tag(tag_id: int, db: Session = Depends(get_db)):
#     tag = await repository_tags.get_tag(tag_id, db)
#     if tag is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
#     return tag
#


#
#
# @router.put("/{tag_id}", response_model=TagResponse)
# async def update_tag(body: TagModel, tag_id: int, db: Session = Depends(get_db)):
#     tag = await repository_tags.update_tag(tag_id, body, db)
#     if tag is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
#     return tag
#
#
# @router.delete("/{tag_id}", response_model=TagResponse)
# async def remove_tag(tag_id: int, db: Session = Depends(get_db)):
#     tag = await repository_tags.remove_tag(tag_id, db)
#     if tag is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
#     return tag

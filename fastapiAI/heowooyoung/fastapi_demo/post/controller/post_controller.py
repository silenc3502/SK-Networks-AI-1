from typing import List

from aiomysql import Pool
from fastapi import APIRouter, Depends

from async_db.database import getMySqlPool
from post.entity.models import Post
from post.service.post_service_impl import PostServiceImpl

postRouter = APIRouter()


async def injectPostService(db_poll: Pool = Depends(getMySqlPool)) -> PostServiceImpl:
    return PostServiceImpl(db_poll)

@postRouter.get("/list", response_model=List[Post])
async def postList(postService: PostServiceImpl = Depends(injectPostService)):

    print(f"postList()")
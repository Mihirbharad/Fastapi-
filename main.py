from fastapi import FastAPI # type: ignore
from routes.RoleRoutes import router as role_router
from routes.UserRoutes import router as user_router
from routes.StateRoutes import router as state_router
from routes.CityRoutes import router as city_router
from routes.CategoryRoutes import router as category_router
from routes.SubCategoryRoutes import router as sub_category_router
from routes.ProductRoutes import router as product_router
from routes.ReviewRoutes import router as review_router
from config.BeanieHelper import init_db



from fastapi.middleware.cors import CORSMiddleware # type: ignore


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def start_db():
    await init_db()
    

app.include_router(role_router)
app.include_router(user_router)
app.include_router(state_router)
app.include_router(city_router)
app.include_router(category_router)
app.include_router(sub_category_router)
app.include_router(product_router)
app.include_router(review_router)





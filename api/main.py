from fastapi import FastAPI
from books.routers import router as book_router

# Set API info
app = FastAPI(
    title="Example API",
    description="This is an example API of FastAPI",
    docs_url="/v1/docs",
    redoc_url="/v1/redoc",
    openapi_url="/v1/openapi.json",
)

app.include_router(book_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



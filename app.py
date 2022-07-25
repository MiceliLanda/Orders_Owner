from fastapi import FastAPI
import uvicorn
from routes.owner import orderRoute

app = FastAPI()
app.include_router(orderRoute)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=9000, reload=True)
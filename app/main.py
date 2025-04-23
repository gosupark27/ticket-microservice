from fastapi import FastAPI

app = FastAPI(
    title="Shoe Repair Ticket Microservice",
    description="Backend service for ticket creation and management",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Ticket Microservice - Operational 🔥"}
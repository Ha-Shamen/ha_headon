import uvicorn


if __name__ == "__main__":
    uvicorn.run("api.web_service:app", host="0.0.0.0", port=3001, reload=True)
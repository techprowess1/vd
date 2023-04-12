import uvicorn

if __name__ == "__main__":
    uvicorn.run("dl_api:app", port=8000, reload=True)

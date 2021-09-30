import uvicorn


def main():
    uvicorn.run("fastpypi.main:api", host="0.0.0.0", port=8000, log_config="logging.yaml", reload=True)


if __name__ == "__main__":
    main()

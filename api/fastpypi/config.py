from pydantic import BaseSettings


class Settings(BaseSettings):
    api_v1_str: str = "/v1"
    repo_dir: str = "/home/apps/repo"
    root_path: str = "/api"

    class Config:
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

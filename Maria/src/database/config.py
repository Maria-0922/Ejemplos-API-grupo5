from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Carpeta raíz del proyecto (Maria/), para encontrar el .env sin importar
# desde qué directorio se ejecute el servidor.
BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Cadena de conexión a la base de datos. Nunca se escribe aquí:
    # se lee desde el archivo .env (que no se sube a GitHub).
    database_url: str

    @property
    def sqlalchemy_url(self) -> str:
        if self.database_url.startswith("postgresql://"):
            return self.database_url.replace(
                "postgresql://",
                "postgresql+psycopg://",
                1,
            )
        return self.database_url


settings = Settings()
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Carpeta raíz del proyecto (Maria/), para encontrar el .env sin importar
# desde qué directorio se ejecute el servidor.
BASE_DIR = Path(__file__).resolve().parents[2]

# Valor por defecto para que la API funcione sin configurar nada.
# Si existe un archivo .env con DATABASE_URL, ese valor tiene prioridad.
DEFAULT_DATABASE_URL = (
    "postgresql://neondb_owner:npg_F4fpBHiDWj0K@"
    "ep-noisy-rain-axzog8km-pooler.c-4.us-east-2.aws.neon.tech/neondb?sslmode=require"
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Cadena de conexión a Neon PostgreSQL
    database_url: str = DEFAULT_DATABASE_URL

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

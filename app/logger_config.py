from loguru import logger
import sys

def setup_app_logger():
    # Remove o log padrão do Loguru
    logger.remove()

    # Configura o log no terminal, melhor view
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="INFO"
    )

    # Configura o log em arquivo, historico
    logger.add(
        "erros.log",
        rotation="10 MB",
        retention="10 days",
        level="ERROR",
        backtrace=True, # show error detail
        diagnose=True   # Mostra os valores das variáveis
    )

    return logger
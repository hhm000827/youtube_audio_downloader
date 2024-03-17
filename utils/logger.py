import inspect
import logging

from attr import define, field


@define(frozen=True)
class Logger:
    log_format: str = field(default="%(asctime)s - %(filename)s - %(levelname)s - %(message)s", init=False)
    date_format: str = field(default="%Y-%m-%d %H:%M:%S", init=False)
    handler: logging.StreamHandler = field(default=logging.StreamHandler(), init=False)
    logger: logging.Logger = field(default=logging.getLogger(), init=False)
    logger_name: str = field(default=inspect.stack()[-1].filename.split("\\")[-1].split(".")[0])
    log_level: int = field(default=logging.DEBUG)

    def __attrs_post_init__(self):
        self.logger.name = self.logger_name
        self.handler.setLevel(self.log_level)
        self.handler.setFormatter(logging.Formatter(self.log_format, datefmt=self.date_format))
        self.logger.addHandler(self.handler)
        self.logger.setLevel(self.log_level)
        self.logger.propagate = False

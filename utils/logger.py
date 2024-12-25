import inspect
import logging

from attrs import define, field
from rich.logging import RichHandler


@define(frozen=True)
class Logger:
    log_format: str = field(default="%(filename)s : %(message)s", init=False)
    date_format: str = field(default="%Y-%m-%d %H:%M:%S", init=False)
    handler: logging.StreamHandler = field(init=False, default=RichHandler())
    logger: logging.Logger = field(default=logging.getLogger(), init=False)
    logger_name: str = field(default=inspect.stack()[-1].filename.split("\\")[-1].split(".")[0])
    log_level: int = field(default=logging.INFO)

    def __attrs_post_init__(self):
        self.logger.name = self.logger_name
        self.logger.setLevel(self.log_level)
        self.logger.propagate = False
        self.logger.addHandler(self.handler)
        self.handler.setLevel(self.log_level)
        self.handler.setFormatter(logging.Formatter(self.log_format, self.date_format))

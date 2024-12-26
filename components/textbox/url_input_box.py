import validators
from attr import define, field
from pydash import is_blank

from constant import GLOBAL_PADDING_Y
from utils import Logger
from .base_text_box import BaseTextBox
from .. import Button

logger = Logger().logger


@define
class URLInputBox(BaseTextBox):
    label_text: str = field(default="Youtube URLs:", init=False)
    clear_button: Button = field(init=False)

    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.clear_button = Button(self, text="Clear", row=2, column=0, sticky="w", padding_y=(GLOBAL_PADDING_Y, 0),
                                   command=lambda: self.clear(), button_color="firebrick")

    def read_urls(self) -> list[str]:
        logger.info(f"Start reading URLs...")
        text = self.textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
        urls = [item.strip() for item in text.split("\n") if
                not is_blank(item.strip()) and validators.url(item.strip())]
        logger.info(f"There are {len(urls)} valid URLs")
        return urls

    def is_enable(self, enable=True):
        self.textbox.configure(state="normal" if enable else "disabled")

    def clear(self):
        self.textbox.delete("1.0", "end")

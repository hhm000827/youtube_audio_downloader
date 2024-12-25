from attr import define, field

from utils import Logger
from .base_text_box import BaseTextBox

logger = Logger().logger


@define
class URLInputBox(BaseTextBox):
    label_text: str = field(default="Youtube URLs:", init=False)

    def __attrs_post_init__(self):
        super().__attrs_post_init__()

    def read_urls(self):
        text = self.textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
        logger.info(f"Read URLs:\n{text}")
        return text

    def is_enable(self, enable=True):
        self.textbox.configure(state="normal" if enable else "disabled")

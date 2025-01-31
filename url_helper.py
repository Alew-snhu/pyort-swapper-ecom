import pyperclip
from pynput.keyboard import Key, Controller

class UrlHelper:
    def __init__(self):
        self.local_host = "localhost:"
        self.chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        self.default_store_url = "http://localhost:12795/GP3/package-detail-shell.aspx?eid=14741&cid=6932&lastaction=viewall"

    @classmethod
    def get_url(cls):
        controller = Controller()
        controller.press(Key.ctrl)
        controller.press('a')
        controller.release('a')
        controller.release(Key.ctrl)

        controller.press(Key.ctrl)
        controller.press('c')
        controller.release('c')
        controller.release(Key.ctrl)
        return pyperclip.paste()

    def parse_modify_url(self, url):

        local_host = url.find(self.local_host)
        if local_host == -1 or local_host > 8:
            raise "no local host here"

        # replace port
        new_port_url = url.replace("12795", "6338")

        # remove store name
        indices = self.get_indices(new_port_url, "/")
        store_name = new_port_url[indices[2] : indices[3]]
        removed_store_url = new_port_url.replace(store_name, '')

        # replace aspx page with html dev page
        indices = self.get_indices(removed_store_url, "/")
        last_slash_index = indices[-1]
        question_mark_index = removed_store_url.find("?")
        text_to_replace = removed_store_url[last_slash_index : question_mark_index]
        replacement_text = self.get_html_replacement(text_to_replace)
        return removed_store_url.replace(text_to_replace, replacement_text)

    @classmethod
    def get_html_replacement(cls, aspx_file):
        match aspx_file:
            case "store.aspx":
                return "store.html"
            case "product-detail-shell.aspx":
                return "product-detail-dev.html"
            case "cart.aspx":
                return "cart-dev.html"
            case "checkout-review.aspx":
                return "checkout-review-dev.html"
            case "package-detail-shell.aspx":
                return "package-detail-dev.html"


    @classmethod
    def get_indices(cls, url: str, char: str):
        indices = []
        for i, c in enumerate(url):
            if c == char:
                indices.append(i + 1)
        return indices


import pytest
from HomophoneSearch.chinese.transfer import ChineseTransfer




@pytest.mark.parametrize(
        "text, language",
        (
            ("Hello", "english"),
            ("哈囉", "chinese"),
            )
        )
def test_transfer(text, language):
    
    return_value = ChineseTransfer.text_to_text(text)
    if language == "chinese":
        assert return_value
        assert isinstance(return_value, list)


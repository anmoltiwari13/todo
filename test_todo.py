from todo import add,clear,li
def test_add():
    """To add"""
    add("Buy milk")
    assert "Buy milk" in li

def test_clear():
    """To clear"""
    add("Buy milk")
    clear()
    assert len(li) == 0

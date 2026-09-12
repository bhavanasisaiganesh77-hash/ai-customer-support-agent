from src.intent.classifier import classify_message


def test_internet_issue():
    assert classify_message("My internet is not working") == "internet_wifi_issue"


def test_billing_issue():
    assert classify_message("I was charged an unexpected fee") == "billing_charges"


def test_router_issue():
    assert classify_message("My router has a red light") == "equipment_router"


def test_account_login():
    assert classify_message("I cannot login to my Verizon account") == "account_login"


def test_plan_upgrade():
    assert classify_message("I want to upgrade my plan") == "plan_product_upgrade"

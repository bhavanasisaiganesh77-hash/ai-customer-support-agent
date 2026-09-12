from src.intent.classifier import classify_message


def test_connection_drops():
    assert classify_message("The connection keeps dropping every few minutes") == "internet_wifi_issue"


def test_unexpected_charge():
    assert classify_message("Someone charged me more than expected this month") == "billing_charges"


def test_cannot_get_online():
    assert classify_message("I can't get online at home") == "internet_wifi_issue"


def test_red_router_indicator():
    assert classify_message("The device in my house is showing a red indicator") == "equipment_router"


def test_installation_request():
    assert classify_message("I need someone to come install my service") == "installation_availability"


def test_better_package():
    assert classify_message("Can I get a better package for my current service?") == "plan_product_upgrade"

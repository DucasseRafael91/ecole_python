from ecole.models.address import Address


def test_address_str():
    address = Address(street="28 rue des jonquilles", city="Paris", postal_code=75000)
    expected_value = "28 rue des jonquilles, 75000 Paris"
    assert str(address) == expected_value


def test_address_attributes():
    address = Address(street="28 rue des jonquilles", city="Paris", postal_code=75000)
    assert address.street == "28 rue des jonquilles"
    assert address.city == "Paris"
    assert address.postal_code == 75000
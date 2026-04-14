from ecole.models.address import Address

class MockResponse:
    def __str__(self):
        return "28 rue des jonquilles, 75000 Paris"

def test_address_str(mocker):
    mocker.patch('ecole.models.address.Address', return_value=MockResponse())

    address = Address(street="28 rue des jonquilles", city="Paris", postal_code=75000)
    expected_value = "28 rue des jonquilles, 75000 Paris"

    assert str(address) == expected_value

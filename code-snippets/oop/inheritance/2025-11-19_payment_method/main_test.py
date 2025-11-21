from main import *


run_cases = [
    ([1200, 300], CreditCard(international=False), 1573),
    ([12000], BankTransfer(), 12000),
    ([5000], Crypto(network_fee_cents=75), 5050),
]

submit_cases = run_cases + [
    ([2000, 2000], CreditCard(international=True), 4246),
    ([9999], BankTransfer(), 10024),
    ([100], Crypto(network_fee_cents=75), 175),
    ([], CreditCard(international=False), 0),
    ([2500, 2500, 2500], CreditCard(international=False), 7747),
]


def method_description(method):
    cls = method.__class__.__name__
    if cls == "CreditCard":
        return f"CreditCard(international={method.international})"
    if cls == "BankTransfer":
        return "BankTransfer()"
    if cls == "Crypto":
        return f"Crypto(network_fee_cents={method.network_fee_cents})"
    return cls


def test(items, method, expected_total):
    print("---------------------------------")
    print("Input:")
    print(f"  Items (cents): {items}")
    print(f"  Method:        {method_description(method)}")
    try:
        result = checkout_total_cents(items, method)
        print(f"Expected total: {expected_total}")
        print(f"Actual total:   {result}")
        if result == expected_total:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for case in test_cases:
        ok = test(*case)
        if ok:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

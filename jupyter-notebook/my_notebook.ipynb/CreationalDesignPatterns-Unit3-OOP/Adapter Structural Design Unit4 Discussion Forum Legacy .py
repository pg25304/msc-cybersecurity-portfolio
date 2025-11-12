class LegacyPaymentSystem:
    def make_payment(self, amount):
        # Simulate SOAP request
        return f"Payment made: {amount}"
class EcommercePlatform:
    def __init__(self):
        self.adapter = None
    def make_payment(self, amount):
        # Simulate RESTful request with JSON payload
        payload = {"amount": amount}
        # Call the Adapter's make_payment method
        if self.adapter is None:
            raise RuntimeError("No adapter configured on EcommercePlatform")
        response = self.adapter.make_payment(payload)
        return response
class Adapter:
    def __init__(self, legacy_payment_system):
        self.legacy_payment_system = legacy_payment_system
    def make_payment(self, payload):
        # Translate JSON payload to SOAP message (omitted for simplicity)
        # Send translated request to the legacy payment system
        response = self.legacy_payment_system.make_payment(payload["amount"])
        # Translate SOAP response back to JSON-like structure
        return {"status": "success", "message": response}
if __name__ == "__main__":
    legacy_payment_system = LegacyPaymentSystem()
    adapter = Adapter(legacy_payment_system)
    ecommerce_platform = EcommercePlatform()
    ecommerce_platform.adapter = adapter  # Inject the Adapter into the EcommercePlatform instance
    result = ecommerce_platform.make_payment(50)
    print(result)  # Output: {'status': 'success', 'message': 'Payment made: 50'}

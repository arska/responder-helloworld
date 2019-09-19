"""
Example project to test the responder framework

https://python-responder.org/en/latest/
https://github.com/kennethreitz/responder/
"""
import os
import responder

API = responder.API()


@API.route("/")
def hello_world(req, resp):  # pylint: disable=unused-argument
    """
    Example endpoint without any parameters
    """
    resp.text = "hello, world!"


if __name__ == "__main__":
    API.run(address="0.0.0.0", port=os.environ.get("PORT", 8080))

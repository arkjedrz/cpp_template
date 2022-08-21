from conans import ConanFile

class cpp_templateConan(ConanFile):
    """
    Dependencies for cpp_template app.
    """
    name = "cpp_template"
    settings = "os", "compiler", "build_type", "arch"
    requires = "gtest/1.11.0"
    generators = "cmake"
    options = {
        # "option_name": [True, False],
    }
    default_options = {
        # "option_name": False
    }

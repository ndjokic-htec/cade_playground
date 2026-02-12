load("@rules_python//python:defs.bzl", "py_test")

py_test(
    name = "test_dummy_logger",
    srcs = [
        "test_dummy_logger.py",
    ],
    deps = [
       "//python:dummy_logger",
       "//python/random_print_library:random_print_library",
    ],
    data = [
        "//c/timestamp_provider:timestamp_provider",
    ],
    visibility = ["//visibility:public"],
)


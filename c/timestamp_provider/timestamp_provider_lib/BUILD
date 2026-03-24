load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_library")
cc_library(
    name = "timestamp_provider_lib",
    srcs = ["timestamp_provider.c"],
    hdrs = ["timestamp_provider.h"],
    includes = ["./"],
    deps = ["//c/timestamp_provider/timestamp_parser_lib:timestamp_parser_lib"], 
    visibility = ["//visibility:public"],
)
{
  "targets": [
    {
      "target_name": "binding",
      "sources": [
        "src/binding.cc",
        "src/utils.cc",
        "src/py_object_wrapper.cc"
      ],
      "conditions": [
        ['OS=="mac"', {
            "xcode_settings": {
              "OTHER_CFLAGS": [
                "-Wno-error=unused-command-line-argument",
                "<!(/usr/bin/python3-config --cflags)"
              ],
              "OTHER_LDFLAGS": [
                "<!(/usr/bin/python3-config --ldflags)"
              ]
            }
        }],['OS=="linux"',{
          "cflags": [
            "<!(python3-config --cflags)"
          ],
          "libraries": [
            "<!(python3-config --libs)"
          ]
        }],['OS=="win"',{
          "include_dirs": [
            "<(module_root_dir)/libs/pyheader"
          ],
          "link_settings": {
            "libraries": [
              "<(module_root_dir)/libs/python35.lib"
            ]
          }
        }]
      ]
    }
  ]
}
